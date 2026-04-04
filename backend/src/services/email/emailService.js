const nodemailer = require('nodemailer');

// Create transporter with Gmail
const transporter = nodemailer.createTransport({
  host: process.env.EMAIL_HOST || 'smtp.gmail.com',
  port: parseInt(process.env.EMAIL_PORT) || 587,
  secure: false, // true for 465, false for other ports
  auth: {
    user: process.env.EMAIL_USER,
    pass: process.env.EMAIL_PASSWORD // Gmail App Password
  }
});

// Verify transporter configuration
transporter.verify((error, success) => {
  if (error) {
    console.error('❌ Email service error:', error);
  } else {
    console.log('✅ Email service ready');
  }
});

// Send email
exports.sendEmail = async (to, subject, html, text) => {
  try {
    const mailOptions = {
      from: process.env.EMAIL_FROM || 'Cloud Heroes Africa <noreply@cloudheroes.africa>',
      to,
      subject,
      text,
      html
    };

    const info = await transporter.sendMail(mailOptions);
    
    console.log('Email sent:', info.messageId);
    return {
      success: true,
      messageId: info.messageId
    };
  } catch (error) {
    console.error('Email sending error:', error);
    throw new Error('Failed to send email');
  }
};

// Send welcome email
exports.sendWelcomeEmail = async (user) => {
  const subject = 'Welcome to Cloud Heroes Africa! ☁️';
  const html = `
    <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
      <h1 style="color: #667eea;">Welcome to Cloud Heroes Africa!</h1>
      <p>Hi ${user.name},</p>
      <p>Thank you for joining Cloud Heroes Africa. We're excited to have you as part of our community!</p>
      <p><strong>Your Role:</strong> ${user.role.charAt(0).toUpperCase() + user.role.slice(1)}</p>
      <p>Get started by exploring your dashboard and connecting with the community.</p>
      <a href="${process.env.FRONTEND_URL}/dashboard" style="display: inline-block; padding: 12px 24px; background: #667eea; color: white; text-decoration: none; border-radius: 5px; margin: 20px 0;">Go to Dashboard</a>
      <p>Best regards,<br>Cloud Heroes Africa Team</p>
    </div>
  `;
  const text = `Welcome to Cloud Heroes Africa! Hi ${user.name}, thank you for joining us.`;

  return await exports.sendEmail(user.email, subject, html, text);
};

// Send donation receipt
exports.sendDonationReceipt = async (donation) => {
  const subject = 'Thank You for Your Donation! 💝';
  const html = `
    <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
      <h1 style="color: #48bb78;">Thank You for Your Donation!</h1>
      <p>Dear ${donation.donorName},</p>
      <p>Thank you for your generous donation to Cloud Heroes Africa. Your support helps students across Africa access quality cloud computing education.</p>
      <div style="background: #f7fafc; padding: 20px; border-radius: 5px; margin: 20px 0;">
        <h3 style="margin-top: 0;">Donation Details</h3>
        <p><strong>Amount:</strong> ${donation.amount} ${donation.currency}</p>
        <p><strong>Date:</strong> ${new Date(donation.createdAt).toLocaleDateString()}</p>
        <p><strong>Transaction ID:</strong> ${donation.transactionId}</p>
        <p><strong>Payment Method:</strong> ${donation.paymentMethod.toUpperCase()}</p>
      </div>
      <p>Your donation is making a real difference in the lives of aspiring cloud professionals.</p>
      <p>Best regards,<br>Cloud Heroes Africa Team</p>
    </div>
  `;
  const text = `Thank you for your donation of ${donation.amount} ${donation.currency} to Cloud Heroes Africa.`;

  return await exports.sendEmail(donation.donorEmail, subject, html, text);
};

// Send MFA code
exports.sendMFACode = async (email, code, name) => {
  const subject = 'Your MFA Verification Code';
  const html = `
    <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
      <h1 style="color: #667eea;">MFA Verification Code</h1>
      <p>Hi ${name},</p>
      <p>Your verification code is:</p>
      <div style="background: #f7fafc; padding: 20px; border-radius: 5px; margin: 20px 0; text-align: center;">
        <h2 style="color: #667eea; font-size: 32px; letter-spacing: 5px; margin: 0;">${code}</h2>
      </div>
      <p>This code will expire in 10 minutes.</p>
      <p>If you didn't request this code, please ignore this email.</p>
      <p>Best regards,<br>Cloud Heroes Africa Team</p>
    </div>
  `;
  const text = `Your MFA verification code is: ${code}. This code will expire in 10 minutes.`;

  return await exports.sendEmail(email, subject, html, text);
};

// Send password reset email
exports.sendPasswordResetEmail = async (email, resetToken, name) => {
  const resetUrl = `${process.env.FRONTEND_URL}/reset-password?token=${resetToken}`;
  const subject = 'Password Reset Request';
  const html = `
    <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
      <h1 style="color: #667eea;">Password Reset Request</h1>
      <p>Hi ${name},</p>
      <p>You requested to reset your password. Click the button below to reset it:</p>
      <a href="${resetUrl}" style="display: inline-block; padding: 12px 24px; background: #667eea; color: white; text-decoration: none; border-radius: 5px; margin: 20px 0;">Reset Password</a>
      <p>This link will expire in 1 hour.</p>
      <p>If you didn't request this, please ignore this email.</p>
      <p>Best regards,<br>Cloud Heroes Africa Team</p>
    </div>
  `;
  const text = `Reset your password by visiting: ${resetUrl}. This link will expire in 1 hour.`;

  return await exports.sendEmail(email, subject, html, text);
};

module.exports = exports;
