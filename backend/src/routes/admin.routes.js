const express = require('express');
const router = express.Router();
const { protect, authorize } = require('../middleware/auth');

// @route   GET /api/admin/dashboard
// @desc    Get admin dashboard data
// @access  Private (Administrator only)
router.get('/dashboard', protect, authorize('administrator'), async (req, res) => {
  res.json({
    success: true,
    data: {
      totalStudents: 1234,
      activeVolunteers: 45,
      totalDonors: 89
    }
  });
});

module.exports = router;
