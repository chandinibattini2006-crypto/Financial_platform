import { MongoClient } from 'mongodb';
import dotenv from 'dotenv';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
dotenv.config({ path: path.join(__dirname, '..', '.env') });

const MONGO_URI = process.env.MONGO_URI || "mongodb://localhost:27017/";

async function insertUsersAdvisors() {
  const client = new MongoClient(MONGO_URI);
  
  try {
    await client.connect();
    console.log('Connected to MongoDB');
    
    const db = client.db('fdfed');
    const peopleCollection = db.collection('people');
    
    // Get users (role: 'user')
    const users = await peopleCollection.find({ role: 'user' }).toArray();
    // Get advisors (role: 'advisor')
    const advisors = await peopleCollection.find({ role: 'advisor' }).toArray();
    
    if (users.length === 0 || advisors.length === 0) {
      console.log('⚠️  No users or advisors found. Please seed them first.');
      return;
    }
    
    // Assign advisors to users (distribute evenly)
    const updates = [];
    
    users.forEach((user, index) => {
      const advisorIndex = index % advisors.length;
      const assignedAdvisor = advisors[advisorIndex];
      
      updates.push({
        updateOne: {
          filter: { _id: user._id },
          update: {
            $set: {
              assignedAdvisor: assignedAdvisor._id
            }
          }
        }
      });
    });
    
    // Execute bulk updates
    if (updates.length > 0) {
      const result = await peopleCollection.bulkWrite(updates);
      console.log(`✅ ${result.modifiedCount} users assigned advisors successfully\n`);
      
      // Display the mappings
      console.log('User-Advisor Mappings:');
      for (let i = 0; i < users.length; i++) {
        const user = users[i];
        const advisorIndex = i % advisors.length;
        const advisor = advisors[advisorIndex];
        const spec = advisor.advisorProfile?.specialization || 'general';
        console.log(`  ${user.name} (${user.email}) → ${advisor.name} (${spec})`);
      }
    }
    
  } catch (error) {
    console.error('Error assigning advisors to users:', error);
  } finally {
    await client.close();
  }
}

insertUsersAdvisors();