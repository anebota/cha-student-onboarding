#!/usr/bin/env python3
"""
Generate all React frontend files for Cloud Heroes Africa
"""
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(BASE_DIR, 'frontend', 'src')

# All React component and page files
files = {
    # Context files
    'context/AuthContext.jsx': '''import { createContext, useContext, useState, useEffect } from 'react';
import api from '../services/api';

const AuthContext = createContext();

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within AuthProvider');
  }
  return context;
};

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    checkAuth();
  }, []);

  const checkAuth = async () => {
    try {
      const response = await api.get('/auth/me');
      if (response.data.success) {
        setUser(response.data.user);
      }
    } catch (error) {
      console.error('Auth check failed:', error);
    } finally {
      setLoading(false);
    }
  };

  const logout = async () => {
    try {
      await api.post('/auth/logout');
      setUser(null);
      window.location.href = '/';
    } catch (error) {
      console.error('Logout failed:', error);
    }
  };

  return (
    <AuthContext.Provider value={{ user, setUser, loading, logout }}>
      {children}
    </AuthContext.Provider>
  );
};''',

    'context/SocketContext.jsx': '''import { createContext, useContext, useEffect, useState } from 'react';
import io from 'socket.io-client';
import { useAuth } from './AuthContext';

const SocketContext = createContext();

export const useSocket = () => {
  return useContext(SocketContext);
};

export const SocketProvider = ({ children }) => {
  const [socket, setSocket] = useState(null);
  const { user } = useAuth();

  useEffect(() => {
    if (user) {
      const newSocket = io(import.meta.env.VITE_SOCKET_URL || 'http://localhost:5000');
      
      newSocket.on('connect', () => {
        console.log('Socket connected');
        newSocket.emit('user:join', user._id);
      });

      setSocket(newSocket);

      return () => newSocket.close();
    }
  }, [user]);

  return (
    <SocketContext.Provider value={socket}>
      {children}
    </SocketContext.Provider>
  );
};''',

    # Services
    'services/api.js': '''import axios from 'axios';

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || 'http://localhost:5000/api',
  withCredentials: true
});

api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

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

export default api;''',

    # Components
    'components/common/Navbar.jsx': '''import { Link } from 'react-router-dom';
import { useAuth } from '../../context/AuthContext';

const Navbar = () => {
  const { user, logout } = useAuth();

  return (
    <nav className="bg-white shadow-lg">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16">
          <div className="flex items-center">
            <Link to="/" className="text-2xl font-bold text-primary-600">
              ☁️ Cloud Heroes Africa
            </Link>
          </div>
          <div className="flex items-center space-x-4">
            <Link to="/" className="text-gray-700 hover:text-primary-600">Home</Link>
            <Link to="/community" className="text-gray-700 hover:text-primary-600">Community</Link>
            {user ? (
              <>
                <Link to={`/${user.role}/dashboard`} className="text-gray-700 hover:text-primary-600">
                  Dashboard
                </Link>
                <button onClick={logout} className="bg-red-500 text-white px-4 py-2 rounded hover:bg-red-600">
                  Logout
                </button>
              </>
            ) : (
              <Link to="/login" className="bg-primary-600 text-white px-4 py-2 rounded hover:bg-primary-700">
                Login
              </Link>
            )}
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;''',

    'components/auth/PrivateRoute.jsx': '''import { Navigate } from 'react-router-dom';
import { useAuth } from '../../context/AuthContext';

const PrivateRoute = ({ children, role }) => {
  const { user, loading } = useAuth();

  if (loading) {
    return <div className="flex justify-center items-center h-screen">
      <div className="text-white text-2xl">Loading...</div>
    </div>;
  }

  if (!user) {
    return <Navigate to="/login" />;
  }

  if (role && user.role !== role) {
    return <Navigate to="/" />;
  }

  return children;
};

export default PrivateRoute;''',

    # Pages
    'pages/Home.jsx': '''import { Link } from 'react-router-dom';

const Home = () => {
  return (
    <div className="container mx-auto px-4 py-8">
      <div className="bg-white rounded-lg shadow-xl p-8 mb-8">
        <h1 className="text-4xl font-bold text-gray-800 mb-4">Welcome to Cloud Heroes Africa ☁️</h1>
        <p className="text-xl text-gray-600 mb-6">Empowering the next generation of cloud professionals across Africa.</p>
        
        <div className="mt-8">
          <h2 className="text-2xl font-bold text-primary-600 mb-4">Our Mission</h2>
          <p className="text-gray-700 mb-4">Cloud Heroes Africa is dedicated to providing world-class cloud computing education and resources to students across the African continent.</p>
        </div>

        <div className="mt-8">
          <h2 className="text-2xl font-bold text-primary-600 mb-4">Get Started</h2>
          <p className="text-gray-700 mb-4">Join our community of learners, educators, and supporters.</p>
          <div className="flex space-x-4">
            <Link to="/login" className="bg-primary-600 text-white px-6 py-3 rounded-lg hover:bg-primary-700">
              Login
            </Link>
            <Link to="/community" className="bg-secondary-600 text-white px-6 py-3 rounded-lg hover:bg-secondary-700">
              Explore Community
            </Link>
          </div>
        </div>
      </div>

      <div className="bg-white rounded-lg shadow-xl p-8">
        <h2 className="text-2xl font-bold text-primary-600 mb-6">Four Ways to Participate</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          <div className="bg-gray-50 p-6 rounded-lg">
            <h3 className="text-xl font-bold text-primary-600 mb-2">🎓 Students</h3>
            <p className="text-gray-700">Access free cloud computing courses and certifications.</p>
          </div>
          <div className="bg-gray-50 p-6 rounded-lg">
            <h3 className="text-xl font-bold text-primary-600 mb-2">👨‍💼 Administrators</h3>
            <p className="text-gray-700">Manage platform operations and user access.</p>
          </div>
          <div className="bg-gray-50 p-6 rounded-lg">
            <h3 className="text-xl font-bold text-primary-600 mb-2">💝 Donors</h3>
            <p className="text-gray-700">Support students with scholarships and resources.</p>
          </div>
          <div className="bg-gray-50 p-6 rounded-lg">
            <h3 className="text-xl font-bold text-primary-600 mb-2">🤝 Volunteers</h3>
            <p className="text-gray-700">Mentor students and contribute to the community.</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Home;''',

    'pages/Login.jsx': '''const Login = () => {
  const handleGoogleLogin = () => {
    window.location.href = import.meta.env.VITE_GOOGLE_AUTH_URL || 'http://localhost:5000/api/auth/google';
  };

  const handleAzureLogin = () => {
    window.location.href = import.meta.env.VITE_AZURE_AUTH_URL || 'http://localhost:5000/api/auth/azure';
  };

  return (
    <div className="container mx-auto px-4 py-16">
      <div className="max-w-md mx-auto bg-white rounded-lg shadow-xl p-8">
        <h1 className="text-3xl font-bold text-gray-800 mb-6">Login to Cloud Heroes Africa</h1>
        <p className="text-gray-600 mb-8">Choose your login method based on your role.</p>

        <div className="mb-8">
          <h2 className="text-xl font-bold text-gray-800 mb-4">Students & Donors</h2>
          <p className="text-gray-600 mb-4">Login with your Google account</p>
          <button
            onClick={handleGoogleLogin}
            className="w-full bg-primary-600 text-white py-3 rounded-lg hover:bg-primary-700 flex items-center justify-center"
          >
            🔐 Login with Google
          </button>
        </div>

        <div className="border-t pt-8">
          <h2 className="text-xl font-bold text-gray-800 mb-4">Administrators & Volunteers</h2>
          <p className="text-gray-600 mb-4">Login with your Microsoft account</p>
          <button
            onClick={handleAzureLogin}
            className="w-full bg-secondary-600 text-white py-3 rounded-lg hover:bg-secondary-700 flex items-center justify-center"
          >
            🔐 Login with Microsoft
          </button>
        </div>
      </div>
    </div>
  );
};

export default Login;''',

    'pages/AuthCallback.jsx': '''import { useEffect } from 'react';
import { useNavigate, useSearchParams } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';

const AuthCallback = () => {
  const [searchParams] = useSearchParams();
  const navigate = useNavigate();
  const { setUser } = useAuth();

  useEffect(() => {
    const token = searchParams.get('token');
    const role = searchParams.get('role');

    if (token && role) {
      localStorage.setItem('token', token);
      
      // Fetch user data
      fetch(`${import.meta.env.VITE_API_URL}/api/auth/me`, {
        headers: {
          'Authorization': `Bearer ${token}`
        }
      })
        .then(res => res.json())
        .then(data => {
          if (data.success) {
            setUser(data.user);
            navigate(`/${role}/dashboard`);
          }
        })
        .catch(err => {
          console.error('Auth callback error:', err);
          navigate('/login');
        });
    } else {
      navigate('/login');
    }
  }, [searchParams, navigate, setUser]);

  return (
    <div className="flex justify-center items-center h-screen">
      <div className="text-white text-2xl">Authenticating...</div>
    </div>
  );
};

export default AuthCallback;''',

    'pages/student/Dashboard.jsx': '''import { useAuth } from '../../context/AuthContext';

const StudentDashboard = () => {
  const { user } = useAuth();

  return (
    <div className="container mx-auto px-4 py-8">
      <div className="bg-white rounded-lg shadow-xl p-8 mb-8">
        <h1 className="text-3xl font-bold text-gray-800 mb-4">Welcome, {user?.name}! 🎓</h1>
        <p className="text-gray-600"><strong>Email:</strong> {user?.email}</p>
        <p className="text-gray-600"><strong>Role:</strong> Student</p>

        <div className="mt-8">
          <h2 className="text-2xl font-bold text-primary-600 mb-4">Your Learning Journey</h2>
          <p className="text-gray-700 mb-4">Access your courses, resources, and community forums.</p>
          <div className="flex space-x-4">
            <a href="/community/forum" className="bg-primary-600 text-white px-6 py-3 rounded-lg hover:bg-primary-700">
              Community Forum
            </a>
            <a href="/community/resources" className="bg-secondary-600 text-white px-6 py-3 rounded-lg hover:bg-secondary-700">
              Learning Resources
            </a>
          </div>
        </div>

        <div className="mt-8">
          <h2 className="text-2xl font-bold text-primary-600 mb-4">Quick Stats</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div className="bg-gray-50 p-6 rounded-lg text-center">
              <h3 className="text-4xl font-bold text-primary-600">5</h3>
              <p className="text-gray-700">Courses Enrolled</p>
            </div>
            <div className="bg-gray-50 p-6 rounded-lg text-center">
              <h3 className="text-4xl font-bold text-secondary-600">3</h3>
              <p className="text-gray-700">Certifications</p>
            </div>
            <div className="bg-gray-50 p-6 rounded-lg text-center">
              <h3 className="text-4xl font-bold text-orange-600">85%</h3>
              <p className="text-gray-700">Progress</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default StudentDashboard;''',

    'pages/administrator/Dashboard.jsx': '''import { useAuth } from '../../context/AuthContext';

const AdministratorDashboard = () => {
  const { user } = useAuth();

  return (
    <div className="container mx-auto px-4 py-8">
      <div className="bg-white rounded-lg shadow-xl p-8">
        <h1 className="text-3xl font-bold text-gray-800 mb-4">Administrator Dashboard 👨‍💼</h1>
        <p className="text-gray-600"><strong>Name:</strong> {user?.name}</p>
        <p className="text-gray-600"><strong>Email:</strong> {user?.email}</p>

        <div className="mt-8">
          <h2 className="text-2xl font-bold text-primary-600 mb-4">Platform Management</h2>
          <div className="flex space-x-4">
            <button className="bg-primary-600 text-white px-6 py-3 rounded-lg hover:bg-primary-700">
              User Management
            </button>
            <button className="bg-secondary-600 text-white px-6 py-3 rounded-lg hover:bg-secondary-700">
              Role Assignment
            </button>
          </div>
        </div>

        <div className="mt-8">
          <h2 className="text-2xl font-bold text-primary-600 mb-4">System Statistics</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div className="bg-gray-50 p-6 rounded-lg text-center">
              <h3 className="text-4xl font-bold text-primary-600">1,234</h3>
              <p className="text-gray-700">Total Students</p>
            </div>
            <div className="bg-gray-50 p-6 rounded-lg text-center">
              <h3 className="text-4xl font-bold text-secondary-600">45</h3>
              <p className="text-gray-700">Active Volunteers</p>
            </div>
            <div className="bg-gray-50 p-6 rounded-lg text-center">
              <h3 className="text-4xl font-bold text-orange-600">89</h3>
              <p className="text-gray-700">Donors</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default AdministratorDashboard;''',

    'pages/donor/Dashboard.jsx': '''import { useAuth } from '../../context/AuthContext';

const DonorDashboard = () => {
  const { user } = useAuth();

  return (
    <div className="container mx-auto px-4 py-8">
      <div className="bg-white rounded-lg shadow-xl p-8">
        <h1 className="text-3xl font-bold text-gray-800 mb-4">Welcome, {user?.name}! 💝</h1>
        <p className="text-gray-600"><strong>Email:</strong> {user?.email}</p>
        <p className="text-gray-600"><strong>Role:</strong> Donor</p>

        <div className="mt-8">
          <h2 className="text-2xl font-bold text-primary-600 mb-4">Your Impact</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div className="bg-gray-50 p-6 rounded-lg text-center">
              <h3 className="text-4xl font-bold text-primary-600">$5,000</h3>
              <p className="text-gray-700">Total Donated</p>
            </div>
            <div className="bg-gray-50 p-6 rounded-lg text-center">
              <h3 className="text-4xl font-bold text-secondary-600">25</h3>
              <p className="text-gray-700">Students Supported</p>
            </div>
            <div className="bg-gray-50 p-6 rounded-lg text-center">
              <h3 className="text-4xl font-bold text-orange-600">12</h3>
              <p className="text-gray-700">Certifications Funded</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default DonorDashboard;''',

    'pages/volunteer/Dashboard.jsx': '''import { useAuth } from '../../context/AuthContext';

const VolunteerDashboard = () => {
  const { user } = useAuth();

  return (
    <div className="container mx-auto px-4 py-8">
      <div className="bg-white rounded-lg shadow-xl p-8">
        <h1 className="text-3xl font-bold text-gray-800 mb-4">Welcome, {user?.name}! 🤝</h1>
        <p className="text-gray-600"><strong>Email:</strong> {user?.email}</p>
        <p className="text-gray-600"><strong>Role:</strong> Volunteer</p>

        <div className="mt-8">
          <h2 className="text-2xl font-bold text-primary-600 mb-4">Class Statistics</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div className="bg-gray-50 p-6 rounded-lg text-center">
              <h3 className="text-4xl font-bold text-primary-600">3</h3>
              <p className="text-gray-700">Classes Assigned</p>
            </div>
            <div className="bg-gray-50 p-6 rounded-lg text-center">
              <h3 className="text-4xl font-bold text-secondary-600">45</h3>
              <p className="text-gray-700">Students Mentored</p>
            </div>
            <div className="bg-gray-50 p-6 rounded-lg text-center">
              <h3 className="text-4xl font-bold text-orange-600">92%</h3>
              <p className="text-gray-700">Completion Rate</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default VolunteerDashboard;''',

    'pages/community/CommunityHome.jsx': '''const CommunityHome = () => {
  return (
    <div className="container mx-auto px-4 py-8">
      <div className="bg-white rounded-lg shadow-xl p-8">
        <h1 className="text-3xl font-bold text-gray-800 mb-4">Cloud Heroes Community 🌍</h1>
        <p className="text-xl text-gray-600 mb-8">Connect, learn, and grow with fellow cloud enthusiasts across Africa.</p>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="bg-gray-50 p-6 rounded-lg">
            <h3 className="text-xl font-bold text-primary-600 mb-2">💬 Forum</h3>
            <p className="text-gray-700 mb-4">Discuss cloud topics, ask questions, and share knowledge.</p>
            <a href="/community/forum" className="bg-primary-600 text-white px-4 py-2 rounded hover:bg-primary-700 inline-block">
              Visit Forum
            </a>
          </div>
          <div className="bg-gray-50 p-6 rounded-lg">
            <h3 className="text-xl font-bold text-secondary-600 mb-2">📚 Resources</h3>
            <p className="text-gray-700 mb-4">Access learning materials, tutorials, and study guides.</p>
            <a href="/community/resources" className="bg-secondary-600 text-white px-4 py-2 rounded hover:bg-secondary-700 inline-block">
              Browse Resources
            </a>
          </div>
          <div className="bg-gray-50 p-6 rounded-lg">
            <h3 className="text-xl font-bold text-orange-600 mb-2">📊 Impact</h3>
            <p className="text-gray-700 mb-4">See the collective impact of our community.</p>
            <a href="/community/impact" className="bg-orange-600 text-white px-4 py-2 rounded hover:bg-orange-700 inline-block">
              View Impact
            </a>
          </div>
        </div>
      </div>
    </div>
  );
};

export default CommunityHome;''',

    'pages/community/Forum.jsx': '''const Forum = () => {
  return (
    <div className="container mx-auto px-4 py-8">
      <div className="bg-white rounded-lg shadow-xl p-8">
        <h1 className="text-3xl font-bold text-gray-800 mb-4">Community Forum 💬</h1>
        <p className="text-gray-600 mb-8">Discuss cloud computing topics with the community.</p>

        <div className="space-y-4">
          <div className="bg-gray-50 p-6 rounded-lg">
            <h3 className="text-xl font-bold text-primary-600 mb-2">AWS Certification Tips</h3>
            <p className="text-gray-700 mb-2">Share your experience and tips for AWS certifications.</p>
            <small className="text-gray-500">45 replies • Last activity 2 hours ago</small>
          </div>
          <div className="bg-gray-50 p-6 rounded-lg">
            <h3 className="text-xl font-bold text-primary-600 mb-2">Azure vs AWS: Which to learn first?</h3>
            <p className="text-gray-700 mb-2">Discussion about choosing your first cloud platform.</p>
            <small className="text-gray-500">32 replies • Last activity 5 hours ago</small>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Forum;''',

    'pages/community/Resources.jsx': '''const Resources = () => {
  return (
    <div className="container mx-auto px-4 py-8">
      <div className="bg-white rounded-lg shadow-xl p-8">
        <h1 className="text-3xl font-bold text-gray-800 mb-4">Learning Resources 📚</h1>
        <p className="text-gray-600 mb-8">Curated resources to help you succeed in your cloud journey.</p>

        <div className="space-y-6">
          <div>
            <h2 className="text-2xl font-bold text-primary-600 mb-4">AWS Resources</h2>
            <ul className="list-disc list-inside space-y-2 text-gray-700">
              <li>AWS Cloud Practitioner Study Guide</li>
              <li>AWS Solutions Architect Practice Tests</li>
              <li>AWS Well-Architected Framework</li>
            </ul>
          </div>
          <div>
            <h2 className="text-2xl font-bold text-primary-600 mb-4">Azure Resources</h2>
            <ul className="list-disc list-inside space-y-2 text-gray-700">
              <li>Azure Fundamentals Learning Path</li>
              <li>Azure Administrator Study Materials</li>
              <li>Azure Architecture Best Practices</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Resources;''',

    'pages/community/Impact.jsx': '''const Impact = () => {
  return (
    <div className="container mx-auto px-4 py-8">
      <div className="bg-white rounded-lg shadow-xl p-8">
        <h1 className="text-3xl font-bold text-gray-800 mb-4">Our Impact 📊</h1>
        <p className="text-gray-600 mb-8">See the difference we're making together across Africa.</p>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          <div className="bg-gray-50 p-6 rounded-lg text-center">
            <h3 className="text-5xl font-bold text-primary-600">1,234</h3>
            <p className="text-gray-700 font-semibold">Students Enrolled</p>
          </div>
          <div className="bg-gray-50 p-6 rounded-lg text-center">
            <h3 className="text-5xl font-bold text-secondary-600">567</h3>
            <p className="text-gray-700 font-semibold">Certifications Earned</p>
          </div>
          <div className="bg-gray-50 p-6 rounded-lg text-center">
            <h3 className="text-5xl font-bold text-orange-600">45</h3>
            <p className="text-gray-700 font-semibold">Active Volunteers</p>
          </div>
          <div className="bg-gray-50 p-6 rounded-lg text-center">
            <h3 className="text-5xl font-bold text-purple-600">$125K</h3>
            <p className="text-gray-700 font-semibold">Scholarships Awarded</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Impact;'''
}

print("Creating React frontend files...")
for filepath, content in files.items():
    full_path = os.path.join(FRONTEND_DIR, filepath)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✓ Created: {filepath}")

print("\n" + "="*60)
print("✅ All React frontend files created!")
print("="*60)
