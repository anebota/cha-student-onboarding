import { Link } from 'react-router-dom';
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

export default Navbar;