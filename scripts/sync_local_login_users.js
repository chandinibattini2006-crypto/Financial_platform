const mongoose = require('mongoose');
const bcrypt = require('bcryptjs');
const Person = require('../src/models/people.model');

const users = [
  { name: 'Ahmed Zulqar', email: 'ahmed.z23@iiits.in', password: 'user_ahmed', role: 'user', pan: 'LCLUSR0001A' },
  { name: 'Krishna Govind', email: 'krishna.g23@iiits.in', password: 'user_krishna', role: 'user', pan: 'LCLUSR0002B' },
  { name: 'Ragamaie N', email: 'ragamaie.n23@iiits.in', password: 'user_ragamaie', role: 'user', pan: 'LCLUSR0003C' },
  { name: 'Deepthi M', email: 'deepthi.m23@iiits.in', password: 'user_deepthi', role: 'user', pan: 'LCLUSR0004D' },
  { name: 'Abhinay M', email: 'abhinay.m23@iiits.in', password: 'user_abhinay', role: 'user', pan: 'LCLUSR0005E' },
  { name: 'XD Phantom', email: 'xdphantom1202@gmail.com', password: 'advisor_xd', role: 'advisor', pan: 'LCLADV0001A' },
  { name: 'Zulqar Ahmed', email: 'zulqar.ahmed.12@gmail.com', password: 'advisor_zulqar', role: 'advisor', pan: 'LCLADV0002B' }
];

(async () => {
  await mongoose.connect('mongodb://localhost:27017/', { dbName: 'fdfed' });
  for (const user of users) {
    const hash = await bcrypt.hash(user.password, 10);
    await Person.findOneAndUpdate(
      { email: user.email },
      {
        $set: {
          name: user.name,
          email: user.email,
          password: hash,
          role: user.role,
          pan: user.pan,
          status: 'Active',
          isApproved: true,
          isRejected: false
        }
      },
      { upsert: true, new: true, setDefaultsOnInsert: true }
    );
    console.log('upserted', user.email, user.role);
  }
  await mongoose.disconnect();
  console.log('sync complete');
})().catch(async (err) => {
  console.error(err);
  process.exit(1);
});
