
"""
Complete setup script for Cloud Heroes Africa Platform
Creates all directories and template files
"""
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Create directories
print("Creating directories...")
dirs = [
    'templates',
    'templates/student',
    'templates/administrator',
    'templates/donor',
    'templates/volunteer',
    'templates/community',
    'templates/admin',
    'static',
    'static/css',
    'static/js',
    'static/images'
]

for d in dirs:
    os.makedirs(d, exist_ok=True)
    print(f"✓ Created: {d}")

# Template files content
templates = {
    'templates/base.html': '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Cloud Heroes Africa{% endblock %}</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }
        .navbar {
            background: rgba(255, 255, 255, 0.95);
            padding: 1rem 2rem;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .navbar-content {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .logo {
            font-size: 1.5rem;
            font-weight: bold;
            color: #667eea;
        }
        .nav-links a {
            margin-left: 2rem;
            text-decoration: none;
            color: #333;
            font-weight: 500;
            transition: color 0.3s;
        }
        .nav-links a:hover {
            color: #667eea;
        }
        .container {
            max-width: 1200px;
            margin: 2rem auto;
            padding: 0 2rem;
        }
        .btn {
            padding: 0.75rem 1.5rem;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 1rem;
            text-decoration: none;
            display: inline-block;
            transition: all 0.3s;
            font-weight: 500;
        }
        .btn-primary {
            background: #667eea;
            color: white;
        }
        .btn-primary:hover {
            background: #5568d3;
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
        .btn-secondary {
            background: #48bb78;
            color: white;
        }
        .btn-secondary:hover {
            background: #38a169;
            transform: translateY(-2px);
        }
        .card {
            background: white;
            border-radius: 10px;
            padding: 2rem;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            margin-bottom: 2rem;
        }
        .card h1 {
            color: #333;
            margin-bottom: 1rem;
        }
        .card h2 {
            color: #667eea;
            margin-top: 1.5rem;
            margin-bottom: 1rem;
        }
        .card p {
            color: #666;
            line-height: 1.6;
            margin-bottom: 0.5rem;
        }
    </style>
    {% block extra_css %}{% endblock %}
</head>
<body>
    <nav class="navbar">
        <div class="navbar-content">
            <div class="logo">☁️ Cloud Heroes Africa</div>
            <div class="nav-links">
                <a href="/">Home</a>
                <a href="/community">Community</a>
                {% if session.user %}
                    <a href="/logout">Logout</a>
                {% else %}
                    <a href="/login">Login</a>
                {% endif %}
            </div>
        </div>
    </nav>
    
    <div class="container">
        {% block content %}{% endblock %}
    </div>
</body>
</html>''',

    'templates/index.html': '''{% extends "base.html" %}

{% block title %}Home - Cloud Heroes Africa{% endblock %}

{% block content %}
<div class="card">
    <h1>Welcome to Cloud Heroes Africa ☁️</h1>
    <p>Empowering the next generation of cloud professionals across Africa.</p>
    
    <div style="margin-top: 2rem;">
        <h2>Our Mission</h2>
        <p>Cloud Heroes Africa is dedicated to providing world-class cloud computing education and resources to students across the African continent.</p>
    </div>
    
    <div style="margin-top: 2rem;">
        <h2>Get Started</h2>
        <p>Join our community of learners, educators, and supporters.</p>
        <div style="margin-top: 1rem;">
            <a href="/login" class="btn btn-primary">Login</a>
            <a href="/community" class="btn btn-secondary" style="margin-left: 1rem;">Explore Community</a>
        </div>
    </div>
</div>

<div class="card">
    <h2>Four Ways to Participate</h2>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; margin-top: 1rem;">
        <div style="padding: 1rem; background: #f7fafc; border-radius: 5px;">
            <h3 style="color: #667eea;">🎓 Students</h3>
            <p>Access free cloud computing courses and certifications.</p>
        </div>
        <div style="padding: 1rem; background: #f7fafc; border-radius: 5px;">
            <h3 style="color: #667eea;">👨‍💼 Administrators</h3>
            <p>Manage platform operations and user access.</p>
        </div>
        <div style="padding: 1rem; background: #f7fafc; border-radius: 5px;">
            <h3 style="color: #667eea;">💝 Donors</h3>
            <p>Support students with scholarships and resources.</p>
        </div>
        <div style="padding: 1rem; background: #f7fafc; border-radius: 5px;">
            <h3 style="color: #667eea;">🤝 Volunteers</h3>
            <p>Mentor students and contribute to the community.</p>
        </div>
    </div>
</div>
{% endblock %}''',

    'templates/login.html': '''{% extends "base.html" %}

{% block title %}Login - Cloud Heroes Africa{% endblock %}

{% block content %}
<div class="card" style="max-width: 600px; margin: 4rem auto;">
    <h1>Login to Cloud Heroes Africa</h1>
    <p>Choose your login method based on your role.</p>
    
    <div style="margin-top: 2rem;">
        <h2>Students & Donors</h2>
        <p>Login with your Google account</p>
        <a href="/auth/google/login" class="btn btn-primary" style="width: 100%; text-align: center; margin-top: 1rem;">
            🔐 Login with Google
        </a>
    </div>
    
    <div style="margin-top: 2rem; padding-top: 2rem; border-top: 2px solid #e2e8f0;">
        <h2>Administrators & Volunteers</h2>
        <p>Login with your Microsoft account</p>
        <a href="/auth/entra/login" class="btn btn-secondary" style="width: 100%; text-align: center; margin-top: 1rem;">
            🔐 Login with Microsoft
        </a>
    </div>
</div>
{% endblock %}''',

    'templates/student/dashboard.html': '''{% extends "base.html" %}

{% block title %}Student Dashboard - Cloud Heroes Africa{% endblock %}

{% block content %}
<div class="card">
    <h1>Welcome, {{ user.name }}! 🎓</h1>
    <p><strong>Email:</strong> {{ user.email }}</p>
    <p><strong>Role:</strong> Student</p>
    <p><strong>Provider:</strong> {{ user.provider }}</p>
    
    <div style="margin-top: 2rem;">
        <h2>Your Learning Journey</h2>
        <p>Access your courses, resources, and community forums.</p>
        
        <div style="margin-top: 1rem;">
            <a href="/community/forum" class="btn btn-primary">Community Forum</a>
            <a href="/community/resources" class="btn btn-secondary" style="margin-left: 1rem;">Learning Resources</a>
            <a href="/community/impact" class="btn btn-secondary" style="margin-left: 1rem;">Impact Dashboard</a>
        </div>
    </div>
    
    <div style="margin-top: 2rem;">
        <h2>Quick Stats</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin-top: 1rem;">
            <div style="padding: 1rem; background: #f7fafc; border-radius: 5px; text-align: center;">
                <h3 style="color: #667eea; font-size: 2rem;">5</h3>
                <p>Courses Enrolled</p>
            </div>
            <div style="padding: 1rem; background: #f7fafc; border-radius: 5px; text-align: center;">
                <h3 style="color: #48bb78; font-size: 2rem;">3</h3>
                <p>Certifications</p>
            </div>
            <div style="padding: 1rem; background: #f7fafc; border-radius: 5px; text-align: center;">
                <h3 style="color: #ed8936; font-size: 2rem;">85%</h3>
                <p>Progress</p>
            </div>
        </div>
    </div>
</div>
{% endblock %}''',

    'templates/student/onboarding.html': '''{% extends "base.html" %}

{% block title %}Student Onboarding - Cloud Heroes Africa{% endblock %}

{% block content %}
<div class="card">
    <h1>Welcome to Cloud Heroes Africa! 🎓</h1>
    <p>Let's get you started on your cloud learning journey.</p>
    
    <div style="margin-top: 2rem;">
        <h2>Step 1: Complete Your Profile</h2>
        <p>Tell us about yourself and your learning goals.</p>
    </div>
    
    <div style="margin-top: 2rem;">
        <h2>Step 2: Choose Your Learning Path</h2>
        <p>Select the cloud certifications you want to pursue.</p>
    </div>
    
    <div style="margin-top: 2rem;">
        <h2>Step 3: Join the Community</h2>
        <p>Connect with fellow students and mentors.</p>
    </div>
    
    <div style="margin-top: 2rem;">
        <a href="/student/dashboard" class="btn btn-primary">Complete Onboarding</a>
    </div>
</div>
{% endblock %}''',

    'templates/administrator/dashboard.html': '''{% extends "base.html" %}

{% block title %}Administrator Dashboard - Cloud Heroes Africa{% endblock %}

{% block content %}
<div class="card">
    <h1>Administrator Dashboard 👨‍💼</h1>
    <p><strong>Name:</strong> {{ user.name }}</p>
    <p><strong>Email:</strong> {{ user.email }}</p>
    <p><strong>Role:</strong> Administrator</p>
    <p><strong>Provider:</strong> {{ user.provider }}</p>
    
    <div style="margin-top: 2rem;">
        <h2>Platform Management</h2>
        <div style="margin-top: 1rem;">
            <a href="/admin/users" class="btn btn-primary">User Management</a>
            <a href="/admin/roles" class="btn btn-secondary" style="margin-left: 1rem;">Role Assignment</a>
            <a href="/admin/volunteers" class="btn btn-secondary" style="margin-left: 1rem;">Volunteer Vetting</a>
        </div>
    </div>
    
    <div style="margin-top: 2rem;">
        <h2>System Statistics</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin-top: 1rem;">
            <div style="padding: 1rem; background: #f7fafc; border-radius: 5px; text-align: center;">
                <h3 style="color: #667eea; font-size: 2rem;">1,234</h3>
                <p>Total Students</p>
            </div>
            <div style="padding: 1rem; background: #f7fafc; border-radius: 5px; text-align: center;">
                <h3 style="color: #48bb78; font-size: 2rem;">45</h3>
                <p>Active Volunteers</p>
            </div>
            <div style="padding: 1rem; background: #f7fafc; border-radius: 5px; text-align: center;">
                <h3 style="color: #ed8936; font-size: 2rem;">89</h3>
                <p>Donors</p>
            </div>
        </div>
    </div>
</div>
{% endblock %}''',

    'templates/donor/dashboard.html': '''{% extends "base.html" %}

{% block title %}Donor Dashboard - Cloud Heroes Africa{% endblock %}

{% block content %}
<div class="card">
    <h1>Welcome, {{ user.name }}! 💝</h1>
    <p><strong>Email:</strong> {{ user.email }}</p>
    <p><strong>Role:</strong> Donor</p>
    <p><strong>Provider:</strong> {{ user.provider }}</p>
    
    <div style="margin-top: 2rem;">
        <h2>Your Impact</h2>
        <p>See how your contributions are making a difference.</p>
        
        <div style="margin-top: 1rem;">
            <a href="/community/impact" class="btn btn-primary">View Impact Dashboard</a>
            <a href="/donor/donate" class="btn btn-secondary" style="margin-left: 1rem;">Make a Donation</a>
        </div>
    </div>
    
    <div style="margin-top: 2rem;">
        <h2>Donation Summary</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin-top: 1rem;">
            <div style="padding: 1rem; background: #f7fafc; border-radius: 5px; text-align: center;">
                <h3 style="color: #667eea; font-size: 2rem;">$5,000</h3>
                <p>Total Donated</p>
            </div>
            <div style="padding: 1rem; background: #f7fafc; border-radius: 5px; text-align: center;">
                <h3 style="color: #48bb78; font-size: 2rem;">25</h3>
                <p>Students Supported</p>
            </div>
            <div style="padding: 1rem; background: #f7fafc; border-radius: 5px; text-align: center;">
                <h3 style="color: #ed8936; font-size: 2rem;">12</h3>
                <p>Certifications Funded</p>
            </div>
        </div>
    </div>
</div>
{% endblock %}''',

    'templates/volunteer/dashboard.html': '''{% extends "base.html" %}

{% block title %}Volunteer Dashboard - Cloud Heroes Africa{% endblock %}

{% block content %}
<div class="card">
    <h1>Welcome, {{ user.name }}! 🤝</h1>
    <p><strong>Email:</strong> {{ user.email }}</p>
    <p><strong>Role:</strong> Volunteer</p>
    <p><strong>Provider:</strong> {{ user.provider }}</p>
    
    <div style="margin-top: 2rem;">
        <h2>Your Classes</h2>
        <p>Manage your assigned student groups and course materials.</p>
        
        <div style="margin-top: 1rem;">
            <a href="/volunteer/classes" class="btn btn-primary">View Classes</a>
            <a href="/volunteer/students" class="btn btn-secondary" style="margin-left: 1rem;">Student Groups</a>
        </div>
    </div>
    
    <div style="margin-top: 2rem;">
        <h2>Class Statistics</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin-top: 1rem;">
            <div style="padding: 1rem; background: #f7fafc; border-radius: 5px; text-align: center;">
                <h3 style="color: #667eea; font-size: 2rem;">3</h3>
                <p>Classes Assigned</p>
            </div>
            <div style="padding: 1rem; background: #f7fafc; border-radius: 5px; text-align: center;">
                <h3 style="color: #48bb78; font-size: 2rem;">45</h3>
                <p>Students Mentored</p>
            </div>
            <div style="padding: 1rem; background: #f7fafc; border-radius: 5px; text-align: center;">
                <h3 style="color: #ed8936; font-size: 2rem;">92%</h3>
                <p>Completion Rate</p>
            </div>
        </div>
    </div>
</div>
{% endblock %}''',

    'templates/community/index.html': '''{% extends "base.html" %}

{% block title %}Community - Cloud Heroes Africa{% endblock %}

{% block content %}
<div class="card">
    <h1>Cloud Heroes Community 🌍</h1>
    <p>Connect, learn, and grow with fellow cloud enthusiasts across Africa.</p>
    
    <div style="margin-top: 2rem;">
        <h2>Community Features</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; margin-top: 1rem;">
            <div style="padding: 1.5rem; background: #f7fafc; border-radius: 5px;">
                <h3 style="color: #667eea;">💬 Forum</h3>
                <p>Discuss cloud topics, ask questions, and share knowledge.</p>
                <a href="/community/forum" class="btn btn-primary" style="margin-top: 1rem;">Visit Forum</a>
            </div>
            <div style="padding: 1.5rem; background: #f7fafc; border-radius: 5px;">
                <h3 style="color: #48bb78;">📚 Resources</h3>
                <p>Access learning materials, tutorials, and study guides.</p>
                <a href="/community/resources" class="btn btn-secondary" style="margin-top: 1rem;">Browse Resources</a>
            </div>
            <div style="padding: 1.5rem; background: #f7fafc; border-radius: 5px;">
                <h3 style="color: #ed8936;">📊 Impact</h3>
                <p>See the collective impact of our community.</p>
                <a href="/community/impact" class="btn btn-secondary" style="margin-top: 1rem;">View Impact</a>
            </div>
        </div>
    </div>
</div>
{% endblock %}''',

    'templates/community/forum.html': '''{% extends "base.html" %}

{% block title %}Community Forum - Cloud Heroes Africa{% endblock %}

{% block content %}
<div class="card">
    <h1>Community Forum 💬</h1>
    <p>Discuss cloud computing topics with the community.</p>
    
    <div style="margin-top: 2rem;">
        <h2>Popular Topics</h2>
        <div style="margin-top: 1rem;">
            <div style="padding: 1rem; background: #f7fafc; border-radius: 5px; margin-bottom: 1rem;">
                <h3 style="color: #667eea;">AWS Certification Tips</h3>
                <p>Share your experience and tips for AWS certifications.</p>
                <small style="color: #999;">45 replies • Last activity 2 hours ago</small>
            </div>
            <div style="padding: 1rem; background: #f7fafc; border-radius: 5px; margin-bottom: 1rem;">
                <h3 style="color: #667eea;">Azure vs AWS: Which to learn first?</h3>
                <p>Discussion about choosing your first cloud platform.</p>
                <small style="color: #999;">32 replies • Last activity 5 hours ago</small>
            </div>
            <div style="padding: 1rem; background: #f7fafc; border-radius: 5px; margin-bottom: 1rem;">
                <h3 style="color: #667eea;">Study Group Formation</h3>
                <p>Join or create study groups for upcoming certifications.</p>
                <small style="color: #999;">18 replies • Last activity 1 day ago</small>
            </div>
        </div>
    </div>
</div>
{% endblock %}''',

    'templates/community/resources.html': '''{% extends "base.html" %}

{% block title %}Learning Resources - Cloud Heroes Africa{% endblock %}

{% block content %}
<div class="card">
    <h1>Learning Resources 📚</h1>
    <p>Curated resources to help you succeed in your cloud journey.</p>
    
    <div style="margin-top: 2rem;">
        <h2>AWS Resources</h2>
        <ul style="margin-left: 2rem; line-height: 2;">
            <li>AWS Cloud Practitioner Study Guide</li>
            <li>AWS Solutions Architect Practice Tests</li>
            <li>AWS Well-Architected Framework</li>
        </ul>
    </div>
    
    <div style="margin-top: 2rem;">
        <h2>Azure Resources</h2>
        <ul style="margin-left: 2rem; line-height: 2;">
            <li>Azure Fundamentals Learning Path</li>
            <li>Azure Administrator Study Materials</li>
            <li>Azure Architecture Best Practices</li>
        </ul>
    </div>
    
    <div style="margin-top: 2rem;">
        <h2>Google Cloud Resources</h2>
        <ul style="margin-left: 2rem; line-height: 2;">
            <li>GCP Associate Cloud Engineer Guide</li>
            <li>Google Cloud Platform Fundamentals</li>
            <li>GCP Architecture Framework</li>
        </ul>
    </div>
</div>
{% endblock %}''',

    'templates/community/impact.html': '''{% extends "base.html" %}

{% block title %}Impact Dashboard - Cloud Heroes Africa{% endblock %}

{% block content %}
<div class="card">
    <h1>Our Impact 📊</h1>
    <p>See the difference we're making together across Africa.</p>
    
    <div style="margin-top: 2rem;">
        <h2>Community Statistics</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin-top: 1rem;">
            <div style="padding: 1.5rem; background: #f7fafc; border-radius: 5px; text-align: center;">
                <h3 style="color: #667eea; font-size: 2.5rem;">1,234</h3>
                <p><strong>Students Enrolled</strong></p>
            </div>
            <div style="padding: 1.5rem; background: #f7fafc; border-radius: 5px; text-align: center;">
                <h3 style="color: #48bb78; font-size: 2.5rem;">567</h3>
                <p><strong>Certifications Earned</strong></p>
            </div>
            <div style="padding: 1.5rem; background: #f7fafc; border-radius: 5px; text-align: center;">
                <h3 style="color: #ed8936; font-size: 2.5rem;">45</h3>
                <p><strong>Active Volunteers</strong></p>
            </div>
            <div style="padding: 1.5rem; background: #f7fafc; border-radius: 5px; text-align: center;">
                <h3 style="color: #9f7aea; font-size: 2.5rem;">$125K</h3>
                <p><strong>Scholarships Awarded</strong></p>
            </div>
        </div>
    </div>
    
    <div style="margin-top: 2rem;">
        <h2>Countries Reached</h2>
        <p>Our community spans across 15 African countries including South Africa, Nigeria, Kenya, Ghana, and more.</p>
    </div>
</div>
{% endblock %}''',

    'templates/admin/dashboard.html': '''{% extends "base.html" %}

{% block title %}Admin Portal - Cloud Heroes Africa{% endblock %}

{% block content %}
<div class="card">
    <h1>Admin Portal 🔧</h1>
    <p><strong>Administrator:</strong> {{ user.name }}</p>
    
    <div style="margin-top: 2rem;">
        <h2>Management Tools</h2>
        <div style="margin-top: 1rem;">
            <a href="/admin/users" class="btn btn-primary">User Management</a>
            <a href="/admin/roles" class="btn btn-secondary" style="margin-left: 1rem;">Role Assignment</a>
            <a href="/admin/volunteers" class="btn btn-secondary" style="margin-left: 1rem;">Volunteer Vetting</a>
            <a href="/admin/invites" class="btn btn-secondary" style="margin-left: 1rem;">Generate Invite Codes</a>
        </div>
    </div>
</div>
{% endblock %}''',

    'templates/admin/users.html': '''{% extends "base.html" %}

{% block title %}User Management - Cloud Heroes Africa{% endblock %}

{% block content %}
<div class="card">
    <h1>User Management 👥</h1>
    <p>Manage all platform users and their roles.</p>
    
    <div style="margin-top: 2rem;">
        <h2>User List</h2>
        <table style="width: 100%; border-collapse: collapse; margin-top: 1rem;">
            <thead>
                <tr style="background: #f7fafc;">
                    <th style="padding: 1rem; text-align: left; border-bottom: 2px solid #e2e8f0;">Name</th>
                    <th style="padding: 1rem; text-align: left; border-bottom: 2px solid #e2e8f0;">Email</th>
                    <th style="padding: 1rem; text-align: left; border-bottom: 2px solid #e2e8f0;">Role</th>
                    <th style="padding: 1rem; text-align: left; border-bottom: 2px solid #e2e8f0;">Status</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td style="padding: 1rem; border-bottom: 1px solid #e2e8f0;">John Doe</td>
                    <td style="padding: 1rem; border-bottom: 1px solid #e2e8f0;">john@example.com</td>
                    <td style="padding: 1rem; border-bottom: 1px solid #e2e8f0;">Student</td>
                    <td style="padding: 1rem; border-bottom: 1px solid #e2e8f0;"><span style="color: #48bb78;">Active</span></td>
                </tr>
                <tr>
                    <td style="padding: 1rem; border-bottom: 1px solid #e2e8f0;">Jane Smith</td>
                    <td style="padding: 1rem; border-bottom: 1px solid #e2e8f0;">jane@example.com</td>
                    <td style="padding: 1rem; border-bottom: 1px solid #e2e8f0;">Volunteer</td>
                    <td style="padding: 1rem; border-bottom: 1px solid #e2e8f0;"><span style="color: #48bb78;">Active</span></td>
                </tr>
            </tbody>
        </table>
    </div>
</div>
{% endblock %}'''
}

# Create all template files
print("\nCreating template files...")
for filepath, content in templates.items():
    full_path = os.path.join(BASE_DIR, filepath)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✓ Created: {filepath}")

print("\n" + "="*60)
print("✅ Setup complete!")
print("="*60)
print("\nNext steps:")
print("1. Install dependencies: pip install -r requirements.txt")
print("2. Copy .env.template to .env and configure")
print("3. Run the application: python app.py")
print("4. Open browser: http://localhost:5000")
print("\nFor detailed instructions, see SETUP.md")
