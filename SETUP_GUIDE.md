# 🚀 FINANCIAL PLANNING PLATFORM - Complete Setup Guide

## ✅ Prerequisites Installed
- ✅ Node.js & npm
- ✅ MongoDB (running on localhost:27017)
- ✅ All npm dependencies

---

## 📋 Configuration Steps

### 1. **Database Setup** ✅ (Already Done)
```bash
# MongoDB is running on port 27017
# Database name: fdfed
# Collections have been seeded with sample data
node mongodb/seed-all.js  # Run this anytime to reset data
```

### 2. **JWT & Security Keys** ✅ (Configured)
**File**: `.env`
```env
JWT_SECRET=financial-planning-secret-jwt-key-2026-change-in-production
CARD_ENC_KEY=financial-planning-card-encryption-key-2026
```
⚠️ **Action for Production**: Change these to random secure keys

---

## 📧 Email Configuration (Optional but Recommended)

### Setup Gmail SMTP:
1. Go to https://myaccount.google.com/apppasswords
2. Select **Mail** and **Windows Computer** (or your device)
3. Google will generate a **16-character password**
4. Copy and update `.env`:

```env
EMAIL_USER=your-email@gmail.com
EMAIL_PASS=xxxx-xxxx-xxxx-xxxx
```

### Test Email:
```bash
# The contact form on the app will send emails using this configuration
# Check in the browser console for success/error messages
```

---

## 📊 Financial Data API (Stock Market)

### Setup Finnhub API:
1. Visit: https://finnhub.io
2. Click **Dashboard** → **Sign Up**
3. Choose **Free Plan** (60 calls/minute is plenty)
4. Copy your API key
5. Update `.env`:

```env
FINNHUB_API_KEY=your-api-key-from-finnhub
```

### Features Enabled:
- ✅ Real-time stock prices
- ✅ Stock portfolio tracking
- ✅ Investment performance analytics
- ✅ Auto-converted to INR currency

### Test Stocks Feature:
```bash
# After login, go to Investments section
# Search for stocks like: AAPL, GOOGL, MSFT, INFY, TCS
```

---

## 🤖 AI Financial Advice (Optional)

### Setup Python AI Service:
The app has fallback responses, but for full AI features:

1. Install Python 3.8+
2. Create a separate Python project with Flask/FastAPI
3. Deploy on `http://127.0.0.1:5002`
4. Update `.env`:

```env
PYTHON_AI_URL=http://127.0.0.1:5002/api/financial-advice
```

**Without Python Service**: ✓ App works perfectly with default advice templates

---

## 🔐 Authentication & User Management

### Default Admin Accounts:
```
1. Venky
   Email: venky045@gmail.com
   Password: @venky210606
   Role: Admin

2. Krishna Gupta
   Email: krishna.gpt607@gmail.com
   Password: admin_krishna
   Role: Admin

3. Ziko Ahmed
   Email: ziko120204@gmail.com
   Password: admin_ziko
   Role: Admin
```

### Test User Accounts:
```
Email: ahmed.z23@iiits.in
Password: user_ahmed

Email: krishna.g23@iiits.in
Password: user_krishna
```

---

## 🖥️ Running the Application

### Development Mode:
```bash
npm run dev
# Runs on http://localhost:3000 (Frontend)
#           http://localhost:5000 (Backend API)
```

### Backend Only:
```bash
npm run server
```

### Frontend Only:
```bash
npm run start:frontend
```

### Build for Production:
```bash
npm run build
npm run preview
```

---

## 📡 API Documentation

Access Swagger UI for all API endpoints:
```
http://localhost:5000/api-docs
```

This shows:
- ✅ All available endpoints
- ✅ Request/response formats
- ✅ Authentication requirements
- ✅ Try out API calls directly

---

## 🛠️ Troubleshooting

### Port Already in Use
```bash
# Automatically handled, but if needed:
taskkill /PID <pid> /F    # Windows
kill -9 <pid>              # Mac/Linux
```

### MongoDB Not Connected
```bash
# Check MongoDB is running
# Windows: Check Services or run: mongod
# Make sure MONGO_URI in .env is correct
```

### Email Not Sending
```bash
# Check EMAIL_USER and EMAIL_PASS in .env
# Verify Gmail App Password is correct (16 characters)
# Check "Less secure app access" is not blocking
```

### Stock Prices Not Loading
```bash
# Verify FINNHUB_API_KEY in .env is set
# Without it, app shows sample/fallback prices (still works!)
# Free Finnhub account gives 60 calls/minute
```

---

## 📂 Project Structure

```
FINANCIAL_PROJECT/
├── server.js                 # Main backend server
├── src/
│   ├── controllers/          # Business logic
│   ├── routes/               # API endpoints
│   ├── models/               # MongoDB schemas
│   ├── middlewares/          # Auth, logging, etc
│   ├── config/               # Configuration files
│   └── utils/                # Helper functions
├── mongodb/                  # Database seed scripts
│   └── seed-all.js          # Run to populate database
├── .env                      # Environment variables (KEEP SECRET!)
├── .env.example              # Template for .env
├── package.json              # Dependencies
└── vite.config.mjs           # Frontend config
```

---

## 🔄 Database Commands

### Seed/Reset Database:
```bash
node mongodb/seed-all.js
```

### Add More Admins:
```bash
# Edit mongodb/admins.js and run it again
node mongodb/admins.js
```

### Add Test Users:
```bash
node mongodb/users.js
```

---

## 🚀 Production Deployment

### Before Going Live:
1. ✅ Change `JWT_SECRET` to random value
2. ✅ Change `CARD_ENC_KEY` to random value
3. ✅ Set `NODE_ENV=production`
4. ✅ Use MongoDB Atlas (cloud database)
5. ✅ Enable HTTPS/SSL
6. ✅ Setup proper email service (SendGrid, AWS SES)
7. ✅ Use environment-specific configs
8. ✅ Never commit `.env` to git

---

## 📞 Support

### Useful Resources:
- MongoDB Docs: https://docs.mongodb.com
- Finnhub API: https://finnhub.io/docs/api
- Express.js: https://expressjs.com
- React: https://react.dev
- Vite: https://vitejs.dev

### Error Logs:
Check browser console (F12) and backend terminal for detailed error messages

---

## ✨ Features Enabled

With this configuration, the following features are fully operational:

- ✅ User authentication & authorization
- ✅ Admin dashboard & user management
- ✅ Advisor system & client management
- ✅ Financial tracking (income, expenses, goals)
- ✅ Investment portfolio management
- ✅ Real-time stock prices (with Finnhub)
- ✅ Email notifications
- ✅ Blog & financial content
- ✅ Account management & KYC
- ✅ Loan & EMI tracking
- ✅ Insurance management
- ✅ Bank account management
- ✅ Card management (encrypted)
- ✅ Comprehensive transaction history
- ✅ Financial analytics & reports

---

**Last Updated**: April 21, 2026
**Version**: 1.0.0
**Status**: ✅ Ready for Development & Production
