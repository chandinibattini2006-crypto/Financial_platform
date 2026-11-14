# FINANCIAL PLANNING PLATFORM - Project Structure Guide 📚

Welcome to the FINANCIAL PLANNING PLATFORM project! This guide will help you understand our folder structure and where to put your code.

---

## 📁 Project Structure Overview

```
FINANCIAL PLANNING PLATFORM/
├── src/
│   ├── config/          # App settings & configuration
│   ├── models/          # Database schemas
│   ├── controllers/     # Business logic
│   ├── routes/          # API endpoints (URLs)
│   ├── middlewares/     # Pre-processing & validation
│   ├── services/        # External API integrations
│   ├── utils/           # Helper functions
│   ├── components/      # Frontend React components
│   └── styles/          # Frontend CSS files
├── public/              # Static assets
├── server.js            # Main server entry point
└── package.json
```

---

## 🎯 Quick Guide - Where Does My Code Go?

| What are you doing? | Folder | Example |
|---------------------|--------|---------|
| Creating a URL endpoint | `routes/` | `/api/users/register` |
| Checking auth before request | `middlewares/` | Verify JWT token |
| Main business logic | `controllers/` | Create user, process order |
| Database structure | `models/` | User schema, Product schema |
| Sending emails/SMS | `services/` | Nodemailer, Twilio |
| App settings | `config/` | Database URL, JWT secret |
| Helper functions | `utils/` | Format date, validate email |

---

## 📂 Detailed Folder Breakdown

### 1️⃣ **config/** - Application Settings

**What it does:** Stores all configuration and settings for the app

**Put here:**
- Database connection setup
- Environment variables (API keys, secrets)
- App constants (user roles, status codes)
- Third-party service configurations

**Example files:**
- `database.js` - MongoDB connection
- `environment.js` - Port, JWT secret, API keys
- `constants.js` - Fixed values like USER_ROLES

**✅ DO:**
```javascript
// config/constants.js
const USER_ROLES = {
  ADMIN: 'admin',
  USER: 'user',
  MODERATOR: 'moderator'
};
```

**❌ DON'T:**
- Don't put business logic here
- Don't put API endpoints here

---

### 2️⃣ **models/** - Database Structure

**What it does:** Defines what your data looks like in the database

**Put here:**
- Mongoose schemas
- Field definitions (name, email, password)
- Validation rules
- Database indexes
- Schema methods

**Example files:**
- `User.js` - User schema
- `Product.js` - Product schema
- `Order.js` - Order schema

**✅ DO:**
```javascript
// models/User.js
const userSchema = new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, required: true, unique: true },
  password: { type: String, required: true }
});
```

**❌ DON'T:**
- Don't put business logic here
- Don't handle HTTP requests here

---

### 3️⃣ **controllers/** - Business Logic

**What it does:** Contains the main logic - what happens when someone makes a request

**Put here:**
- Functions that handle requests
- Database operations (CRUD)
- Data processing and validation
- Response formatting
- Calling models and services

**Example files:**
- `userController.js` - User operations
- `productController.js` - Product operations
- `orderController.js` - Order operations

**✅ DO:**
```javascript
// controllers/userController.js
async function createUser(req, res) {
  // 1. Get data from request
  const { name, email, password } = req.body;
  
  // 2. Process data
  const hashedPassword = await bcrypt.hash(password, 10);
  
  // 3. Save to database
  const user = await User.create({ name, email, password: hashedPassword });
  
  // 4. Call external service if needed
  await emailService.sendWelcomeEmail(user.email);
  
  // 5. Send response
  res.status(201).json({ success: true, user });
}
```

**❌ DON'T:**
- Don't define routes here (that's for routes/)
- Don't define database schemas here (that's for models/)

---

### 4️⃣ **routes/** - API Endpoints

**What it does:** Defines the URLs people can visit

**Put here:**
- Express router definitions
- HTTP methods (GET, POST, PUT, DELETE)
- URL paths
- Middleware assignments
- Controller connections

**Example files:**
- `userRoutes.js` - User endpoints
- `productRoutes.js` - Product endpoints
- `index.js` - Combine all routes

**✅ DO:**
```javascript
// routes/userRoutes.js
const router = express.Router();
const userController = require('../controllers/userController');
const { authenticate } = require('../middlewares/auth');

router.post('/register', userController.register);
router.get('/profile', authenticate, userController.getProfile);
router.put('/profile', authenticate, userController.updateProfile);
```

**❌ DON'T:**
- Don't put business logic here
- Don't write controller code here
- Keep routes clean - just URLs and connections

---

### 5️⃣ **middlewares/** - Pre-checks and Validation

**What it does:** Checks things BEFORE your controller runs

**Put here:**
- Authentication checks (is user logged in?)
- Authorization checks (does user have permission?)
- Input validation
- Request logging
- Error handling
- File upload processing

**Example files:**
- `auth.js` - Authentication middleware
- `validation.js` - Input validation
- `errorHandler.js` - Error handling
- `logger.js` - Request logging

