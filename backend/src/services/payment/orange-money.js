const axios = require('axios');
const Donation = require('../../models/Donation');

// Orange Money API Configuration
const ORANGE_BASE_URL = process.env.ORANGE_MONEY_ENVIRONMENT === 'production'
  ? 'https://api.orange.com/orange-money-webpay/cm/v1'
  : 'https://api.orange.com/orange-money-webpay/dev/v1';

// Initiate Orange Money payment
exports.initiatePayment = async (amount, phoneNumber, donorName, donorEmail) => {
  try {
    const orderId = `ORD-${Date.now()}-${Math.random().toString(36).substr(2, 9)}`;
    
    const response = await axios.post(
      `${ORANGE_BASE_URL}/webpayment`,
      {
        merchant_key: process.env.ORANGE_MONEY_MERCHANT_ID,
        currency: 'XAF',
        order_id: orderId,
        amount: amount,
        return_url: `${process.env.ORANGE_MONEY_CALLBACK_URL}?orderId=${orderId}`,
        cancel_url: `${process.env.FRONTEND_URL}/donation/cancel`,
        notif_url: `${process.env.ORANGE_MONEY_CALLBACK_URL}/notify`,
        lang: 'en',
        reference: `Donation from ${donorName}`
      },
      {
        headers: {
          'Authorization': `Bearer ${await getOrangeAccessToken()}`,
          'Content-Type': 'application/json'
        }
      }
    );

    // Create pending donation record
    const donation = await Donation.create({
      donorEmail: donorEmail,
      donorName: donorName,
      amount: amount,
      currency: 'XAF',
      paymentMethod: 'orange-money',
      paymentStatus: 'pending',
      transactionId: orderId,
      paymentDetails: {
        phoneNumber: phoneNumber,
        orderId: orderId,
        paymentUrl: response.data.payment_url
      }
    });

    return {
      success: true,
      orderId,
      paymentUrl: response.data.payment_url,
      donation,
      message: 'Redirect to Orange Money payment page'
    };
  } catch (error) {
    console.error('Orange Money payment initiation error:', error.response?.data || error.message);
    throw new Error('Failed to initiate Orange Money payment');
  }
};

// Check Orange Money payment status
exports.checkPaymentStatus = async (orderId) => {
  try {
    const response = await axios.get(
      `${ORANGE_BASE_URL}/webpayment/${orderId}`,
      {
        headers: {
          'Authorization': `Bearer ${await getOrangeAccessToken()}`
        }
      }
    );

    const status = response.data.status;

    // Update donation status
    if (status === 'SUCCESS') {
      await Donation.findOneAndUpdate(
        { transactionId: orderId },
        { 
          paymentStatus: 'completed',
          'paymentDetails.transactionId': response.data.txnid
        }
      );
    } else if (status === 'FAILED' || status === 'EXPIRED') {
      await Donation.findOneAndUpdate(
        { transactionId: orderId },
        { paymentStatus: 'failed' }
      );
    }

    return {
      success: true,
      status: status,
      details: response.data
    };
  } catch (error) {
    console.error('Orange Money status check error:', error.response?.data || error.message);
    throw new Error('Failed to check Orange Money payment status');
  }
};

// Handle Orange Money callback/notification
exports.handleCallback = async (orderId, status, txnId) => {
  try {
    const paymentStatus = status === 'SUCCESS' ? 'completed' : 'failed';
    
    const donation = await Donation.findOneAndUpdate(
      { transactionId: orderId },
      { 
        paymentStatus: paymentStatus,
        'paymentDetails.transactionId': txnId,
        'paymentDetails.callbackStatus': status
      },
      { new: true }
    );

    return {
      success: true,
      donation
    };
  } catch (error) {
    console.error('Orange Money callback error:', error);
    throw new Error('Failed to process Orange Money callback');
  }
};

// Get Orange Money access token
async function getOrangeAccessToken() {
  try {
    const response = await axios.post(
      'https://api.orange.com/oauth/v3/token',
      'grant_type=client_credentials',
      {
        headers: {
          'Authorization': `Basic ${Buffer.from(`${process.env.ORANGE_MONEY_API_KEY}:${process.env.ORANGE_MONEY_API_SECRET}`).toString('base64')}`,
          'Content-Type': 'application/x-www-form-urlencoded'
        }
      }
    );

    return response.data.access_token;
  } catch (error) {
    console.error('Orange Money token error:', error.response?.data || error.message);
    throw new Error('Failed to get Orange Money access token');
  }
}

module.exports = exports;
