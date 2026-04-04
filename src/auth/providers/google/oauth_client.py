"""
Google OAuth 2.0 Client for Students and Donors
"""
from flask import Blueprint, redirect, request, session, url_for
import requests
import os

google_bp = Blueprint('google_auth', __name__)

GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID', '')
GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET', '')
GOOGLE_REDIRECT_URI = os.getenv('GOOGLE_REDIRECT_URI', 'http://localhost:5000/auth/google/callback')

GOOGLE_DISCOVERY_URL = "https://accounts.google.com/.well-known/openid-configuration"
GOOGLE_AUTH_URL = "https://accounts.google.com/o/oauth2/v2/auth"
GOOGLE_TOKEN_URL = "https://oauth2.googleapis.com/token"
GOOGLE_USERINFO_URL = "https://www.googleapis.com/oauth2/v2/userinfo"

@google_bp.route('/login')
def login():
    """Initiate Google OAuth flow"""
    params = {
        'client_id': GOOGLE_CLIENT_ID,
        'redirect_uri': GOOGLE_REDIRECT_URI,
        'scope': 'openid email profile',
        'response_type': 'code',
        'access_type': 'offline',
        'prompt': 'consent'
    }
    auth_url = f"{GOOGLE_AUTH_URL}?{'&'.join([f'{k}={v}' for k, v in params.items()])}"
    return redirect(auth_url)

@google_bp.route('/callback')
def callback():
    """Handle Google OAuth callback"""
    code = request.args.get('code')
    
    if not code:
        return "Error: No authorization code received", 400
    
    # Exchange code for token
    token_data = {
        'code': code,
        'client_id': GOOGLE_CLIENT_ID,
        'client_secret': GOOGLE_CLIENT_SECRET,
        'redirect_uri': GOOGLE_REDIRECT_URI,
        'grant_type': 'authorization_code'
    }
    
    token_response = requests.post(GOOGLE_TOKEN_URL, data=token_data)
    tokens = token_response.json()
    
    if 'access_token' not in tokens:
        return "Error: Failed to obtain access token", 400
    
    # Get user info
    headers = {'Authorization': f"Bearer {tokens['access_token']}"}
    userinfo_response = requests.get(GOOGLE_USERINFO_URL, headers=headers)
    user_info = userinfo_response.json()
    
    # Store in session
    session['user'] = {
        'email': user_info.get('email'),
        'name': user_info.get('name'),
        'picture': user_info.get('picture'),
        'provider': 'google',
        'role': 'student'  # Default role, can be determined by logic
    }
    
    return redirect(url_for('student_onboarding.dashboard'))
