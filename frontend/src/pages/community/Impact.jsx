const Impact = () => {
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

export default Impact;