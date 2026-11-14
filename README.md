# 💎 Financial Planning & Wealth Management Platform

An intelligent, full-stack financial management ecosystem designed to empower individuals with real-time portfolio tracking, expense analytics, automated budgeting, and seamless financial advisor consultations.

[![Node.js](https://img.shields.io/badge/Node.js-v18+-green.svg)](https://nodejs.org/)
[![React](https://img.shields.io/badge/React-18-blue.svg)](https://reactjs.org/)
[![Vite](https://img.shields.io/badge/Vite-7-purple.svg)](https://vitejs.dev/)
[![MongoDB](https://img.shields.io/badge/MongoDB-Database-emerald.svg)](https://www.mongodb.com/)
[![Express](https://img.shields.io/badge/Express-Backend-black.svg)](https://expressjs.com/)
[![License](https://img.shields.io/badge/License-ISC-yellow.svg)](LICENSE)

---

## 🌟 Key Highlights

- **Multi-Role Architecture**: Dedicated portals and workflows for **Users**, **Financial Advisors**, and **Platform Administrators**.
- **Interactive 3D Visuals & Analytics**: Realistic 3D credit card visualizer powered by Three.js & Framer Motion, along with rich financial charts (Chart.js & Recharts).
- **Embedded Zero-Config Database**: Automatic fallback to an embedded MongoDB instance for seamless local setup with zero external installations required.
- **Stock & Investment Tracking**: Real-time market data monitoring, portfolio breakdown (stocks, mutual funds, precious holdings, properties, and fixed deposits).
- **Secure Authentication & RBAC**: JWT-based session security, bcrypt encryption, rate limiting, and role-guarded routes.
- **Advisor Video & Advisory Services**: Connect directly with accredited advisors, request advisory sessions, and review customized financial blueprints.
- **Interactive API Documentation**: Full Swagger UI documentation at `/api-docs`.

---

## 🚀 Architecture & Tech Stack

### Frontend
- **Framework**: React 18 with Vite
- **State Management**: Redux Toolkit & React Context API
- **Styling & UI**: TailwindCSS, Styled-Components, Lucide Icons, React Icons
- **3D & Animations**: Three.js, `@react-three/fiber`, `@react-three/drei`, GSAP, Framer Motion
- **Data Visualizations**: Recharts, Chart.js

### Backend
- **Runtime**: Node.js & Express.js
- **Database**: MongoDB with Mongoose ODM
- **Real-Time Communication**: Socket.io
- **Security & Middlewares**: JWT, BcryptJS, Morgan logger, Express Rate Limit, Multer
- **API Documentation**: Swagger (swagger-jsdoc & swagger-ui-express)

---

## 📁 System Roles & Dashboards

| Role | Access URL | Key Capabilities |
| :--- | :--- | :--- |
| **User** | `/user/dashboard` | Track spendings, credit scores, manage cards, EMIs, bank accounts, portfolio, and chat with AI advisor |
| **Advisor** | `/advisor/dashboard` | Manage assigned clients, view financial health reports, schedule consultation calls, and review portfolios |
| **Admin** | `/admin/dashboard` | Oversee user management, review advisor applications, inspect audit logs, monitor system server health |

---

## 🛠️ Quick Start Guide

### 1. Prerequisites
- [Node.js](https://nodejs.org/) (v18 or higher)
- [Git](https://git-scm.com/)

### 2. Clone the Repository
```bash
git clone https://github.com/chandinibattini2006-crypto/Financial_platform.git
cd Financial_platform
```

### 3. Install Dependencies
```bash
npm install
```

### 4. Configure Environment Variables
Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```
*(Default settings work out of the box with auto-embedded MongoDB on port `27017`)*

### 5. Seed Initial Data
Populate the database with sample records and test accounts:
```bash
npm run seed
```

### 6. Run the Application
Launch both the backend API and frontend Vite server:
```bash
npm run dev
```

- **Frontend Application**: [http://localhost:3000](http://localhost:3000)
- **Backend API**: [http://localhost:5000](http://localhost:5000)
- **Interactive Swagger Docs**: [http://localhost:5000/api-docs](http://localhost:5000/api-docs)

---

## 🔐 Default Demo Accounts

| Role | Email | Password |
| :--- | :--- | :--- |
| **User** | `chandiniuser@gmail.com` | `chandini123` |
| **Advisor** | `chandiniadviser@gmail.com` | `chandini123` |
| **Admin** | `chandiniadmin@gmail.com` | `chandini123` |

---

## 📖 API Endpoints Preview

- `POST /api/auth/login` — User authentication & JWT issuance
- `POST /api/auth/register` — User & advisor registration
- `GET /api/account-summary` — Net worth, cash flow & account aggregates
- `GET /api/spendings` — Category-wise expense tracking
- `GET /api/investments` — Stocks, mutual funds, and fixed deposits
- `GET /api/advisor/clients` — Client roster for financial advisors
- `GET /api-docs` — Interactive Swagger documentation playground

---

## 👩‍💻 Author

**Chandini**
- GitHub: [@chandinibattini2006-crypto](https://github.com/chandinibattini2006-crypto)
- Email: [chandinibattini2006@gmail.com](mailto:chandinibattini2006@gmail.com)

---

## 📄 License

This project is licensed under the [ISC License](LICENSE).
