const { MongoClient } = require('mongodb');
const bcrypt = require('bcryptjs');
const path = require('path');
const fs = require('fs');
const { MongoMemoryServer } = require('mongodb-memory-server');

async function run() {
  const dbPath = path.join(__dirname, '..', 'mongodb_data');
  if (!fs.existsSync(dbPath)) {
    fs.mkdirSync(dbPath, { recursive: true });
  }

  let mongod = null;
  let uri = 'mongodb://127.0.0.1:27017/';

  // Check if MongoDB is already running or start embedded instance
  try {
    const testClient = new MongoClient(uri, { serverSelectionTimeoutMS: 2000 });
    await testClient.connect();
    await testClient.close();
    console.log('✅ Connected to existing MongoDB on 27017');
  } catch (e) {
    console.log('Starting embedded MongoDB for account setup...');
    mongod = await MongoMemoryServer.create({
      instance: {
        port: 27017,
        dbPath: dbPath,
        storageEngine: 'wiredTiger',
      },
    });
    uri = mongod.getUri();
    console.log('✅ Embedded MongoDB started at:', uri);
  }

  const client = new MongoClient(uri);
  await client.connect();
  const db = client.db('fdfed');
  const peopleCollection = db.collection('people');
  const usersCollection = db.collection('users');

  const passwordHash = await bcrypt.hash('chandini123', 10);

  // 1. User Account
  const userDoc = {
    name: 'Chandini User',
    email: 'chandiniuser@gmail.com'.toLowerCase(),
    password: passwordHash,
    phone: '+91-9876500001',
    role: 'user',
    pan: 'CHAND1234F',
    occupation: 'Financial Analyst',
    monthlyIncome: 120000,
    creditScore: 780,
    totalDebt: 30000,
    profilePicture: '',
    kycStatus: 'verified',
    status: 'Active',
    isApproved: true,
    isRejected: false,
    updated_at: new Date(),
  };

  await peopleCollection.updateOne(
    { email: userDoc.email },
    { $set: userDoc, $setOnInsert: { created_at: new Date() } },
    { upsert: true }
  );

  await usersCollection.updateOne(
    { email: userDoc.email },
    {
      $set: {
        name: 'Chandini User',
        email: userDoc.email,
        password_hash: passwordHash,
        role: 'normal',
        updated_at: new Date(),
      },
      $setOnInsert: { created_at: new Date() },
    },
    { upsert: true }
  );
  console.log('✅ User account created: chandiniuser@gmail.com');

  // 2. Admin Account
  const adminDoc = {
    name: 'Chandini Admin',
    email: 'chandiniadmin@gmail.com'.toLowerCase(),
    password: passwordHash,
    role: 'admin',
    dob: new Date('1998-01-01'),
    phone: '+91-9876500002',
    status: 'Active',
    isApproved: true,
    isRejected: false,
    updated_at: new Date(),
  };

  await peopleCollection.updateOne(
    { email: adminDoc.email },
    { $set: adminDoc, $setOnInsert: { created_at: new Date() } },
    { upsert: true }
  );
  console.log('✅ Admin account created: chandiniadmin@gmail.com');

  // 3. Advisor Account
  const advisorDoc = {
    name: 'Chandini Adviser',
    email: 'chandiniadviser@gmail.com'.toLowerCase(),
    password: passwordHash,
    phone: '+91-9876500003',
    role: 'advisor',
    isApproved: true,
    isRejected: false,
    status: 'Active',
    advisorProfile: {
      specialization: 'financial_planning',
      bio: 'Certified financial advisor and wealth management expert',
      experience: 5,
      price: 500,
      contactEmail: 'chandiniadviser@gmail.com',
      contactPhone: '+91-9876500003',
      isAcceptingClients: true,
    },
    updated_at: new Date(),
  };

  await peopleCollection.updateOne(
    { email: advisorDoc.email },
    { $set: advisorDoc, $setOnInsert: { created_at: new Date() } },
    { upsert: true }
  );
  console.log('✅ Advisor account created: chandiniadviser@gmail.com');

  await client.close();

  if (mongod) {
    await mongod.stop();
    console.log('MongoDB stopped cleanly.');
  }

  console.log('\n🎉 All 3 accounts successfully saved to database!');
}

run().catch((err) => {
  console.error('Error creating accounts:', err);
  process.exit(1);
});
