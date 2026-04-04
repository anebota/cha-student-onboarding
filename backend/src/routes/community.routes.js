const express = require('express');
const router = express.Router();

// @route   GET /api/community/stats
// @desc    Get community statistics
// @access  Public
router.get('/stats', async (req, res) => {
  res.json({
    success: true,
    data: {
      studentsEnrolled: 1234,
      certificationsEarned: 567,
      activeVolunteers: 45,
      scholarshipsAwarded: 125000
    }
  });
});

// @route   GET /api/community/forum
// @desc    Get forum posts
// @access  Public
router.get('/forum', async (req, res) => {
  res.json({
    success: true,
    posts: [
      {
        id: 1,
        title: 'AWS Certification Tips',
        replies: 45,
        lastActivity: '2 hours ago'
      },
      {
        id: 2,
        title: 'Azure vs AWS: Which to learn first?',
        replies: 32,
        lastActivity: '5 hours ago'
      }
    ]
  });
});

module.exports = router;
