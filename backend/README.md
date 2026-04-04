# Cloud Heroes Africa - Backend API

Node.js + Express + MongoDB backend for Cloud Heroes Africa platform.

---

## 🚀 Quick Start

```bash
npm install
cp .env.example .env
# Edit .env with your credentials
npm run dev
```

Server runs on: `http://localhost:5000`

---

## 📦 Dependencies

### Core
- **express** - Web framework
- **mongoose** - MongoDB ODM
- **dotenv** - Environment variables

### Authentication
- **passport** - Authentication middleware
- **passport-google-oauth20** - Google OAuth
- **passport-azure-ad** - Microsoft Entra ID
- **jsonwebtoken** - JWT tokens
- **bcryptjs** - Password hashing

### Payment
- **stripe** - Stripe payments
- **paypal-rest-sdk** - PayPal payments
- **axios** - HTTP client for MTN/Orange APIs

### Communication
- **socket.io** - Real-time WebSocket
- **nodemailer** - Email service

### Security
- **helmet** - Security headers
- **cors** - CORS middleware
- **express-rate-limit** - Rate limiting
- **express-validator** - Input validation

---

## 📁 Structure

```
backend/
├── src/
│   ├── config/
│   │   ├── database.js          # MongoDB connection
│   │   └── jwt.js               # JWT utilities
│   ├── models/
│   │   ├── User.js              # User schema
│   │   └── Donation.js          # Donation schema
│   ├── routes/
│   │   ├── auth.routes.js       # Authentication
│   │   ├── payment.routes.js    # Payments
│   │   ├── student.routes.js    # Student endpoints
│   │   ├── admin.routes.js      # Admin endpoints
│   │   ├── donor.routes.js      # Donor endpoints
│   │   ├── volunteer.routes.js  # Volunteer endpoints
│   │   └── community.routes.js  # Community endpoints
│   ├── middleware/
│   │   ├── auth.js              # JWT verification
│   │   ├── rateLimiter.js       # Rate limiting
│   │   └── errorHandler.js      # Error handling
│   ├── services/
│   │   ├── payment/
│   │   │   ├── stripe.js        # Stripe integration
│   │   │   ├── paypal.js        # PayPal integration
│   │   │   ├── mtn-momo.js      # MTN Mobile Money
│   │   │   └── orange-money.js  # Orange Money
│   │   ├── email/
│   │   │   └── emailService.js  # Nodemailer
│   │   └── socket/
│   │       └── socketHandler.js # Socket.io events
│   └── server.js                # Entry point
├── package.json
└── .env.example
```

---

## 🔌 API Endpoints

### Authentication
```
GET  /api/auth/google              - Initiate Google OAuth
GET  /api/auth/google/callback     - Google callback
GET  /api/auth/azure               - Initiate Azure OAuth
POST /api/auth/azure/callback      - Azure callback
GET  /api/auth/me                  - Get current user
POST /api/auth/logout              - Logout
```

### Payments
```
POST /api/payments/stripe/create-checkout    - Create Stripe session
GET  /api/payments/stripe/verify/:sessionId  - Verify Stripe payment
POST /api/payments/paypal/create             - Create PayPal payment
POST /api/payments/paypal/execute            - Execute PayPal payment
POST /api/payments/mtn/request               - Request MTN MoMo payment
GET  /api/payments/mtn/status/:referenceId   - Check MTN status
POST /api/payments/orange/initiate           - Initiate Orange Money
GET  /api/payments/orange/status/:orderId    - Check Orange status
```

### Role-Specific (Protected)
```
GET /api/student/dashboard         - Student dashboard data
GET /api/admin/dashboard           - Admin dashboard data
GET /api/donor/dashboard           - Donor dashboard data
GET /api/volunteer/dashboard       - Volunteer dashboard data
```

### Community (Public)
```
GET /api/community/stats           - Community statistics
GET /api/community/forum           - Forum posts
```

---

## 🔐 Environment Variables

