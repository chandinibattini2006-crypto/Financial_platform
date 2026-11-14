import { MongoClient } from 'mongodb';
import bcrypt from 'bcryptjs';
import dotenv from 'dotenv';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

dotenv.config({ path: path.join(__dirname, '..', '.env') });

const MONGO_URI = process.env.MONGO_URI || "mongodb://localhost:27017/";

const advisorsData = [
  {
    name: "Chandini Adviser",
    email: "chandiniadviser@gmail.com",
    password: "chandini123",
    phone: "+91-9876500003",
    advisorProfile: {
      specialization: "financial_planning",
      bio: "Certified financial advisor and wealth management expert",
      experience: 5,
      price: 500,
      contactEmail: "chandiniadviser@gmail.com",
      contactPhone: "+91-9876500003",
      isAcceptingClients: true
    }
  },
  {
    name: "XD Phantom",
    email: "xdphantom1202@gmail.com",
    password: "advisor_xd",
    phone: "+91-9876543210",
    advisorProfile: {
      specialization: "stocks",
      bio: "Expert in stock market and portfolio management",
      experience: 8,
      price: 500,
      contactEmail: "xdphantom1202@gmail.com",
      contactPhone: "+91-9876543210",
      isAcceptingClients: true
    }
  },
  {
    name: "Zulqar Ahmed",
    email: "zulqar.ahmed.12@gmail.com",
    password: "advisor_zulqar",
    phone: "+91-9123456789",
    advisorProfile: {
      specialization: "investments",
      bio: "Certified investment advisor with 10 years experience",
      experience: 10,
      price: 750,
      contactEmail: "zulqar.ahmed.12@gmail.com",
      contactPhone: "+91-9123456789",
      isAcceptingClients: true
    }
  }
];

async function insertAdvisors() {
  const client = new MongoClient(MONGO_URI);
  
  try {
    await client.connect();
    console.log('Connected to MongoDB');
    
    const db = client.db('fdfed');
    const collection = db.collection('people'); // Changed to 'people' collection
    
    const advisorsWithHashedPasswords = await Promise.all(
      advisorsData.map(async (advisor) => ({
        name: advisor.name,
        email: advisor.email.toLowerCase(),
        password: await bcrypt.hash(advisor.password, 10),
        phone: advisor.phone,
        role: 'advisor', // Set role as advisor
        isApproved: true, // Auto-approve advisors
        isRejected: false,
        status: 'Active',
        advisorProfile: advisor.advisorProfile,
        created_at: new Date()
      }))
    );
    
    const result = await collection.insertMany(advisorsWithHashedPasswords);
    console.log(`${result.insertedCount} advisors inserted successfully`);
    
  } catch (error) {
    console.error('Error inserting advisors:', error);
  } finally {
    await client.close();
  }
}

insertAdvisors();