**✅ DO:**
```javascript
// middlewares/auth.js
function authenticate(req, res, next) {
  const token = req.headers.authorization;
  
  if (!token) {
    return res.status(401).json({ error: "No token" });
  }
  
  // Verify token...
  next(); // Continue to controller
}
```

**❌ DON'T:**
- Don't put main business logic here
- Don't create/update database records here

---

### 6️⃣ **services/** - External API Calls

**What it does:** Handles all communication with external services

**Put here:**
- Email sending (Nodemailer, SendGrid)
- Payment processing (Stripe, Razorpay)
- SMS services (Twilio)
- Cloud storage (AWS S3, Cloudinary)
- Push notifications
- Social media APIs
- Any third-party integrations

**Example files:**
- `emailService.js` - Email operations
- `paymentService.js` - Payment processing
- `smsService.js` - SMS sending
- `cloudinaryService.js` - Image uploads

**✅ DO:**
```javascript
// services/emailService.js
async function sendWelcomeEmail(email, name) {
  await nodemailer.sendMail({
    to: email,
    subject: 'Welcome!',
    html: `<h1>Welcome ${name}!</h1>`
  });
}
```

**❌ DON'T:**
- Don't put internal app logic here
- Don't handle database operations here

---

### 7️⃣ **utils/** - Helper Functions

**What it does:** Small reusable functions used throughout the app

**Put here:**
- Data formatting (dates, currency)
- String manipulation
- Custom validation functions
- Response standardization
- Token generators
- Common calculations

**Example files:**
- `helpers.js` - General helpers
- `validators.js` - Validation functions
- `responseHandler.js` - Standard responses

**✅ DO:**
```javascript
// utils/helpers.js
function formatDate(date) {
  return new Date(date).toLocaleDateString();
}

function generateRandomCode() {
  return Math.random().toString(36).substring(7);
}
```

**❌ DON'T:**
- Don't put business logic here
- Don't handle HTTP requests here

---

## 🔄 Request Flow Example

**User registers:** `POST /api/users/register`

```
1. routes/userRoutes.js
   → Receives request at /register
   
2. middlewares/validation.js
   → Validates email, password
   → If invalid: stops here, returns error
   → If valid: continues...
   
3. controllers/userController.js
   → Checks if user exists
   → Hashes password
   → Creates user in database (uses Model)
   → Calls emailService
   → Sends response
   
4. models/User.js
   → Defines user structure
   → Saves to MongoDB
   
5. services/emailService.js
   → Sends welcome email via Nodemailer
   
6. User receives response
```

---

## 🎨 Frontend Structure

### **components/** - React Components

**Put here:**
- All React components
- Organized by feature (user/, product/, common/)
- Reusable UI components

**Example structure:**
```
components/
├── common/
│   ├── Header.jsx
│   ├── Footer.jsx
│   └── Button.jsx
├── user/
│   ├── UserProfile.jsx
│   └── UserList.jsx
└── product/
    ├── ProductCard.jsx
    └── ProductList.jsx
```

### **styles/** - CSS Files

**Put here:**
- All CSS and styling files
- Global styles
- Component-specific styles

---

## 🚀 Getting Started

### For New Features:

1. **Create a Model** (if you need new data structure)
   - Define schema in `models/YourModel.js`

2. **Create a Controller**
   - Add business logic in `controllers/yourController.js`

3. **Create Routes**
   - Define endpoints in `routes/yourRoutes.js`

4. **Add Middleware** (if needed)
   - Validation or auth in `middlewares/`

5. **Add Service** (if using external APIs)
   - External calls in `services/yourService.js`

---

## ✅ Best Practices

### DO:
- ✅ Keep routes simple - only URL definitions
- ✅ Put all logic in controllers
- ✅ Use services for external APIs
- ✅ Add validation in middlewares
- ✅ Use meaningful file names
- ✅ Write comments for complex logic
- ✅ Handle errors properly

### DON'T:
- ❌ Don't mix concerns (logic in routes, URLs in controllers)
- ❌ Don't repeat code (use utils/)
- ❌ Don't hardcode values (use config/)
- ❌ Don't skip error handling
- ❌ Don't commit sensitive data (.env files)

---

## 🆘 Common Questions

**Q: Where do I put password hashing?**
A: In the controller, before saving to database

**Q: Where do I check if user is logged in?**
A: In middleware (auth.js)

**Q: Where do I send emails?**
A: In services (emailService.js)

**Q: Where do I define user schema?**
A: In models (User.js)

**Q: Where do I define the /register URL?**
A: In routes (userRoutes.js)

**Q: Where do I format dates?**
A: In utils (helpers.js)

---

## 📞 Need Help?

- Check this README first
- Look at existing code examples in the same folder
- Ask team members in group chat
- Review the code flow diagram above

---

## 🔑 Simple Rule to Remember

**"Is it talking to something OUTSIDE the database?"**
- ✅ YES → `services/`
- ❌ NO → `controllers/`

**"Is it a URL?"**
- ✅ YES → `routes/`

**"Is it checking something BEFORE main logic?"**
- ✅ YES → `middlewares/`

**"Is it database structure?"**
- ✅ YES → `models/`

---

Happy Coding! 🚀