const Forum = () => {
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

export default Forum;