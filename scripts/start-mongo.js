const { MongoMemoryServer } = require('mongodb-memory-server');
const path = require('path');
const fs = require('fs');

async function startMongo() {
  const dbPath = path.join(__dirname, '..', 'mongodb_data');
  if (!fs.existsSync(dbPath)) {
    fs.mkdirSync(dbPath, { recursive: true });
  }

  console.log('🚀 Starting embedded MongoDB server on port 27017...');
  try {
    const mongod = await MongoMemoryServer.create({
      instance: {
        port: 27017,
        dbPath: dbPath,
        storageEngine: 'wiredTiger',
      },
    });

    console.log(`✅ Embedded MongoDB is running at: ${mongod.getUri()}`);
    console.log(`📁 Persistent storage path: ${dbPath}`);

    const cleanup = async () => {
      console.log('\n🛑 Stopping MongoDB...');
      await mongod.stop();
      process.exit(0);
    };

    process.on('SIGINT', cleanup);
    process.on('SIGTERM', cleanup);
  } catch (err) {
    if (err.message && err.message.includes('Port 27017 already in use')) {
      console.log('ℹ️ MongoDB is already running on port 27017.');
      return;
    }
    console.error('Failed to start MongoDB:', err);
    process.exit(1);
  }
}

if (require.main === module) {
  startMongo();
}

module.exports = startMongo;
