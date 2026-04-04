const Login = () => {
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

export default Login;