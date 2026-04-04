# Quick Start Guide - Cloud Heroes Africa

## ⚡ Get Running in 5 Minutes

### Step 1: Install Backend Dependencies (2 min)
```bash
cd backend
npm install
```

### Step 2: Configure Backend Environment (1 min)
```bash
cp .env.example .env
```

**Edit `backend/.env` - Minimum required:**
```env
MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/cloudheroes
JWT_SECRET=your-secret-key-here
JWT_REFRESH_SECRET=your-refresh-secret-here
SESSION_SECRET=your-session-secret-here
FRONTEND_URL=http://localhost:5173
```

**Generate secrets:**
```bash
node -e "console.log(require('crypto').randomBytes(32).toString('hex'))"
```

### Step 3: Start Backend (30 sec)
```bash
npm run dev
```

### Step 4: Install Frontend Dependencies (1 min)
**Open NEW terminal:**
```bash
cd frontend
npm install
```

### Step 5: Configure Frontend (30 sec)
```bash
cp .env.example .env
```

**Edit `frontend/.env`:**
```env
VITE_API_URL=http://localhost:5000
VITE_SOCKET_URL=http://localhost:5000
```

### Step 6: Start Frontend (30 sec)
```bash
npm run dev
```

### Step 7: Open Browser
```
http://localhost:5173
```

---

## 🎯 What You'll See

1. **Homepage** - Welcome page with platform overview
2. **Login Page** - Google and Microsoft login options
3. **Community** - Public forum, resources, and impact dashboard

---

## 🔧 MongoDB Atlas Setup (5 min)

1. Go to https://www.mongodb.com/cloud/atlas
2. Sign up (free tier)
3. Create cluster (M0 Free)
4. Create database user
5. Whitelist IP (0.0.0.0/0 for development)
6. Get connection string
7. Paste into `backend/.env` as `MONGODB_URI`

---

## 🔐 OAuth Setup (Optional - 10 min each)

### Google OAuth (Students/Donors)
1. https://console.cloud.google.com/
2. Create project
3. Enable Google+ API
4. Create OAuth credentials
5. Add to `backend/.env`

### Microsoft Entra ID (Admins/Volunteers)
1. https://portal.azure.com/
2. Azure Active Directory
3. App registrations → New
4. Create client secret
5. Add to `backend/.env`

---

## 💳 Payment Setup (Optional - 5 min each)

### Stripe
1. https://stripe.com/ → Sign up
2. Get API keys from Dashboard
3. Add to `backend/.env` and `frontend/.env`

### PayPal
1. https://developer.paypal.com/ → Sign up
2. Create app
3. Get Client ID and Secret
4. Add to `backend/.env`

---

## 📧 Email Setup (Optional - 5 min)

### Gmail App Password
1. Enable 2-Step Verification
2. https://myaccount.google.com/apppasswords
3. Generate app password
4. Add to `backend/.env`

---

## 🧪 Test Without OAuth

Add this to `backend/src/routes/auth.routes.js`:

```javascript
router.get('/test-login/:role', async (req, res) => {
  const { role } = req.params;
  let user = await User.findOne({ email: `test-${role}@test.com` });
  
  if (!user) {
    user = await User.create({
      name: `Test ${role}`,
      email: `test-${role}@test.com`,
      role: role,
      provider: 'local',
      isVerified: true
    });
  }
  
  const token = generateToken(user._id, user.role);
  res.cookie('token', token, { httpOnly: true, maxAge: 7 * 24 * 60 * 60 * 1000 });
  res.redirect(`${process.env.FRONTEND_URL}/auth/callback?token=${token}&role=${role}`);
});
```

**Then visit:**
- `http://localhost:5000/api/auth/test-login/student`
- `http://localhost:5000/api/auth/test-login/administrator`
- `http://localhost:5000/api/auth/test-login/donor`
- `http://localhost:5000/api/auth/test-login/volunteer`

---

## 🚨 Common Issues

### Backend won't start
```bash
# Check Node version (need 18+)
node --version

# Reinstall dependencies
rm -rf node_modules package-lock.json
npm install
```

### MongoDB connection error
- Check `MONGODB_URI` in `.env`
- Ensure password doesn't have special characters
- Whitelist your IP in MongoDB Atlas

### Frontend won't start
```bash
# Check if backend is running
curl http://localhost:5000

# Reinstall dependencies
rm -rf node_modules package-lock.json
npm install
```

### Port already in use
```bash
# Kill process on port 5000 (backend)
# Windows:
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Mac/Linux:
lsof -ti:5000 | xargs kill -9
```

---

## 📚 Next Steps

1. ✅ Get app running locally
2. [ ] Set up MongoDB Atlas
3. [ ] Configure OAuth providers
4. [ ] Set up payment gateways
5. [ ] Configure email service
6. [ ] Read [SETUP.md](SETUP.md) for details
7. [ ] Read [TECH_STACK.md](TECH_STACK.md) for architecture

---

## 🎉 Success!

If you see the Cloud Heroes Africa homepage, you're done! 🚀

**Need help?** See [SETUP.md](SETUP.md) for detailed instructions.
