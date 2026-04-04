const express = require('express');
const router = express.Router();
const { protect, authorize } = require('../middleware/auth');

// @route   GET /api/donor/dashboard
// @desc    Get donor dashboard data
// @access  Private (Donor only)
router.get('/dashboard', protect, authorize('donor'), async (req, res) => {
  res.json({
    success: true,
    data: {
      totalDonated: 5000,
      studentsSupported: 25,
      certificationsFunded: 12
    }
  });
});

module.exports = router;
