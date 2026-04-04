const axios = require('axios');
const { v4: uuidv4 } = require('uuid');
const Donation = require('../../models/Donation');

// MTN MoMo API Configuration
const MTN_BASE_URL = process.env.MTN_MOMO_ENVIRONMENT === 'production' 
  ? 'https://proxy.momoapi.mtn.com'
  : 'https://sandbox.momodeveloper.mtn.com';

// Create MTN MoMo payment request
exports.requestPayment = async (amount, phoneNumber, donorName, donorEmail) => {
  try {
    const referenceId = uuidv4();
    
    const response = await axios.post(
      `${MTN_BASE_URL}/collection/v1_0/requesttopay`,
      {
        amount: amount.toString(),
        currency: 'XAF', // Central African Franc (Cameroon)
        externalId: referenceId,
        payer: {
          partyIdType: 'MSISDN',
          partyId: phoneNumber
        },
        payerMessage: 'Donation to Cloud Heroes Africa',
        payeeNote: `Donation from ${donorName}`
      },
      {
        headers: {
          'X-Reference-Id': referenceId,
          'X-Target-Environment': process.env.MTN_MOMO_ENVIRONMENT || 'sandbox',
          'Ocp-Apim-Subscription-Key': process.env.MTN_MOMO_SUBSCRIPTION_KEY,
          'Authorization': `Bearer ${await getMTNAccessToken()}`,
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
      paymentMethod: 'mtn-momo',
      paymentStatus: 'pending',
      transactionId: referenceId,
      paymentDetails: {
        phoneNumber: phoneNumber,
        referenceId: referenceId
      }
    });

    return {
      success: true,
      referenceId,
      donation,
      message: 'Payment request sent. Please approve on your phone.'
    };
  } catch (error) {
    console.error('MTN MoMo payment request error:', error.response?.data || error.message);
    throw new Error('Failed to create MTN MoMo payment request');
  }
};

// Check MTN MoMo payment status
exports.checkPaymentStatus = async (referenceId) => {
  try {
    const response = await axios.get(
      `${MTN_BASE_URL}/collection/v1_0/requesttopay/${referenceId}`,
      {
        headers: {
          'X-Target-Environment': process.env.MTN_MOMO_ENVIRONMENT || 'sandbox',
          'Ocp-Apim-Subscription-Key': process.env.MTN_MOMO_SUBSCRIPTION_KEY,
          'Authorization': `Bearer ${await getMTNAccessToken()}`
        }
      }
    );

    const status = response.data.status;

    // Update donation status
    if (status === 'SUCCESSFUL') {
      await Donation.findOneAndUpdate(
        { transactionId: referenceId },
        { paymentStatus: 'completed' }
      );
    } else if (status === 'FAILED') {
      await Donation.findOneAndUpdate(
        { transactionId: referenceId },
        { paymentStatus: 'failed' }
      );
    }

    return {
      success: true,
      status: status,
      details: response.data
    };
  } catch (error) {
    console.error('MTN MoMo status check error:', error.response?.data || error.message);
    throw new Error('Failed to check MTN MoMo payment status');
  }
};

// Get MTN MoMo access token
async function getMTNAccessToken() {
  try {
    const response = await axios.post(
      `${MTN_BASE_URL}/collection/token/`,
      {},
      {
        headers: {
          'Ocp-Apim-Subscription-Key': process.env.MTN_MOMO_SUBSCRIPTION_KEY,
          'Authorization': `Basic ${Buffer.from(`${process.env.MTN_MOMO_API_KEY}:${process.env.MTN_MOMO_API_SECRET}`).toString('base64')}`
        }
      }
    );

    return response.data.access_token;
  } catch (error) {
    console.error('MTN MoMo token error:', error.response?.data || error.message);
    throw new Error('Failed to get MTN MoMo access token');
  }
}

module.exports = exports;
