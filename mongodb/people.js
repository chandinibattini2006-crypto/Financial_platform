import { MongoClient } from 'mongodb';
import bcrypt from 'bcryptjs';
import dotenv from 'dotenv';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

dotenv.config({ path: path.join(__dirname, '..', '.env') });

const MONGO_URI = process.env.MONGO_URI || "mongodb://localhost:27017/";

const peopleData = [
  // Test Users (role: user)
  {
    name: "Chandini User",
    email: "chandiniuser@gmail.com",
    password: "chandini123",
    phone: "+91-9876500001",
    role: "user",
    pan: "CHAND1234F",
    occupation: "Financial Analyst",
    monthlyIncome: 120000,
    creditScore: 780,
    totalDebt: 30000,
    profilePicture: "",
    kycStatus: "verified",
    status: "Active",
    isApproved: true
  },
  {
    name: "Ahmed Zulqar",
    email: "ahmed.z23@iiits.in",
    password: "user_ahmed",
    phone: "+91-9876543210",
    role: "user",
    pan: "AHMED1234A",
    occupation: "Software Engineer",
    monthlyIncome: 100000,
    creditScore: 750,
    totalDebt: 50000,
    profilePicture: "",
    kycStatus: "verified",
    status: "Active",
    isApproved: true
  },
  {
    name: "Krishna Govind",
    email: "krishna.g23@iiits.in",
    password: "user_krishna",
    phone: "+91-9987654321",
    role: "user",
    pan: "KRISH5678B",
    occupation: "Data Scientist",
    monthlyIncome: 125000,
    creditScore: 780,
    totalDebt: 75000,
    profilePicture: "",
    kycStatus: "verified",
    status: "Active",
    isApproved: true
  },
  {
    name: "Ragamaie N",
    email: "ragamaie.n23@iiits.in",
    password: "user_ragamaie",
    phone: "+91-9876543211",
    role: "user",
    pan: "RAGAM9012C",
    occupation: "Product Manager",
    monthlyIncome: 150000,
    creditScore: 800,
    totalDebt: 100000,
    profilePicture: "",
    kycStatus: "verified",
    status: "Active",
    isApproved: true
  },
  {
    name: "Deepthi M",
    email: "deepthi.m23@iiits.in",
    password: "user_deepthi",
    phone: "+91-9876543212",
    role: "user",
    pan: "DEEPT3456D",
    occupation: "UI/UX Designer",
    monthlyIncome: 80000,
    creditScore: 720,
    totalDebt: 40000,
    profilePicture: "",
    kycStatus: "pending",
    status: "Active",
    isApproved: true
  },
  {
    name: "Abhinay M",
    email: "abhinay.m23@iiits.in",
    password: "user_abhinay",
    phone: "+91-9876543213",
    role: "user",
    pan: "ABHIN7890E",
    occupation: "DevOps Engineer",
    monthlyIncome: 115000,
    creditScore: 760,
    totalDebt: 60000,
    profilePicture: "",
    kycStatus: "verified",
    status: "Active",
    isApproved: true
  }
];

async function insertPeople() {
  const client = new MongoClient(MONGO_URI);
  
  try {
    await client.connect();
    console.log('Connected to MongoDB');
    
    const db = client.db('fdfed');
    const collection = db.collection('people');
    
    // Hash passwords and prepare data
    const peopleWithHashedPasswords = await Promise.all(
      peopleData.map(async (person) => ({
        ...person,
        password: await bcrypt.hash(person.password, 10)
      }))
    );
    
    const result = await collection.insertMany(peopleWithHashedPasswords);
    console.log(`${result.insertedCount} user records inserted successfully`);
    console.log('\nTest Users available for login:');
    peopleData.forEach(user => {
      console.log(`  ${user.name} (${user.email}) / ${user.password}`);
    });
    
  } catch (error) {
    console.error('Error inserting people:', error);
  } finally {
    await client.close();
  }
}

insertPeople();