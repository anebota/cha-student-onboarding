const jwt = require('jsonwebtoken');
const User = require('../models/User');

// Protect routes - verify JWT token
exports.protect = async (req, res, next) => {
  try {
    let token;

    // Check for token in Authorization header
    if (req.headers.authorization && req.headers.authorization.startsWith('Bearer')) {
      token = req.headers.authorization.split(' ')[1];
    } else if (req.cookies.token) {
      token = req.cookies.token;
    }

    if (!token) {
      return res.status(401).json({
        success: false,
        message: 'Not authorized to access this route'
      });
    }

    try {
      // Verify token
      const decoded = jwt.verify(token, process.env.JWT_SECRET);

      // Get user from token
      req.user = await User.findById(decoded.id).select('-password');

      if (!req.user) {
        return res.status(401).json({
          success: false,
          message: 'User not found'
        });
      }

      if (!req.user.isActive) {
        return res.status(401).json({
          success: false,
          message: 'User account is deactivated'
        });
      }

      next();
    } catch (error) {
      return res.status(401).json({
        success: false,
        message: 'Invalid token'
      });
    }
  } catch (error) {
    return res.status(500).json({
      success: false,
      message: 'Server error'
    });
  }
};

// Role-based access control
exports.authorize = (...roles) => {
  return (req, res, next) => {
    if (!roles.includes(req.user.role)) {
      return res.status(403).json({
        success: false,
        message: `Role '${req.user.role}' is not authorized to access this route`
      });
    }
    next();
  };
};

// Check MFA requirement
exports.checkMFA = async (req, res, next) => {
  try {
    const user = req.user;

    // Admins and volunteers require immediate MFA
    if (['administrator', 'volunteer'].includes(user.role) && !user.mfaEnabled) {
      return res.status(403).json({
        success: false,
        message: 'MFA is required for your role',
        requireMFA: true
      });
    }

    // Students and donors have grace period
    if (['student', 'donor'].includes(user.role) && !user.mfaEnabled) {
      if (!user.isWithinMfaGracePeriod()) {
        return res.status(403).json({
          success: false,
          message: 'MFA grace period has expired. Please enable MFA.',
          requireMFA: true
        });
      }
    }

    next();
  } catch (error) {
    return res.status(500).json({
      success: false,
      message: 'Server error'
    });
  }
};
