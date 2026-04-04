"""
Administrator onboarding flow
"""
from flask import Blueprint, render_template, session, redirect, url_for

administrator_bp = Blueprint('administrator_onboarding', __name__)

@administrator_bp.route('/dashboard')
def dashboard():
    """Administrator dashboard"""
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('administrator/dashboard.html', user=session['user'])
