@echo off
echo Creating Cloud Heroes Africa directory structure...

REM Create src/auth structure
mkdir src\auth\providers\google 2>nul
mkdir src\auth\providers\entra 2>nul
mkdir src\auth\mfa\google-mfa 2>nul
mkdir src\auth\mfa\ms-authenticator 2>nul
mkdir src\auth\mfa\grace-period 2>nul
mkdir src\auth\session 2>nul
mkdir src\auth\cha 2>nul

REM Create src/roles structure
mkdir src\roles\student\onboarding 2>nul
mkdir src\roles\student\permissions 2>nul
mkdir src\roles\student\error-handlers 2>nul
mkdir src\roles\administrator\onboarding 2>nul
mkdir src\roles\administrator\permissions 2>nul
mkdir src\roles\administrator\error-handlers 2>nul
mkdir src\roles\administrator\pam 2>nul
mkdir src\roles\donor\onboarding 2>nul
mkdir src\roles\donor\permissions 2>nul
mkdir src\roles\donor\error-handlers 2>nul
mkdir src\roles\donor\guest-flow 2>nul
mkdir src\roles\volunteer\onboarding 2>nul
mkdir src\roles\volunteer\permissions 2>nul
mkdir src\roles\volunteer\error-handlers 2>nul
mkdir src\roles\volunteer\class-scope 2>nul

REM Create src/platform structure
mkdir src\platform\community 2>nul
mkdir src\platform\admin-portal 2>nul
mkdir src\platform\class-management 2>nul

REM Create src/monitoring structure
mkdir src\monitoring\audit-log 2>nul
mkdir src\monitoring\compliance 2>nul
mkdir src\monitoring\deprovisioning 2>nul

REM Create infrastructure structure
mkdir infrastructure\identity 2>nul
mkdir infrastructure\networking 2>nul
mkdir infrastructure\environments\staging 2>nul
mkdir infrastructure\environments\production 2>nul

REM Create config structure
mkdir config\rbac-policies 2>nul
mkdir config\session-policies 2>nul
mkdir config\mfa-policies 2>nul

REM Create docs and scripts
mkdir docs 2>nul
mkdir scripts 2>nul

echo Directory structure created successfully!
