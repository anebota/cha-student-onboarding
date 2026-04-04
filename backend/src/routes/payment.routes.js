const express = require('express');
const router = express.Router();
const stripeService = require('../services/payment/stripe');
const paypalService = require('../services/payment/paypal');
const mtnMomoService = require('../services/payment/mtn-momo');
const orangeMoneyService = require('../services/payment/orange-money');
const { sendDonationReceipt } = require('../services/email/emailService');

// @route   POST /api/payments/stripe/create-checkout
// @desc    Create Stripe checkout session
// @access  Public
router.post('/stripe/create-checkout', async (req, res) => {
  try {
    const { amount, currency, donorEmail, donorName } = req.body;
    
    const session = await stripeService.createCheckoutSession(
      amount,
      currency,
      donorEmail,
      donorName
    );
    
    res.json({
      success: true,
      ...session
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: error.message
    });
  }
});

// @route   GET /api/payments/stripe/verify/:sessionId
// @desc    Verify Stripe payment
// @access  Public
router.get('/stripe/verify/:sessionId', async (req, res) => {
  try {
    const result = await stripeService.verifyPayment(req.params.sessionId);
    
    if (result.success) {
      // Send receipt email
      await sendDonationReceipt(result.donation);
    }
    
    res.json(result);
  } catch (error) {
    res.status(500).json({
      success: false,
      message: error.message
    });
  }
});

// @route   POST /api/payments/paypal/create
// @desc    Create PayPal payment
// @access  Public
router.post('/paypal/create', async (req, res) => {
  try {
    const { amount, currency, donorEmail, donorName } = req.body;
    
    const result = await paypalService.createPayment(
      amount,
      currency,
      donorEmail,
      donorName,
      `${process.env.FRONTEND_URL}/donation/paypal/success`,
      `${process.env.FRONTEND_URL}/donation/cancel`
    );
    
    res.json(result);
  } catch (error) {
    res.status(500).json({
      success: false,
      message: error.message
    });
  }
});

// @route   POST /api/payments/paypal/execute
// @desc    Execute PayPal payment
// @access  Public
router.post('/paypal/execute', async (req, res) => {
  try {
    const { paymentId, payerId, donorEmail, donorName } = req.body;
    
    const result = await paypalService.executePayment(
      paymentId,
      payerId,
      donorEmail,
      donorName
    );
    
    if (result.success) {
      await sendDonationReceipt(result.donation);
    }
    
    res.json(result);
  } catch (error) {
    res.status(500).json({
      success: false,
      message: error.message
    });
  }
});

// @route   POST /api/payments/mtn/request
// @desc    Request MTN Mobile Money payment
// @access  Public
router.post('/mtn/request', async (req, res) => {
  try {
    const { amount, phoneNumber, donorName, donorEmail } = req.body;
    
    const result = await mtnMomoService.requestPayment(
      amount,
      phoneNumber,
      donorName,
      donorEmail
    );
    
    res.json(result);
  } catch (error) {
    res.status(500).json({
      success: false,
      message: error.message
    });
  }
});

// @route   GET /api/payments/mtn/status/:referenceId
// @desc    Check MTN Mobile Money payment status
// @access  Public
router.get('/mtn/status/:referenceId', async (req, res) => {
  try {
    const result = await mtnMomoService.checkPaymentStatus(req.params.referenceId);
    
    if (result.status === 'SUCCESSFUL') {
      const donation = await require('../models/Donation').findOne({ 
        transactionId: req.params.referenceId 
      });
      if (donation) {
        await sendDonationReceipt(donation);
      }
    }
    
    res.json(result);
  } catch (error) {
    res.status(500).json({
      success: false,
      message: error.message
    });
  }
});

// @route   POST /api/payments/orange/initiate
// @desc    Initiate Orange Money payment
// @access  Public
router.post('/orange/initiate', async (req, res) => {
  try {
    const { amount, phoneNumber, donorName, donorEmail } = req.body;
    
    const result = await orangeMoneyService.initiatePayment(
      amount,
      phoneNumber,
      donorName,
      donorEmail
    );
    
    res.json(result);
  } catch (error) {
    res.status(500).json({
      success: false,
      message: error.message
    });
  }
});

// @route   GET /api/payments/orange/status/:orderId
// @desc    Check Orange Money payment status
// @access  Public
router.get('/orange/status/:orderId', async (req, res) => {
  try {
    const result = await orangeMoneyService.checkPaymentStatus(req.params.orderId);
    
    if (result.status === 'SUCCESS') {
      const donation = await require('../models/Donation').findOne({ 
        transactionId: req.params.orderId 
      });
      if (donation) {
        await sendDonationReceipt(donation);
      }
    }
    
    res.json(result);
  } catch (error) {
    res.status(500).json({
      success: false,
      message: error.message
    });
  }
});

// @route   POST /api/payments/orange/callback
// @desc    Handle Orange Money callback
// @access  Public
router.post('/orange/callback', async (req, res) => {
  try {
    const { orderId, status, txnId } = req.body;
    
    const result = await orangeMoneyService.handleCallback(orderId, status, txnId);
    
    if (result.success && status === 'SUCCESS') {
      await sendDonationReceipt(result.donation);
    }
    
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: error.message
    });
  }
});

module.exports = router;
