# Cloud Heroes Africa - Frontend

React + Vite + Tailwind CSS frontend for Cloud Heroes Africa platform.

---

## 🚀 Quick Start

```bash
npm install
cp .env.example .env
# Edit .env with your API URL
npm run dev
```

App runs on: `http://localhost:5173`

---

## 📦 Dependencies

### Core
- **react** - UI library
- **react-dom** - React DOM renderer
- **vite** - Build tool and dev server

### Routing
- **react-router-dom** - Client-side routing

### HTTP & Real-time
- **axios** - HTTP client
- **socket.io-client** - WebSocket client

### Styling
- **tailwindcss** - Utility-first CSS
- **postcss** - CSS processing
- **autoprefixer** - CSS vendor prefixes

---

## 📁 Structure

```
frontend/
├── src/
│   ├── components/
│   │   ├── common/
│   │   │   └── Navbar.jsx          # Navigation bar
│   │   ├── auth/
│   │   │   └── PrivateRoute.jsx    # Protected route wrapper
│   │   └── dashboard/              # Dashboard components
│   ├── pages/
│   │   ├── Home.jsx                # Homepage
│   │   ├── Login.jsx               # Login page
│   │   ├── AuthCallback.jsx        # OAuth callback handler
│   │   ├── student/
│   │   │   └── Dashboard.jsx       # Student dashboard
│   │   ├── administrator/
│   │   │   └── Dashboard.jsx       # Admin dashboard
│   │   ├── donor/
│   │   │   └── Dashboard.jsx       # Donor dashboard
│   │   ├── volunteer/
│   │   │   └── Dashboard.jsx       # Volunteer dashboard
│   │   └── community/
│   │       ├── CommunityHome.jsx   # Community home
│   │       ├── Forum.jsx           # Forum page
│   │       ├── Resources.jsx       # Resources page
│   │       └── Impact.jsx          # Impact dashboard
│   ├── context/
│   │   ├── AuthContext.jsx         # Authentication state
│   │   └── SocketContext.jsx       # Socket.io connection
│   ├── services/
│   │   └── api.js                  # Axios configuration
│   ├── hooks/                      # Custom React hooks
│   ├── utils/                      # Utility functions
│   ├── App.jsx                     # Main app component
│   ├── main.jsx                    # Entry point
│   └── index.css                   # Global styles
├── public/                         # Static assets
├── index.html                      # HTML template
├── vite.config.js                  # Vite configuration
├── tailwind.config.js              # Tailwind configuration
├── postcss.config.js               # PostCSS configuration
├── package.json
└── .env.example
```

---

## 🎨 Tailwind Configuration

### Custom Colors
```javascript
colors: {
  primary: {
    500: '#667eea',  // Main brand color
    600: '#5568d3',
    700: '#4451b8',
  },
  secondary: {
    500: '#48bb78',  // Success/positive actions
    600: '#38a169',
    700: '#2f855a',
  }
}
```

### Usage
```jsx
<button className="bg-primary-600 hover:bg-primary-700 text-white px-4 py-2 rounded">
  Click Me
</button>
```

---

## 🔌 API Integration

### Axios Configuration
```javascript
// src/services/api.js
import axios from 'axios';

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
  withCredentials: true
});

// Request interceptor
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Response interceptor
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem('token');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

export default api;
```

### Usage
```javascript
import api from '../services/api';

// GET request
const response = await api.get('/community/stats');

// POST request
const response = await api.post('/payments/stripe/create-checkout', {
  amount: 100,
  currency: 'USD'
});
```

---

## 🔐 Authentication

### AuthContext
```javascript
import { useAuth } from '../context/AuthContext';

function MyComponent() {
  const { user, loading, logout } = useAuth();

  if (loading) return <div>Loading...</div>;
  if (!user) return <div>Please login</div>;

  return (
    <div>
      <p>Welcome, {user.name}!</p>
      <button onClick={logout}>Logout</button>
    </div>
  );
}
```

### Protected Routes
```javascript
<Route path="/student/dashboard" element={
  <PrivateRoute role="student">
    <StudentDashboard />
  </PrivateRoute>
} />
```

---

## 🔄 Real-time Features

