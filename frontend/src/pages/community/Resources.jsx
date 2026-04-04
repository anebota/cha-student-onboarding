const Resources = () => {
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

export default Resources;