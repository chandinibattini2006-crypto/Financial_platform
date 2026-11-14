import { MongoClient } from 'mongodb';
import bcrypt from 'bcryptjs';
import dotenv from 'dotenv';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

dotenv.config({ path: path.join(__dirname, '..', '.env') });

const MONGO_URI = process.env.MONGO_URI || "mongodb://localhost:27017/";

const adminsData = [
  {
    name: "Chandini Admin",
    email: "chandiniadmin@gmail.com",
    password: "chandini123",
    dob: new Date('1998-01-01')
  },
  {
    name: "Krishna Gupta",
    email: "krishna.gpt607@gmail.com",
    password: "admin_krishna",
    dob: new Date('1995-03-15')
  },
  {
    name: "Ziko Ahmed",
    email: "ziko120204@gmail.com",
    password: "admin_ziko",
    dob: new Date('1998-12-02')
  },
  {
    name: "venky",
    email: "venky045@gmail.com",
    password: "@venky210606",
    dob: new Date('2005-07-23')
  }
];

async function insertAdmins() {
  const client = new MongoClient(MONGO_URI);
  
  try {
    await client.connect();
    console.log('Connected to MongoDB');
    
    const db = client.db('fdfed');
    const collection = db.collection('people');

    let upsertedCount = 0;
    let modifiedCount = 0;

    for (const admin of adminsData) {
      const passwordHash = await bcrypt.hash(admin.password, 10);

      const result = await collection.updateOne(
        { email: admin.email.toLowerCase() },
        {
          $set: {
            name: admin.name,
            email: admin.email.toLowerCase(),
            password: passwordHash,
            role: 'admin',
            dob: admin.dob,
            isApproved: true,
            isRejected: false,
            status: 'Active'
          },
          $setOnInsert: {
            created_at: new Date()
          }
        },
        { upsert: true }
      );

      upsertedCount += result.upsertedCount || 0;
      modifiedCount += result.modifiedCount || 0;
    }

    console.log(`Admin upsert complete. Inserted: ${upsertedCount}, Updated: ${modifiedCount}`);
    console.log('Admins are now available in people collection for auth login.');
    
  } catch (error) {
    console.error('Error inserting admins:', error);
  } finally {
    await client.close();
  }
}

insertAdmins();