### Socket.io Integration
```javascript
import { useSocket } from '../context/SocketContext';

function MyComponent() {
  const socket = useSocket();

  useEffect(() => {
    if (socket) {
      // Listen for events
      socket.on('notification:receive', (notification) => {
        showNotification(notification);
      });

      // Send events
      socket.emit('forum:message', { text: 'Hello!' });

      // Cleanup
      return () => {
        socket.off('notification:receive');
      };
    }
  }, [socket]);
}
```

---

## 🎯 Routing

### Public Routes
- `/` - Homepage
- `/login` - Login page
- `/community` - Community home
- `/community/forum` - Forum
- `/community/resources` - Resources
- `/community/impact` - Impact dashboard

### Protected Routes
- `/student/dashboard` - Student dashboard (role: student)
- `/administrator/dashboard` - Admin dashboard (role: administrator)
- `/donor/dashboard` - Donor dashboard (role: donor)
- `/volunteer/dashboard` - Volunteer dashboard (role: volunteer)

---

## 🔧 Environment Variables

```env
# API Configuration
VITE_API_URL=http://localhost:5000
VITE_SOCKET_URL=http://localhost:5000

# OAuth URLs
VITE_GOOGLE_AUTH_URL=http://localhost:5000/api/auth/google
VITE_AZURE_AUTH_URL=http://localhost:5000/api/auth/azure

# Stripe
VITE_STRIPE_PUBLISHABLE_KEY=pk_test_xxx

# App Configuration
VITE_APP_NAME=Cloud Heroes Africa
VITE_APP_URL=http://localhost:5173
```

**Note:** All Vite env variables must start with `VITE_`

---

## 🎨 Styling Guidelines

### Tailwind Utilities
```jsx
// Layout
<div className="container mx-auto px-4 py-8">

// Cards
<div className="bg-white rounded-lg shadow-xl p-8">

// Buttons
<button className="bg-primary-600 hover:bg-primary-700 text-white px-6 py-3 rounded-lg">

// Grid
<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">

// Responsive
<div className="text-sm md:text-base lg:text-lg">
```

### Custom CSS (if needed)
```css
/* src/index.css */
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer components {
  .btn-primary {
    @apply bg-primary-600 hover:bg-primary-700 text-white px-6 py-3 rounded-lg;
  }
}
```

---

## 🧪 Development

### Start Dev Server
```bash
npm run dev
```

### Build for Production
```bash
npm run build
```

### Preview Production Build
```bash
npm run preview
```

---

## 📱 Responsive Design

### Breakpoints
```javascript
// Tailwind default breakpoints
sm: '640px'   // Small devices
md: '768px'   // Medium devices
lg: '1024px'  // Large devices
xl: '1280px'  // Extra large devices
2xl: '1536px' // 2X Extra large devices
```

### Usage
```jsx
<div className="text-sm md:text-base lg:text-lg xl:text-xl">
  Responsive text
</div>

<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4">
  Responsive grid
</div>
```

---

## 🚀 Performance Optimization

### Code Splitting
```javascript
import { lazy, Suspense } from 'react';

const StudentDashboard = lazy(() => import('./pages/student/Dashboard'));

<Suspense fallback={<div>Loading...</div>}>
  <StudentDashboard />
</Suspense>
```

### Memoization
```javascript
import { useMemo, useCallback } from 'react';

const expensiveValue = useMemo(() => {
  return computeExpensiveValue(data);
}, [data]);

const handleClick = useCallback(() => {
  doSomething(id);
}, [id]);
```

---

## 🐛 Debugging

### React DevTools
Install React DevTools browser extension for debugging.

### Vite Debug
```bash
DEBUG=vite:* npm run dev
```

### Check API Calls
Open browser DevTools → Network tab

---

## 📦 Build Output

```bash
npm run build
```

Creates `dist/` folder with:
- Optimized JavaScript bundles
- Minified CSS
- Optimized assets
- index.html

---

## 🌐 Deployment

### Static Hosting (Vercel, Netlify)
```bash
npm run build
# Upload dist/ folder
```

### Environment Variables
Set in hosting platform:
```
VITE_API_URL=https://api.yourdomain.com
VITE_SOCKET_URL=https://api.yourdomain.com
```

---

## 📚 Resources

- **React Docs**: https://react.dev/
- **Vite Docs**: https://vitejs.dev/
- **Tailwind Docs**: https://tailwindcss.com/docs
- **React Router**: https://reactrouter.com/

---

**Version:** 1.0.0  
**React:** 18.2  
**Vite:** 5.0  
**License:** MIT
