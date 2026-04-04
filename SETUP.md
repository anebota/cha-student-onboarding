# Cloud Heroes Africa - Complete Setup Guide

## MERN Stack Application Setup

This guide will walk you through setting up and running the Cloud Heroes Africa platform on your local machine.

---

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Node.js** (v18 or higher) - [Download](https://nodejs.org/)
- **npm** (comes with Node.js)
- **MongoDB Atlas Account** - [Sign up free](https://www.mongodb.com/cloud/atlas)
- **Git** (optional)

---

## 🚀 Quick Start (10 Minutes)

### Step 1: Install Backend Dependencies

Open your terminal and navigate to the backend directory:

```bash
cd backend
npm install
```

**What this does:** Installs all Node.js packages including Express, MongoDB, Passport, Stripe, PayPal, Socket.io, and Nodemailer.

**Expected output:** You'll see packages being downloaded and installed.

---

### Step 2: Configure Backend Environment Variables

Copy the environment template:

```bash
cp .env.example .env
```

**For Windows Command Prompt:**
```bash
copy .env.example .env
```

**Edit the `.env` file** with your actual credentials:

```bash
# Use any text editor
notepad .env
# or
nano .env
# or
code .env
```

**Minimum required configuration to start:**

```env
# MongoDB Atlas (REQUIRED)
MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/cloudheroes?retryWrites=true&w=majority

# JWT Secrets (REQUIRED)
JWT_SECRET=your-super-secret-jwt-key-change-in-production
JWT_REFRESH_SECRET=your-refresh-token-secret-key

# Session Secret (REQUIRED)
SESSION_SECRET=your-session-secret-key

# Frontend URL (REQUIRED)
FRONTEND_URL=http://localhost:5173
```

**Generate secure secrets:**
```bash
node -e "console.log(require('crypto').randomBytes(32).toString('hex'))"
```

Run this command 3 times to generate 3 different secrets for JWT_SECRET, JWT_REFRESH_SECRET, and SESSION_SECRET.

---

### Step 3: Start the Backend Server

```bash
npm run dev
```

**Expected output:**
```
🚀 Server running on port 5000
📡 Environment: development
🌐 API URL: http://localhost:5000
✅ MongoDB Connected: cluster0.mongodb.net
✅ Email service ready
```

**Keep this terminal open!** The backend server is now running.

---

### Step 4: Install Frontend Dependencies

Open a **NEW terminal window** (keep the backend running) and navigate to the frontend directory:

```bash
cd frontend
npm install
```

**What this does:** Installs React, Vite, Tailwind CSS, React Router, Axios, and Socket.io-client.

---

### Step 5: Configure Frontend Environment Variables

Copy the environment template:

```bash
cp .env.example .env
```

**For Windows:**
```bash
copy .env.example .env
```

**Edit the `.env` file:**

```env
VITE_API_URL=http://localhost:5000
VITE_SOCKET_URL=http://localhost:5000
VITE_GOOGLE_AUTH_URL=http://localhost:5000/api/auth/google
VITE_AZURE_AUTH_URL=http://localhost:5000/api/auth/azure
```

---

### Step 6: Start the Frontend Development Server

```bash
npm run dev
```

**Expected output:**
```
  VITE v5.0.8  ready in 500 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
  ➜  press h to show help
```

---

### Step 7: Open in Browser

Open your web browser and navigate to:

```
http://localhost:5173
```

**🎉 You should see the Cloud Heroes Africa homepage!**

---

## 🔧 Detailed Configuration

### MongoDB Atlas Setup (REQUIRED)

1. **Create MongoDB Atlas Account:**
   - Go to: https://www.mongodb.com/cloud/atlas
   - Click "Try Free"
   - Sign up with Google or email

2. **Create a Cluster:**
   - Choose "FREE" tier (M0 Sandbox)
   - Select a cloud provider (AWS recommended)
   - Choose a region close to you
   - Click "Create Cluster"

3. **Create Database User:**
   - Go to "Database Access"
   - Click "Add New Database User"
   - Choose "Password" authentication
   - Username: `cloudheroes`
   - Password: Generate a secure password
   - User Privileges: "Read and write to any database"
   - Click "Add User"

4. **Whitelist Your IP Address:**
   - Go to "Network Access"
   - Click "Add IP Address"
   - Click "Allow Access from Anywhere" (for development)
   - Click "Confirm"

5. **Get Connection String:**
   - Go to "Database" → "Connect"
   - Choose "Connect your application"
   - Copy the connection string
   - Replace `<password>` with your database user password
   - Replace `<dbname>` with `cloudheroes`

**Example:**
```
mongodb+srv://cloudheroes:YourPassword123@cluster0.abc123.mongodb.net/cloudheroes?retryWrites=true&w=majority
```

Paste this into your `backend/.env` file as `MONGODB_URI`.

---

### Google OAuth Setup (For Students & Donors)

1. **Go to Google Cloud Console:**
   - Visit: https://console.cloud.google.com/

2. **Create a New Project:**
   - Click "Select a project" → "New Project"
   - Name: "Cloud Heroes Africa"
   - Click "Create"

3. **Enable Google+ API:**
   - Navigate to "APIs & Services" → "Library"
   - Search for "Google+ API"
   - Click "Enable"

4. **Create OAuth Credentials:**
   - Go to "APIs & Services" → "Credentials"
   - Click "Create Credentials" → "OAuth client ID"
   - Configure consent screen if prompted
   - Application type: "Web application"
   - Name: "Cloud Heroes Africa Web"
   - Authorized JavaScript origins: `http://localhost:5173`
   - Authorized redirect URIs: `http://localhost:5000/api/auth/google/callback`
   - Click "Create"

5. **Copy Credentials to `.env`:**
   ```env
   GOOGLE_CLIENT_ID=your_client_id_here.apps.googleusercontent.com
   GOOGLE_CLIENT_SECRET=your_client_secret_here
   GOOGLE_CALLBACK_URL=http://localhost:5000/api/auth/google/callback
   ```

6. **Restart backend server** (Ctrl+C then `npm run dev`)

---

### Microsoft Entra ID Setup (For Administrators & Volunteers)

1. **Go to Azure Portal:**
   - Visit: https://portal.azure.com/

2. **Navigate to Azure Active Directory:**
   - Search for "Azure Active Directory"

3. **Register an Application:**
   - Click "App registrations" → "New registration"
   - Name: "Cloud Heroes Africa"
   - Supported account types: "Accounts in this organizational directory only"
   - Redirect URI: 
     - Platform: "Web"
     - URI: `http://localhost:5000/api/auth/azure/callback`
   - Click "Register"

4. **Create Client Secret:**
   - Go to "Certificates & secrets"
   - Click "New client secret"
   - Description: "Cloud Heroes Africa Secret"
   - Expires: Choose duration (6 months recommended)
   - Click "Add"
   - **Copy the secret value immediately** (you won't see it again!)

5. **Copy Credentials to `.env`:**
   ```env
   AZURE_CLIENT_ID=your_application_id_here
   AZURE_TENANT_ID=your_tenant_id_here
   AZURE_CLIENT_SECRET=your_client_secret_here
   AZURE_CALLBACK_URL=http://localhost:5000/api/auth/azure/callback
   ```

6. **Restart backend server**

---

### Stripe Payment Gateway Setup

1. **Create Stripe Account:**
   - Visit: https://stripe.com/
   - Click "Sign up"

2. **Get API Keys:**
   - Go to Dashboard → Developers → API keys
   - Copy "Publishable key" (starts with `pk_test_`)
   - Copy "Secret key" (starts with `sk_test_`)

3. **Add to Environment Files:**

**Backend `.env`:**
```env
STRIPE_SECRET_KEY=sk_test_your_secret_key_here
STRIPE_PUBLISHABLE_KEY=pk_test_your_publishable_key_here
```

**Frontend `.env`:**
```env
VITE_STRIPE_PUBLISHABLE_KEY=pk_test_your_publishable_key_here
```

4. **Restart both servers**

---

### PayPal Payment Gateway Setup

1. **Create PayPal Developer Account:**
   - Visit: https://developer.paypal.com/
   - Sign up or log in

2. **Create App:**
   - Go to "My Apps & Credentials"
   - Click "Create App"
   - App Name: "Cloud Heroes Africa"
   - App Type: "Merchant"
   - Click "Create App"

3. **Get Credentials:**
   - Copy "Client ID"
   - Copy "Secret"

4. **Add to Backend `.env`:**
```env
PAYPAL_MODE=sandbox
PAYPAL_CLIENT_ID=your_client_id_here
PAYPAL_CLIENT_SECRET=your_secret_here
```

5. **Restart backend server**

---

### MTN Mobile Money Setup (Cameroon)

1. **Register for MTN MoMo API:**
   - Visit: https://momodeveloper.mtn.com/
   - Sign up for developer account

2. **Subscribe to Collections API:**
   - Go to Products → Collections
   - Subscribe to the API

3. **Get Credentials:**
   - Primary Key (Subscription Key)
   - API User ID
   - API Key

4. **Add to Backend `.env`:**
```env
MTN_MOMO_API_KEY=your_api_user_id
MTN_MOMO_API_SECRET=your_api_key
MTN_MOMO_SUBSCRIPTION_KEY=your_subscription_key
MTN_MOMO_ENVIRONMENT=sandbox
MTN_MOMO_CALLBACK_URL=http://localhost:5000/api/payments/mtn/callback
```

5. **Restart backend server**

---

### Orange Money Setup (Cameroon)

1. **Register for Orange Money API:**
   - Visit: https://developer.orange.com/
   - Sign up for developer account

2. **Create Application:**
   - Go to "My Apps" → "Create New App"
   - Subscribe to Orange Money API

3. **Get Credentials:**
   - Client ID
   - Client Secret
   - Merchant ID

4. **Add to Backend `.env`:**
```env
ORANGE_MONEY_API_KEY=your_client_id
ORANGE_MONEY_API_SECRET=your_client_secret
ORANGE_MONEY_MERCHANT_ID=your_merchant_id
ORANGE_MONEY_ENVIRONMENT=sandbox
ORANGE_MONEY_CALLBACK_URL=http://localhost:5000/api/payments/orange/callback
```

5. **Restart backend server**

---

### Gmail App Password Setup (Email Service)

1. **Enable 2-Step Verification:**
   - Go to: https://myaccount.google.com/security
   - Enable "2-Step Verification"

2. **Generate App Password:**
   - Go to: https://myaccount.google.com/apppasswords
   - Select app: "Mail"
   - Select device: "Other (Custom name)"
   - Name: "Cloud Heroes Africa"
   - Click "Generate"
   - Copy the 16-character password

3. **Add to Backend `.env`:**
```env
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=your-email@gmail.com
EMAIL_PASSWORD=your-16-char-app-password
EMAIL_FROM=Cloud Heroes Africa <noreply@cloudheroes.africa>
```

4. **Restart backend server**

---

## 🧪 Testing the Application

### Test Without OAuth (Demo Mode)

You can test the application without setting up OAuth by directly accessing dashboards:

**Add this temporary route to `backend/src/routes/auth.routes.js`:**

```javascript
// TEMPORARY TEST ROUTE - REMOVE IN PRODUCTION
router.get('/test-login/:role', async (req, res) => {
  const { role } = req.params;
  
  // Create or find test user
  let user = await User.findOne({ email: `test-${role}@test.com` });
  
  if (!user) {
    user = await User.create({
      name: `Test ${role.charAt(0).toUpperCase() + role.slice(1)}`,
      email: `test-${role}@test.com`,
      role: role,
      provider: 'local',
      isVerified: true
    });
  }
  
  const token = generateToken(user._id, user.role);
  
  res.cookie('token', token, {
    httpOnly: true,
    maxAge: 7 * 24 * 60 * 60 * 1000
  });
  
  res.redirect(`${process.env.FRONTEND_URL}/auth/callback?token=${token}&role=${role}`);
});
```

**Then access:**
- Student: `http://localhost:5000/api/auth/test-login/student`
- Administrator: `http://localhost:5000/api/auth/test-login/administrator`
- Donor: `http://localhost:5000/api/auth/test-login/donor`
- Volunteer: `http://localhost:5000/api/auth/test-login/volunteer`

---

### Test Community Pages (No Login Required)

- Homepage: `http://localhost:5173/`
- Community: `http://localhost:5173/community`
- Forum: `http://localhost:5173/community/forum`
- Resources: `http://localhost:5173/community/resources`
- Impact: `http://localhost:5173/community/impact`

---

## 📁 Project Structure

```
cloud-heroes-africa/
├── backend/                          # Node.js + Express API
│   ├── src/
│   │   ├── config/                   # Database, JWT configs
│   │   ├── models/                   # MongoDB schemas
│   │   ├── routes/                   # API endpoints
│   │   ├── middleware/               # Auth, RBAC, validation
│   │   ├── services/
│   │   │   ├── payment/              # Stripe, PayPal, MTN, Orange
│   │   │   ├── email/                # Nodemailer
│   │   │   ├── auth/                 # OAuth providers
│   │   │   └── socket/               # Socket.io handlers
│   │   └── server.js                 # Entry point
│   ├── package.json
│   └── .env
│
├── frontend/                         # React + Vite + Tailwind
│   ├── src/
│   │   ├── components/               # Reusable components
│   │   ├── pages/                    # Page components
│   │   ├── context/                  # React Context (Auth, Socket)
│   │   ├── services/                 # API calls (Axios)
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   ├── vite.config.js
│   ├── tailwind.config.js
│   └── .env
│
├── infrastructure/                   # Your existing IaC
├── config/                           # Your existing policies
├── docs/                             # Your existing documentation
├── scripts/                          # Your existing scripts
├── SETUP.md                          # This file
├── TECH_STACK.md                     # Technical documentation
└── README.md                         # Project overview
```

---

## 🔌 API Endpoints

### Authentication
- `GET /api/auth/google` - Initiate Google OAuth
- `GET /api/auth/google/callback` - Google OAuth callback
- `GET /api/auth/azure` - Initiate Azure AD OAuth
- `POST /api/auth/azure/callback` - Azure AD callback
- `GET /api/auth/me` - Get current user
- `POST /api/auth/logout` - Logout

### Payments
- `POST /api/payments/stripe/create-checkout` - Create Stripe session
- `GET /api/payments/stripe/verify/:sessionId` - Verify Stripe payment
- `POST /api/payments/paypal/create` - Create PayPal payment
- `POST /api/payments/paypal/execute` - Execute PayPal payment
- `POST /api/payments/mtn/request` - Request MTN MoMo payment
- `GET /api/payments/mtn/status/:referenceId` - Check MTN status
- `POST /api/payments/orange/initiate` - Initiate Orange Money
- `GET /api/payments/orange/status/:orderId` - Check Orange status

### Role-Specific
- `GET /api/student/dashboard` - Student dashboard data
- `GET /api/admin/dashboard` - Admin dashboard data
- `GET /api/donor/dashboard` - Donor dashboard data
- `GET /api/volunteer/dashboard` - Volunteer dashboard data

### Community
- `GET /api/community/stats` - Community statistics
- `GET /api/community/forum` - Forum posts

---

## 🐛 Troubleshooting

### Backend Issues

**Issue: `Cannot find module 'express'`**
```bash
cd backend
npm install
```

**Issue: `MongooseError: The uri parameter to openUri() must be a string`**
- Check your `MONGODB_URI` in `backend/.env`
- Ensure you replaced `<password>` with your actual password
- Ensure you replaced `<dbname>` with `cloudheroes`

**Issue: `Port 5000 already in use`**
```bash
# Find and kill the process using port 5000
# Windows:
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Mac/Linux:
lsof -ti:5000 | xargs kill -9
```

**Issue: `JWT_SECRET is not defined`**
- Make sure you created `backend/.env` from `.env.example`
- Add all required environment variables

---

### Frontend Issues

**Issue: `Cannot find module 'react'`**
```bash
cd frontend
npm install
```

**Issue: `Failed to fetch`**
- Ensure backend is running on port 5000
- Check `VITE_API_URL` in `frontend/.env`
- Check browser console for CORS errors

**Issue: `Vite port 5173 already in use`**
- Change port in `frontend/vite.config.js`:
```javascript
server: {
  port: 5174  // Use different port
}
```

---

### OAuth Issues

**Issue: `redirect_uri_mismatch`**
- Ensure redirect URIs in Google/Azure console match exactly
- Use `http://localhost:5000` (not `127.0.0.1`)
- Check for trailing slashes

**Issue: `invalid_client`**
- Double-check Client ID and Client Secret
- Ensure no extra spaces when copying
- Restart backend server after changing credentials

---

## 🚀 Production Deployment

### Environment Variables for Production

**Backend:**
```env
NODE_ENV=production
PORT=5000
MONGODB_URI=mongodb+srv://production-user:password@cluster.mongodb.net/cloudheroes
FRONTEND_URL=https://yourdomain.com
JWT_SECRET=<strong-random-secret>
# ... all other production credentials
```

**Frontend:**
```env
VITE_API_URL=https://api.yourdomain.com
VITE_SOCKET_URL=https://api.yourdomain.com
```

### Build Frontend for Production

```bash
cd frontend
npm run build
```

This creates a `dist/` folder with optimized production files.

### Run Backend in Production

```bash
cd backend
npm start
```

Or use PM2 for process management:
```bash
npm install -g pm2
pm2 start src/server.js --name cloud-heroes-backend
```

---

## 📊 Real-time Features (Socket.io)

The application includes real-time features:

- **Live notifications** for all users
- **Forum messages** broadcast in real-time
- **Donation alerts** for administrators
- **Student progress updates** for volunteers
- **Online user presence** tracking

Socket.io automatically connects when users log in.

---

## 🔒 Security Best Practices

### Development
- ✅ Using environment variables for secrets
- ✅ JWT token authentication
- ✅ CORS configured
- ✅ Rate limiting enabled
- ⚠️ Debug mode enabled (disable in production)

### Production Checklist
- [ ] Set `NODE_ENV=production`
- [ ] Use strong JWT secrets (32+ characters)
- [ ] Enable HTTPS/TLS
- [ ] Configure proper CORS origins
- [ ] Set secure cookie flags
- [ ] Enable rate limiting
- [ ] Regular security audits
- [ ] Keep dependencies updated

---

## 📝 Testing Checklist

### Basic Functionality
- [ ] Homepage loads at `http://localhost:5173`
- [ ] Login page loads
- [ ] Community pages load (no auth required)
- [ ] Backend API responds at `http://localhost:5000`

### Authentication (With OAuth Setup)
- [ ] Google login redirects correctly
- [ ] Azure login redirects correctly
- [ ] User session persists after login
- [ ] Logout clears session
- [ ] Protected routes redirect to login

### Role-Specific Dashboards
- [ ] Student dashboard displays correctly
- [ ] Administrator dashboard displays correctly
- [ ] Donor dashboard displays correctly
- [ ] Volunteer dashboard displays correctly

### Real-time Features
- [ ] Socket.io connects successfully
- [ ] Real-time notifications work
- [ ] User presence updates

---

## 🎯 Next Steps

### Immediate
1. ✅ Set up MongoDB Atlas
2. ✅ Configure environment variables
3. ✅ Run backend and frontend
4. ✅ Test in browser

### Short Term
1. [ ] Set up Google OAuth
2. [ ] Set up Microsoft Entra ID
3. [ ] Configure payment gateways
4. [ ] Set up email service
5. [ ] Test all authentication flows

### Medium Term
1. [ ] Implement user registration
2. [ ] Add course management
3. [ ] Build donation flow UI
4. [ ] Implement MFA enforcement
5. [ ] Add audit logging UI

### Long Term
1. [ ] Deploy to production
2. [ ] Set up CI/CD pipeline
3. [ ] Configure monitoring
4. [ ] Implement backup strategy
5. [ ] Load testing

---

## 📚 Additional Resources

### Documentation
- **Technical Stack:** See `TECH_STACK.md`
- **Project Overview:** See `README.md`
- **Backend README:** See `backend/README.md`
- **Frontend README:** See `frontend/README.md`

### Learning Resources
- **Node.js:** https://nodejs.org/docs
- **Express:** https://expressjs.com/
- **MongoDB:** https://docs.mongodb.com/
- **React:** https://react.dev/
- **Vite:** https://vitejs.dev/
- **Tailwind CSS:** https://tailwindcss.com/docs

### API Documentation
- **Stripe:** https://stripe.com/docs/api
- **PayPal:** https://developer.paypal.com/docs/api
- **MTN MoMo:** https://momodeveloper.mtn.com/
- **Orange Money:** https://developer.orange.com/
- **Socket.io:** https://socket.io/docs/

---

## 🆘 Getting Help

### Common Commands

```bash
# Backend
cd backend
npm install              # Install dependencies
npm run dev             # Start development server
npm start               # Start production server

# Frontend
cd frontend
npm install              # Install dependencies
npm run dev             # Start development server
npm run build           # Build for production
npm run preview         # Preview production build

# Generate secrets
node -e "console.log(require('crypto').randomBytes(32).toString('hex'))"

# Check Node version
node --version

# Check npm version
npm --version
```

---

## ✅ Success Criteria

You've successfully set up the application when:

1. ✅ Backend server runs without errors
2. ✅ Frontend loads in browser
3. ✅ MongoDB connection is established
4. ✅ You can navigate between pages
5. ✅ Community pages display correctly
6. ✅ (Optional) OAuth login works
7. ✅ (Optional) Payment gateways configured

---

## 🎉 Congratulations!

If you can see the Cloud Heroes Africa platform in your browser, you've successfully set up a full-stack MERN application with:

- ✅ Node.js + Express backend
- ✅ MongoDB database
- ✅ React + Vite + Tailwind CSS frontend
- ✅ JWT authentication
- ✅ Socket.io real-time features
- ✅ Payment gateway integrations
- ✅ Email service
- ✅ OAuth providers

**You're ready to start developing!** 🚀

---

**Version:** 1.0.0  
**Last Updated:** 2024  
**Tech Stack:** MERN (MongoDB, Express, React, Node.js)  
**Maintained By:** Cloud Heroes Africa Development Team
