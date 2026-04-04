"""
Community platform - Forum, Learning Resources, Impact Dashboard
"""
from flask import Blueprint, render_template, session, redirect, url_for

community_bp = Blueprint('community', __name__)

@community_bp.route('/')
def index():
    """Community home page"""
    return render_template('community/index.html')

@community_bp.route('/forum')
def forum():
    """Community forum"""
    return render_template('community/forum.html')

@community_bp.route('/resources')
def resources():
    """Learning resources"""
    return render_template('community/resources.html')

@community_bp.route('/impact')
def impact():
    """Impact dashboard"""
    return render_template('community/impact.html')
