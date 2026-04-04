const express = require('express');
const router = express.Router();
const { protect, authorize } = require('../middleware/auth');

// @route   GET /api/volunteer/dashboard
// @desc    Get volunteer dashboard data
// @access  Private (Volunteer only)
router.get('/dashboard', protect, authorize('volunteer'), async (req, res) => {
  res.json({
    success: true,
    data: {
      classesAssigned: 3,
      studentsMentored: 45,
      completionRate: 92
    }
  });
});

module.exports = router;
