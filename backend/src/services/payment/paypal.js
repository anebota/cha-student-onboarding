const paypal = require('paypal-rest-sdk');
const Donation = require('../../models/Donation');

// Configure PayPal
paypal.configure({
  mode: process.env.PAYPAL_MODE || 'sandbox',
  client_id: process.env.PAYPAL_CLIENT_ID,
  client_secret: process.env.PAYPAL_CLIENT_SECRET
});

// Create PayPal payment
exports.createPayment = async (amount, currency, donorEmail, donorName, returnUrl, cancelUrl) => {
  return new Promise((resolve, reject) => {
    const create_payment_json = {
      intent: 'sale',
      payer: {
        payment_method: 'paypal',
        payer_info: {
          email: donorEmail
        }
      },
      redirect_urls: {
        return_url: returnUrl,
        cancel_url: cancelUrl
      },
      transactions: [{
        item_list: {
          items: [{
            name: 'Donation to Cloud Heroes Africa',
            sku: 'donation',
            price: amount.toFixed(2),
            currency: currency,
            quantity: 1
          }]
        },
        amount: {
          currency: currency,
          total: amount.toFixed(2)
        },
        description: `Donation from ${donorName}`
      }]
    };

    paypal.payment.create(create_payment_json, (error, payment) => {
      if (error) {
        console.error('PayPal payment creation error:', error);
        reject(new Error('Failed to create PayPal payment'));
      } else {
        const approvalUrl = payment.links.find(link => link.rel === 'approval_url');
        resolve({
          success: true,
          paymentId: payment.id,
          approvalUrl: approvalUrl ? approvalUrl.href : null
        });
      }
    });
  });
};

// Execute PayPal payment
exports.executePayment = async (paymentId, payerId, donorEmail, donorName) => {
  return new Promise((resolve, reject) => {
    const execute_payment_json = {
      payer_id: payerId
    };

    paypal.payment.execute(paymentId, execute_payment_json, async (error, payment) => {
      if (error) {
        console.error('PayPal payment execution error:', error);
        reject(new Error('Failed to execute PayPal payment'));
      } else {
        // Create donation record
        const transaction = payment.transactions[0];
        const donation = await Donation.create({
          donorEmail: donorEmail,
          donorName: donorName,
          amount: parseFloat(transaction.amount.total),
          currency: transaction.amount.currency,
          paymentMethod: 'paypal',
          paymentStatus: 'completed',
          transactionId: payment.id,
          paymentDetails: {
            paymentId: payment.id,
            payerId: payerId,
            state: payment.state
          }
        });

        resolve({
          success: true,
          donation,
          payment
        });
      }
    });
  });
};

// Get payment details
exports.getPaymentDetails = async (paymentId) => {
  return new Promise((resolve, reject) => {
    paypal.payment.get(paymentId, (error, payment) => {
      if (error) {
        console.error('PayPal get payment error:', error);
        reject(new Error('Failed to get PayPal payment details'));
      } else {
        resolve({
          success: true,
          payment
        });
      }
    });
  });
};

module.exports = exports;
