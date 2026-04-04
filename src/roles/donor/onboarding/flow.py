"""
Donor onboarding flow
"""
from flask import Blueprint, render_template, session, redirect, url_for

donor_bp = Blueprint('donor_onboarding', __name__)

@donor_bp.route('/dashboard')
def dashboard():
    """Donor dashboard"""
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('donor/dashboard.html', user=session['user'])
