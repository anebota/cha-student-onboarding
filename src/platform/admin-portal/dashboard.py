"""
Admin portal dashboard
"""
from flask import Blueprint, render_template, session, redirect, url_for

admin_bp = Blueprint('admin_portal', __name__)

@admin_bp.route('/dashboard')
def dashboard():
    """Admin dashboard"""
    if 'user' not in session or session['user'].get('role') != 'administrator':
        return redirect(url_for('login'))
    return render_template('admin/dashboard.html', user=session['user'])

@admin_bp.route('/users')
def users():
    """User management"""
    if 'user' not in session or session['user'].get('role') != 'administrator':
        return redirect(url_for('login'))
    return render_template('admin/users.html', user=session['user'])
