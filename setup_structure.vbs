Set fso = CreateObject("Scripting.FileSystemObject")
Set shell = CreateObject("WScript.Shell")
currentDir = shell.CurrentDirectory

dirs = Array( _
    "src\auth\providers\google", _
    "src\auth\providers\entra", _
    "src\auth\mfa\google-mfa", _
    "src\auth\mfa\ms-authenticator", _
    "src\auth\mfa\grace-period", _
    "src\auth\session", _
    "src\auth\cha", _
    "src\roles\student\onboarding", _
    "src\roles\student\permissions", _
    "src\roles\student\error-handlers", _
    "src\roles\administrator\onboarding", _
    "src\roles\administrator\permissions", _
    "src\roles\administrator\error-handlers", _
    "src\roles\administrator\pam", _
    "src\roles\donor\onboarding", _
    "src\roles\donor\permissions", _
    "src\roles\donor\error-handlers", _
    "src\roles\donor\guest-flow", _
    "src\roles\volunteer\onboarding", _
    "src\roles\volunteer\permissions", _
    "src\roles\volunteer\error-handlers", _
    "src\roles\volunteer\class-scope", _
    "src\platform\community", _
    "src\platform\admin-portal", _
    "src\platform\class-management", _
    "src\monitoring\audit-log", _
    "src\monitoring\compliance", _
    "src\monitoring\deprovisioning", _
    "infrastructure\identity", _
    "infrastructure\networking", _
    "infrastructure\environments\staging", _
    "infrastructure\environments\production", _
    "config\rbac-policies", _
    "config\session-policies", _
    "config\mfa-policies", _
    "docs", _
    "scripts" _
)

For Each dir In dirs
    fullPath = currentDir & "\" & dir
    If Not fso.FolderExists(fullPath) Then
        CreatePath fullPath
    End If
Next

WScript.Echo "Directory structure created successfully!"

Sub CreatePath(path)
    parts = Split(path, "\")
    current = ""
    For i = 0 To UBound(parts)
        If i = 0 Then
            current = parts(i)
        Else
            current = current & "\" & parts(i)
        End If
        If Not fso.FolderExists(current) Then
            fso.CreateFolder(current)
        End If
    Next
End Sub
