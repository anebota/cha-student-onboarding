"""
Student onboarding flow
"""
from flask import Blueprint, render_template, session, redirect, url_for

student_bp = Blueprint('student_onboarding', __name__)

@student_bp.route('/dashboard')
def dashboard():
    """Student dashboard"""
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('student/dashboard.html', user=session['user'])

@student_bp.route('/onboarding')
def onboarding():
    """Student onboarding process"""
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('student/onboarding.html', user=session['user'])
