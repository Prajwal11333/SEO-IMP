# MongoDB Authentication Setup Guide

## Step 1: Install Backend Dependencies
Navigate to the backend directory and install the required packages:

```bash
cd backend/node-server/node-Server
npm install
```

This will install:
- **mongoose**: MongoDB object modeling
- **bcryptjs**: Password hashing
- **jsonwebtoken**: JWT token generation

## Step 2: Configure MongoDB Atlas

1. Create a MongoDB Atlas account at https://www.mongodb.com/cloud/atlas
2. Create a cluster (free tier available)
3. Get your connection string: `mongodb+srv://username:password@cluster.mongodb.net/database-name`

## Step 3: Update Environment Variables

Edit `backend/node-server/node-Server/.env`:

```env
PORT=3001
PYTHON_SERVICE_URL=http://localhost:8000
MONGODB_URI=mongodb+srv://YOUR_USERNAME:YOUR_PASSWORD@YOUR_CLUSTER.mongodb.net/seoz-db?retryWrites=true&w=majority
JWT_SECRET=your_secure_secret_key_here_min_32_chars
```

Replace:
- `YOUR_USERNAME` - Your MongoDB Atlas username
- `YOUR_PASSWORD` - Your MongoDB Atlas password
- `YOUR_CLUSTER` - Your cluster name

## Step 4: Start the Backend Server

```bash
cd backend/node-server/node-Server
npm start
# or for development with hot reload:
npm run dev
```

You should see: `✅ MongoDB connected successfully`

## Step 5: Test Authentication

### Register a new user:
```bash
curl -X POST http://localhost:3001/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","password":"password123"}'
```

### Login:
```bash
curl -X POST http://localhost:3001/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","password":"password123"}'
```

### Logout:
```bash
curl -X POST http://localhost:3001/api/auth/logout
```

## Frontend Features

The login component now includes:

- ✅ **Login**: Authenticate with email and password
- ✅ **Register**: Create new user accounts
- ✅ **Password Toggle**: Show/hide password
- ✅ **Error Messages**: Display validation errors
- ✅ **Loading States**: Visual feedback during authentication
- ✅ **JWT Tokens**: Stored in localStorage
- ✅ **Logout**: Clear session and tokens
- ✅ **Toggle**: Switch between login and signup modes

## Architecture

```
Frontend (React)
    ↓ (API calls)
Backend (Node.js/Express)
    ↓ (Mongoose)
MongoDB Atlas (Cloud Database)
```

## Password Security

- Passwords are hashed using bcryptjs (10 salt rounds)
- Never stored in plain text
- Each user has unique hashed password

## Token Management

- JWT tokens expire after 24 hours
- Tokens stored in browser localStorage
- Can be sent with API requests in Authorization header
