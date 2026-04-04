const CommunityHome = () => {
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

export default CommunityHome;