const mongoose = require('mongoose');
const path = require('path');
const fs = require('fs');

let embeddedMongo = null;

const connectDB = async () => {
  const mongoUri = process.env.MONGO_URI || 'mongodb://localhost:27017/';
  const mongoDbName = process.env.MONGO_DB_NAME || 'fdfed';

  try {
    const isLocal = mongoUri.includes('localhost') || mongoUri.includes('127.0.0.1');
    await mongoose.connect(mongoUri, {
      dbName: mongoDbName,
      serverSelectionTimeoutMS: isLocal ? 2500 : 10000,
    });
    console.log('MongoDB Connected');
  } catch (err) {
    if (mongoUri.includes('localhost') || mongoUri.includes('127.0.0.1')) {
      console.log('⚠️ Local MongoDB not found on port 27017. Starting embedded MongoDB...');
      try {
        const { MongoMemoryServer } = require('mongodb-memory-server');
        const dbPath = path.join(__dirname, '../../mongodb_data');
        if (!fs.existsSync(dbPath)) {
          fs.mkdirSync(dbPath, { recursive: true });
        }

        embeddedMongo = await MongoMemoryServer.create({
          instance: {
            port: 27017,
            dbPath: dbPath,
            storageEngine: 'wiredTiger',
          },
        });

        console.log(`✅ Embedded MongoDB running at: ${embeddedMongo.getUri()}`);
        await mongoose.connect(embeddedMongo.getUri(), { dbName: mongoDbName });
        console.log('MongoDB Connected (Embedded)');

        const shutdown = async () => {
          if (embeddedMongo) {
            console.log('Stopping embedded MongoDB...');
            await embeddedMongo.stop();
          }
        };
        process.on('SIGINT', shutdown);
        process.on('SIGTERM', shutdown);
        return;
      } catch (embeddedErr) {
        console.error('Embedded MongoDB Error:', embeddedErr.message);
      }
    }

    console.error('DB Connection Error:', err.message);
    process.exit(1);
  }
};

module.exports = connectDB;
