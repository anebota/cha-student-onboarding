const express = require('express');
const router = express.Router();
const { protect } = require('../middleware/auth');

// @route   GET /api/users/profile
// @desc    Get user profile
// @access  Private
router.get('/profile', protect, async (req, res) => {
  res.json({
    success: true,
    user: req.user
  });
});

module.exports = router;
