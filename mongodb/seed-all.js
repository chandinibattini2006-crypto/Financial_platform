import { MongoClient } from 'mongodb';
import bcrypt from 'bcryptjs';
import dotenv from 'dotenv';
import path from 'path';
import { fileURLToPath } from 'url';
import { spawn } from 'child_process';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

dotenv.config({ path: path.join(__dirname, '..', '.env') });

const seedFiles = [
  'admins.js',
  'users.js',
  'advisors.js',
  'bank_accounts.js',
  'blogs.js',
  'cards.js',
  'emis.js',
  'expenses.js',
  'financial_goals.js',
  'fixed_deposits.js',
  'insurances.js',
  'investments.js',
  'loans.js',
  'mutual_funds.js',
  'people.js',
  'precious_holdings.js',
  'properties.js',
  'stocks.js',
  'transactions.js',
  'users_advisors.js'
];

async function runSeedFiles() {
  console.log('🌱 Starting MongoDB seed process...\n');
  
  for (const file of seedFiles) {
    console.log(`▶️  Running ${file}...`);
    
    await new Promise((resolve, reject) => {
      const child = spawn('node', [path.join(__dirname, file)], {
        cwd: __dirname,
        stdio: 'inherit'
      });
      
      child.on('close', (code) => {
        if (code !== 0) {
          console.warn(`⚠️  ${file} exited with code ${code}\n`);
        } else {
          console.log(`✅ ${file} completed successfully\n`);
        }
        resolve();
      });
      
      child.on('error', (err) => {
        console.error(`❌ Error running ${file}:`, err.message);
        resolve(); // Continue with next file
      });
    });
  }
  
  console.log('🎉 All seed files completed!');
  console.log('\n📊 Database populated with sample data:');
  console.log('   - Admins');
  console.log('   - Users');
  console.log('   - Advisors');
  console.log('   - Bank Accounts');
  console.log('   - Blogs');
  console.log('   - Cards');
  console.log('   - EMIs');
  console.log('   - Expenses');
  console.log('   - Financial Goals');
  console.log('   - Fixed Deposits');
  console.log('   - Insurances');
  console.log('   - Investments');
  console.log('   - Loans');
  console.log('   - Mutual Funds');
  console.log('   - People');
  console.log('   - Precious Holdings');
  console.log('   - Properties');
  console.log('   - Stocks');
  console.log('   - Transactions');
  console.log('   - User-Advisor Associations\n');
}

runSeedFiles().catch(console.error);
