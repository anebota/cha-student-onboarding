const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);
const Donation = require('../../models/Donation');

// Create Stripe checkout session
exports.createCheckoutSession = async (amount, currency, donorEmail, donorName, metadata = {}) => {
  try {
    const session = await stripe.checkout.sessions.create({
      payment_method_types: ['card'],
      line_items: [
        {
          price_data: {
            currency: currency.toLowerCase(),
            product_data: {
              name: 'Donation to Cloud Heroes Africa',
              description: 'Support students learning cloud computing'
            },
            unit_amount: Math.round(amount * 100) // Convert to cents
          },
          quantity: 1
        }
      ],
      mode: 'payment',
      success_url: `${process.env.FRONTEND_URL}/donation/success?session_id={CHECKOUT_SESSION_ID}`,
      cancel_url: `${process.env.FRONTEND_URL}/donation/cancel`,
      customer_email: donorEmail,
      metadata: {
        donorName,
        ...metadata
      }
    });

    return {
      success: true,
      sessionId: session.id,
      url: session.url
    };
  } catch (error) {
    console.error('Stripe checkout error:', error);
    throw new Error('Failed to create Stripe checkout session');
  }
};

// Verify Stripe payment
exports.verifyPayment = async (sessionId) => {
  try {
    const session = await stripe.checkout.sessions.retrieve(sessionId);
    
    if (session.payment_status === 'paid') {
      // Create donation record
      const donation = await Donation.create({
        donorEmail: session.customer_email,
        donorName: session.metadata.donorName,
        amount: session.amount_total / 100,
        currency: session.currency.toUpperCase(),
        paymentMethod: 'stripe',
        paymentStatus: 'completed',
        transactionId: session.payment_intent,
        paymentDetails: {
          sessionId: session.id,
          paymentIntent: session.payment_intent
        }
      });

      return {
        success: true,
        donation
      };
    }

    return {
      success: false,
      message: 'Payment not completed'
    };
  } catch (error) {
    console.error('Stripe verification error:', error);
    throw new Error('Failed to verify Stripe payment');
  }
};

// Handle Stripe webhook
exports.handleWebhook = async (req, res) => {
  const sig = req.headers['stripe-signature'];
  let event;

  try {
    event = stripe.webhooks.constructEvent(
      req.body,
      sig,
      process.env.STRIPE_WEBHOOK_SECRET
    );
  } catch (err) {
    console.error('Webhook signature verification failed:', err.message);
    return res.status(400).send(`Webhook Error: ${err.message}`);
  }

  // Handle the event
  switch (event.type) {
    case 'checkout.session.completed':
      const session = event.data.object;
      await exports.verifyPayment(session.id);
      break;
    case 'payment_intent.succeeded':
      console.log('Payment succeeded:', event.data.object.id);
      break;
    case 'payment_intent.payment_failed':
      console.log('Payment failed:', event.data.object.id);
      break;
    default:
      console.log(`Unhandled event type ${event.type}`);
  }

  res.json({ received: true });
};

module.exports = exports;
