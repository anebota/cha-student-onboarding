"""
Volunteer onboarding flow
"""
from flask import Blueprint, render_template, session, redirect, url_for

volunteer_bp = Blueprint('volunteer_onboarding', __name__)

@volunteer_bp.route('/dashboard')
def dashboard():
    """Volunteer dashboard"""
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('volunteer/dashboard.html', user=session['user'])
