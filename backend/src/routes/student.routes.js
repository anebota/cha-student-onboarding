const express = require('express');
const router = express.Router();
const { protect, authorize } = require('../middleware/auth');

// @route   GET /api/student/dashboard
// @desc    Get student dashboard data
// @access  Private (Student only)
router.get('/dashboard', protect, authorize('student'), async (req, res) => {
  res.json({
    success: true,
    data: {
      coursesEnrolled: 5,
      certifications: 3,
      progress: 85
    }
  });
});

module.exports = router;
