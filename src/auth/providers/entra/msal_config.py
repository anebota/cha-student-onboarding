"""
Microsoft Entra ID (Azure AD) authentication for Administrators and Volunteers
"""
from flask import Blueprint, redirect, request, session, url_for
import os

entra_bp = Blueprint('entra_auth', __name__)

ENTRA_CLIENT_ID = os.getenv('ENTRA_CLIENT_ID', '')
ENTRA_TENANT_ID = os.getenv('ENTRA_TENANT_ID', '')
ENTRA_CLIENT_SECRET = os.getenv('ENTRA_CLIENT_SECRET', '')
ENTRA_REDIRECT_URI = os.getenv('ENTRA_REDIRECT_URI', 'http://localhost:5000/auth/entra/callback')

AUTHORITY = f"https://login.microsoftonline.com/{ENTRA_TENANT_ID}"
ENTRA_AUTH_URL = f"{AUTHORITY}/oauth2/v2.0/authorize"
ENTRA_TOKEN_URL = f"{AUTHORITY}/oauth2/v2.0/token"

@entra_bp.route('/login')
def login():
    """Initiate Microsoft Entra ID OAuth flow"""
    params = {
        'client_id': ENTRA_CLIENT_ID,
        'redirect_uri': ENTRA_REDIRECT_URI,
        'scope': 'openid email profile User.Read',
        'response_type': 'code',
        'response_mode': 'query'
    }
    auth_url = f"{ENTRA_AUTH_URL}?{'&'.join([f'{k}={v}' for k, v in params.items()])}"
    return redirect(auth_url)

@entra_bp.route('/callback')
def callback():
    """Handle Microsoft Entra ID OAuth callback"""
    code = request.args.get('code')
    
    if not code:
        return "Error: No authorization code received", 400
    
    # For demo purposes, simulate successful authentication
    session['user'] = {
        'email': 'admin@cloudheroes.africa',
        'name': 'Administrator',
        'provider': 'entra',
        'role': 'administrator'
    }
    
    return redirect(url_for('admin_portal.dashboard'))
