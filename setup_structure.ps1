$dirs = @(
    "src\auth\providers\google",
    "src\auth\providers\entra",
    "src\auth\mfa\google-mfa",
    "src\auth\mfa\ms-authenticator",
    "src\auth\mfa\grace-period",
    "src\auth\session",
    "src\auth\cha",
    "src\roles\student\onboarding",
    "src\roles\student\permissions",
    "src\roles\student\error-handlers",
    "src\roles\administrator\onboarding",
    "src\roles\administrator\permissions",
    "src\roles\administrator\error-handlers",
    "src\roles\administrator\pam",
    "src\roles\donor\onboarding",
    "src\roles\donor\permissions",
    "src\roles\donor\error-handlers",
    "src\roles\donor\guest-flow",
    "src\roles\volunteer\onboarding",
    "src\roles\volunteer\permissions",
    "src\roles\volunteer\error-handlers",
    "src\roles\volunteer\class-scope",
    "src\platform\community",
    "src\platform\admin-portal",
    "src\platform\class-management",
    "src\monitoring\audit-log",
    "src\monitoring\compliance",
    "src\monitoring\deprovisioning",
    "infrastructure\identity",
    "infrastructure\networking",
    "infrastructure\environments\staging",
    "infrastructure\environments\production",
    "config\rbac-policies",
    "config\session-policies",
    "config\mfa-policies",
    "docs",
    "scripts"
)

foreach ($dir in $dirs) {
    New-Item -ItemType Directory -Force -Path $dir | Out-Null
}

Write-Host "Directory structure created successfully!"
