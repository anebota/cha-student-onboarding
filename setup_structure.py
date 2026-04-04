"""
Setup script to create Cloud Heroes Africa directory structure
"""
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

STRUCTURE = {
    'src': {
        'auth': {
            'providers': {
                'google': ['oauth_client.py', 'callback_handler.py', 'token_manager.py', '__init__.py'],
                'entra': ['msal_config.py', 'enterprise_sso.py', 'conditional_access.py', '__init__.py'],
                '__init__.py': None
            },
            'mfa': {
                'google-mfa': ['enforcement.py', '__init__.py'],
                'ms-authenticator': ['enforcement.py', '__init__.py'],
                'grace-period': ['manager.py', '__init__.py'],
                '__init__.py': None
            },
            'session': ['session_manager.py', 'timeout_detector.py', 'reauth_trigger.py', '__init__.py'],
            'cha': ['continuous_auth.py', 'integrity_validator.py', '__init__.py'],
            '__init__.py': None
        },
        'roles': {
            'student': {
                'onboarding': ['invite_validation.py', 'flow.py', '__init__.py'],
                'permissions': ['rbac.py', '__init__.py'],
                'error-handlers': ['recovery.py', '__init__.py'],
                '__init__.py': None
            },
            'administrator': {
                'onboarding': ['enrollment.py', 'flow.py', '__init__.py'],
                'permissions': ['rbac.py', '__init__.py'],
                'error-handlers': ['recovery.py', '__init__.py'],
                'pam': ['jit_elevation.py', 'session_recording.py', 'auto_revocation.py', '__init__.py'],
                '__init__.py': None
            },
            'donor': {
                'onboarding': ['donation_form.py', 'flow.py', '__init__.py'],
                'permissions': ['rbac.py', '__init__.py'],
                'error-handlers': ['recovery.py', '__init__.py'],
                'guest-flow': ['guest_donation.py', '__init__.py'],
                '__init__.py': None
            },
            'volunteer': {
                'onboarding': ['vetting.py', 'flow.py', '__init__.py'],
                'permissions': ['rbac.py', '__init__.py'],
                'error-handlers': ['recovery.py', '__init__.py'],
                'class-scope': ['scope_enforcer.py', '__init__.py'],
                '__init__.py': None
            },
            '__init__.py': None
        },
        'platform': {
            'community': ['forum.py', 'learning_resources.py', 'impact_dashboard.py', '__init__.py'],
            'admin-portal': ['dashboard.py', 'user_management.py', 'role_assignment.py', 'volunteer_vetting.py', 'invite_codes.py', '__init__.py'],
            'class-management': ['student_groups.py', 'course_materials.py', '__init__.py'],
            '__init__.py': None
        },
        'monitoring': {
            'audit-log': ['logger.py', 'schema.py', 'storage.py', 'query.py', '__init__.py'],
            'compliance': ['popia_report.py', 'gdpr_report.py', '__init__.py'],
            'deprovisioning': ['offboarding.py', 'role_change.py', 'access_cleanup.py', '__init__.py'],
            '__init__.py': None
        },
        '__init__.py': None
    },
    'infrastructure': {
        'identity': ['idp_config.tf', 'mfa_config.tf', 'README.md'],
        'networking': ['api_gateway.tf', 'security_groups.tf', 'README.md'],
        'environments': {
            'staging': ['variables.tf', 'terraform.tfvars.example'],
            'production': ['variables.tf', 'terraform.tfvars.example'],
            'README.md': None
        },
        'README.md': None
    },
    'config': {
        'rbac-policies': ['student.json', 'administrator.json', 'donor.json', 'volunteer.json', 'README.md'],
        'session-policies': ['student.json', 'administrator.json', 'donor.json', 'volunteer.json', 'README.md'],
        'mfa-policies': ['student.json', 'administrator.json', 'donor.json', 'volunteer.json', 'README.md'],
        'README.md': None
    },
    'docs': ['architecture.md', 'discovery.md', 'runbooks.md', 'incident_response.md', 'README.md'],
    'scripts': ['access_review.py', 'bulk_provision.py', 'audit_export.py', 'deprovision.py', 'README.md']
}

def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        elif isinstance(content, list):
            os.makedirs(path, exist_ok=True)
            for file in content:
                file_path = os.path.join(path, file)
                if not os.path.exists(file_path):
                    with open(file_path, 'w') as f:
                        f.write('')
        elif content is None:
            if not os.path.exists(path):
                with open(path, 'w') as f:
                    f.write('')

if __name__ == '__main__':
    create_structure(BASE_DIR, STRUCTURE)
    print('Directory structure created successfully!')
