#!/bin/bash

echo "Creating Cloud Heroes Africa directory structure..."

# Create all directories
mkdir -p src/auth/providers/google
mkdir -p src/auth/providers/entra
mkdir -p src/auth/mfa/google-mfa
mkdir -p src/auth/mfa/ms-authenticator
mkdir -p src/auth/mfa/grace-period
mkdir -p src/auth/session
mkdir -p src/auth/cha
mkdir -p src/roles/student/onboarding
mkdir -p src/roles/student/permissions
mkdir -p src/roles/student/error-handlers
mkdir -p src/roles/administrator/onboarding
mkdir -p src/roles/administrator/permissions
mkdir -p src/roles/administrator/error-handlers
mkdir -p src/roles/administrator/pam
mkdir -p src/roles/donor/onboarding
mkdir -p src/roles/donor/permissions
mkdir -p src/roles/donor/error-handlers
mkdir -p src/roles/donor/guest-flow
mkdir -p src/roles/volunteer/onboarding
mkdir -p src/roles/volunteer/permissions
mkdir -p src/roles/volunteer/error-handlers
mkdir -p src/roles/volunteer/class-scope
mkdir -p src/platform/community
mkdir -p src/platform/admin-portal
mkdir -p src/platform/class-management
mkdir -p src/monitoring/audit-log
mkdir -p src/monitoring/compliance
mkdir -p src/monitoring/deprovisioning
mkdir -p infrastructure/identity
mkdir -p infrastructure/networking
mkdir -p infrastructure/environments/staging
mkdir -p infrastructure/environments/production
mkdir -p config/rbac-policies
mkdir -p config/session-policies
mkdir -p config/mfa-policies
mkdir -p docs
mkdir -p scripts

echo "Directory structure created successfully!"
