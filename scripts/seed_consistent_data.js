// scripts/seed_consistent_data.js
const mongoose = require('mongoose');
const Person = require('../src/models/people.model');
const bcrypt = require('bcryptjs');

const MONGO_URI = process.env.MONGO_URI || "mongodb://localhost:27017/";
const MONGO_DB_NAME = process.env.MONGO_DB_NAME || "fdfed";

const seed = async () => {
  try {
    console.log('------------------------------------------------');
    console.log('🔌 Connecting to MongoDB...');
    
    await mongoose.connect(MONGO_URI, { dbName: MONGO_DB_NAME });
    console.log('✅ Connected.');

    // Helper to hash passwords individually
    const hashPwd = async (pwd) => await bcrypt.hash(pwd, 10);

    // Define Users with ORIGINAL Passwords & Rich Data
    const users = [
      // --- ADVISORS (Restoring Passwords) ---
      {
        name: "Advisor 1",
        email: "advisor1@drakz.com",
        password: await hashPwd("Advisor1@123"), // ✅ Original Password
        pan: "DRVAD1234A",
        role: "advisor"
      },
      {
        name: "Advisor 2",
        email: "advisor2@drakz.com",
        password: await hashPwd("Advisor2@123"), // ✅ Original Password
        pan: "DRVAD1234B",
        role: "advisor"
      },

      // --- USERS (Restoring Passwords + Rich Data) ---
      {
        name: "User 1",
        email: "user1@drakz.com",
        password: await hashPwd("User1@123"), // ✅ User1@123
        pan: "DRVUS1234A",
        role: "user",
        portfolioValue: 2500000, 
        riskProfile: "Aggressive",
        activeGoals: 5,
        monthlyIncome: 150000,
        totalDebt: 45000,
        creditScore: 780,
        occupation: "Software Architect",
        phone: "+91 98765 43210"
      },
      {
        name: "User 2",
        email: "user2@drakz.com",
        password: await hashPwd("User2@123"), // ✅ User2@123
        pan: "DRVUS1234B",
        role: "user",
        portfolioValue: 450000,
        riskProfile: "Conservative",
        activeGoals: 2,
        monthlyIncome: 65000,
        totalDebt: 12000,
        creditScore: 820,
        occupation: "Government Teacher",
        phone: "+91 91234 56789"
      },
      {
        name: "User 3",
        email: "user3@drakz.com",
        password: await hashPwd("User3@123"), // ✅ User3@123
        pan: "DRVUS1234C",
        role: "user",
        portfolioValue: 875000,
        riskProfile: "Moderate",
        activeGoals: 3,
        monthlyIncome: 95000,
        totalDebt: 250000,
        creditScore: 690,
        occupation: "Marketing Manager",
        phone: "+91 88888 77777"
      },
      {
        name: "User 4",
        email: "user4@drakz.com",
        password: await hashPwd("User4@123"), // ✅ User4@123
        pan: "DRVUS1234D",
        role: "user",
        portfolioValue: 25000,
        riskProfile: "Aggressive",
        activeGoals: 1,
        monthlyIncome: 25000,
        totalDebt: 5000,
        creditScore: 650,
        occupation: "Freelancer",
        phone: "+91 77777 66666"
      },
      {
        name: "User 5",
        email: "user5@drakz.com",
        password: await hashPwd("User5@123"), // ✅ User5@123
        pan: "DRVUS1234E",
        role: "user",
        portfolioValue: 5500000,
        riskProfile: "Conservative",
        activeGoals: 0,
        monthlyIncome: 120000,
        totalDebt: 0,
        creditScore: 850,
        occupation: "Retired Officer",
        phone: "+91 99999 11111"
      }
    ];

    // Upsert (Update existing, Create new)
    for (const u of users) {
      const result = await Person.findOneAndUpdate(
        { email: u.email }, 
        { $set: u }, 
        { upsert: true, new: true, setDefaultsOnInsert: true }
      );
      console.log(`👤 Updated: ${result.name} (${result.email})`);
    }

    console.log('------------------------------------------------');
    console.log('🎉 SUCCESS: Passwords restored & Data updated.');
    console.log('------------------------------------------------');
    
    process.exit();
  } catch (err) {
    console.error('❌ Error:', err);
    process.exit(1);
  }
};

seed();