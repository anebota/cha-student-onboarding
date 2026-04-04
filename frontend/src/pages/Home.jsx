import { Link } from 'react-router-dom';

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

export default Home;