```env
# Server
NODE_ENV=development
PORT=5000
FRONTEND_URL=http://localhost:5173

# Database
MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/cloudheroes

# JWT
JWT_SECRET=your-jwt-secret
JWT_EXPIRE=7d
JWT_REFRESH_SECRET=your-refresh-secret
JWT_REFRESH_EXPIRE=30d

# Google OAuth
GOOGLE_CLIENT_ID=xxx.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=xxx
GOOGLE_CALLBACK_URL=http://localhost:5000/api/auth/google/callback

# Microsoft Entra ID
AZURE_CLIENT_ID=xxx
AZURE_TENANT_ID=xxx
AZURE_CLIENT_SECRET=xxx
AZURE_CALLBACK_URL=http://localhost:5000/api/auth/azure/callback

# Stripe
STRIPE_SECRET_KEY=sk_test_xxx
STRIPE_PUBLISHABLE_KEY=pk_test_xxx
STRIPE_WEBHOOK_SECRET=whsec_xxx

# PayPal
PAYPAL_MODE=sandbox
PAYPAL_CLIENT_ID=xxx
PAYPAL_CLIENT_SECRET=xxx

# MTN Mobile Money
MTN_MOMO_API_KEY=xxx
MTN_MOMO_API_SECRET=xxx
MTN_MOMO_SUBSCRIPTION_KEY=xxx
MTN_MOMO_ENVIRONMENT=sandbox

# Orange Money
ORANGE_MONEY_API_KEY=xxx
ORANGE_MONEY_API_SECRET=xxx
ORANGE_MONEY_MERCHANT_ID=xxx
ORANGE_MONEY_ENVIRONMENT=sandbox

# Email
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=your-email@gmail.com
EMAIL_PASSWORD=your-gmail-app-password
EMAIL_FROM=Cloud Heroes Africa <noreply@cloudheroes.africa>

# Session
SESSION_SECRET=your-session-secret
SESSION_TIMEOUT=1800000

# MFA Grace Periods (days)
MFA_GRACE_STUDENT=14
MFA_GRACE_DONOR=30
MFA_GRACE_ADMIN=0
MFA_GRACE_VOLUNTEER=0

# Rate Limiting
RATE_LIMIT_WINDOW_MS=900000
RATE_LIMIT_MAX_REQUESTS=100
```

---

## 🧪 Testing

### Manual Testing with cURL

**Health Check:**
```bash
curl http://localhost:5000
```

**Get Community Stats:**
```bash
curl http://localhost:5000/api/community/stats
```

**Test Authentication (with token):**
```bash
curl -H "Authorization: Bearer YOUR_JWT_TOKEN" \
     http://localhost:5000/api/auth/me
```

---

## 🔒 Security Features

- **Helmet** - Security headers
- **CORS** - Cross-origin resource sharing
- **Rate Limiting** - Prevent abuse
- **JWT** - Token-based auth
- **bcrypt** - Password hashing
- **Input Validation** - express-validator
- **HttpOnly Cookies** - Secure token storage

---

## 📊 Database Models

### User Model
```javascript
{
  name: String,
  email: String (unique),
  password: String (hashed),
  role: ['student', 'administrator', 'donor', 'volunteer'],
  provider: ['google', 'azure', 'local'],
  providerId: String,
  avatar: String,
  isActive: Boolean,
  isVerified: Boolean,
  mfaEnabled: Boolean,
  lastLogin: Date,
  timestamps: true
}
```

### Donation Model
```javascript
{
  donor: ObjectId (ref: User),
  donorEmail: String,
  donorName: String,
  amount: Number,
  currency: String,
  paymentMethod: ['stripe', 'paypal', 'mtn-momo', 'orange-money'],
  paymentStatus: ['pending', 'completed', 'failed', 'refunded'],
  transactionId: String (unique),
  timestamps: true
}
```

---

## 🔄 Real-time Events (Socket.io)

### Server Events
```javascript
// User joins
socket.on('user:join', (userId) => { ... });

// Forum message
socket.on('forum:message', (data) => { ... });

// Donation received
socket.on('donation:new', (donation) => { ... });

// User disconnects
socket.on('disconnect', () => { ... });
```

### Client Events
```javascript
// User online
socket.emit('user:online', userId);

// New notification
socket.emit('notification:receive', notification);

// Donation alert
socket.emit('donation:received', donation);
```

---

## 🚀 Deployment

### Production Build
```bash
npm start
```

### With PM2
```bash
npm install -g pm2
pm2 start src/server.js --name cloud-heroes-backend
pm2 save
pm2 startup
```

---

## 📝 Scripts

```bash
npm start       # Start production server
npm run dev     # Start development server with nodemon
npm test        # Run tests (not implemented yet)
```

---

## 🐛 Debugging

### Enable Debug Logs
```bash
DEBUG=* npm run dev
```

### Check MongoDB Connection
```javascript
mongoose.connection.on('connected', () => {
  console.log('MongoDB connected');
});
```

### Test Email Service
```javascript
const { sendEmail } = require('./services/email/emailService');
await sendEmail('test@example.com', 'Test', '<h1>Test</h1>', 'Test');
```

---

## 📚 Resources

- **Express Docs**: https://expressjs.com/
- **Mongoose Docs**: https://mongoosejs.com/
- **Passport Docs**: http://www.passportjs.org/
- **Socket.io Docs**: https://socket.io/docs/

---

**Version:** 1.0.0  
**Node.js:** v18+  
**License:** MIT
