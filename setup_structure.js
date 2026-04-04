const fs = require('fs');
const path = require('path');

const structure = {
  'src/auth/providers/google': ['oauth_client.py', 'callback_handler.py', 'token_manager.py', '__init__.py'],
  'src/auth/providers/entra': ['msal_config.py', 'enterprise_sso.py', 'conditional_access.py', '__init__.py'],
  'src/auth/mfa/google-mfa': ['enforcement.py', '__init__.py'],
  'src/auth/mfa/ms-authenticator': ['enforcement.py', '__init__.py'],
  'src/auth/mfa/grace-period': ['manager.py', '__init__.py'],
  'src/auth/session': ['session_manager.py', 'timeout_detector.py', 'reauth_trigger.py', '__init__.py'],
  'src/auth/cha': ['continuous_auth.py', 'integrity_validator.py', '__init__.py'],
  'src/roles/student/onboarding': ['invite_validation.py', 'flow.py', '__init__.py'],
  'src/roles/student/permissions': ['rbac.py', '__init__.py'],
  'src/roles/student/error-handlers': ['recovery.py', '__init__.py'],
  'src/roles/administrator/onboarding': ['enrollment.py', 'flow.py', '__init__.py'],
  'src/roles/administrator/permissions': ['rbac.py', '__init__.py'],
  'src/roles/administrator/error-handlers': ['recovery.py', '__init__.py'],
  'src/roles/administrator/pam': ['jit_elevation.py', 'session_recording.py', 'auto_revocation.py', '__init__.py'],
  'src/roles/donor/onboarding': ['donation_form.py', 'flow.py', '__init__.py'],
  'src/roles/donor/permissions': ['rbac.py', '__init__.py'],
  'src/roles/donor/error-handlers': ['recovery.py', '__init__.py'],
  'src/roles/donor/guest-flow': ['guest_donation.py', '__init__.py'],
  'src/roles/volunteer/onboarding': ['vetting.py', 'flow.py', '__init__.py'],
  'src/roles/volunteer/permissions': ['rbac.py', '__init__.py'],
  'src/roles/volunteer/error-handlers': ['recovery.py', '__init__.py'],
  'src/roles/volunteer/class-scope': ['scope_enforcer.py', '__init__.py'],
  'src/platform/community': ['forum.py', 'learning_resources.py', 'impact_dashboard.py', '__init__.py'],
  'src/platform/admin-portal': ['dashboard.py', 'user_management.py', 'role_assignment.py', 'volunteer_vetting.py', 'invite_codes.py', '__init__.py'],
  'src/platform/class-management': ['student_groups.py', 'course_materials.py', '__init__.py'],
  'src/monitoring/audit-log': ['logger.py', 'schema.py', 'storage.py', 'query.py', '__init__.py'],
  'src/monitoring/compliance': ['popia_report.py', 'gdpr_report.py', '__init__.py'],
  'src/monitoring/deprovisioning': ['offboarding.py', 'role_change.py', 'access_cleanup.py', '__init__.py'],
  'infrastructure/identity': ['idp_config.tf', 'mfa_config.tf', 'README.md'],
  'infrastructure/networking': ['api_gateway.tf', 'security_groups.tf', 'README.md'],
  'infrastructure/environments/staging': ['variables.tf', 'terraform.tfvars.example'],
  'infrastructure/environments/production': ['variables.tf', 'terraform.tfvars.example'],
  'config/rbac-policies': ['student.json', 'administrator.json', 'donor.json', 'volunteer.json', 'README.md'],
  'config/session-policies': ['student.json', 'administrator.json', 'donor.json', 'volunteer.json', 'README.md'],
  'config/mfa-policies': ['student.json', 'administrator.json', 'donor.json', 'volunteer.json', 'README.md'],
  'docs': ['architecture.md', 'discovery.md', 'runbooks.md', 'incident_response.md', 'README.md'],
  'scripts': ['access_review.py', 'bulk_provision.py', 'audit_export.py', 'deprovision.py', 'README.md']
};

Object.entries(structure).forEach(([dir, files]) => {
  const fullPath = path.join(__dirname, dir);
  fs.mkdirSync(fullPath, { recursive: true });
  files.forEach(file => {
    fs.writeFileSync(path.join(fullPath, file), '');
  });
});

fs.writeFileSync(path.join(__dirname, 'src/__init__.py'), '');
fs.writeFileSync(path.join(__dirname, 'src/auth/__init__.py'), '');
fs.writeFileSync(path.join(__dirname, 'src/auth/providers/__init__.py'), '');
fs.writeFileSync(path.join(__dirname, 'src/auth/mfa/__init__.py'), '');
fs.writeFileSync(path.join(__dirname, 'src/roles/__init__.py'), '');
fs.writeFileSync(path.join(__dirname, 'src/roles/student/__init__.py'), '');
fs.writeFileSync(path.join(__dirname, 'src/roles/administrator/__init__.py'), '');
fs.writeFileSync(path.join(__dirname, 'src/roles/donor/__init__.py'), '');
fs.writeFileSync(path.join(__dirname, 'src/roles/volunteer/__init__.py'), '');
fs.writeFileSync(path.join(__dirname, 'src/platform/__init__.py'), '');
fs.writeFileSync(path.join(__dirname, 'src/monitoring/__init__.py'), '');
fs.writeFileSync(path.join(__dirname, 'infrastructure/README.md'), '');
fs.writeFileSync(path.join(__dirname, 'infrastructure/environments/README.md'), '');
fs.writeFileSync(path.join(__dirname, 'config/README.md'), '');

console.log('Directory structure created successfully!');
