# Microsoft Azure AD / Entra ID Setup Guide

This guide provides step-by-step instructions to get Microsoft Azure AD (now Entra ID) OAuth credentials for the Cloud Heroes Africa backend.

---

## Prerequisites
- Microsoft account
- Access to [Azure Portal](https://portal.azure.com/)
- Admin access to create app registrations (or contact your Azure admin)

---

## Step 1: Go to Azure Portal
1. Open [Azure Portal](https://portal.azure.com/)
2. Sign in with your Microsoft account
3. If you don't have an Azure subscription, create a free one:
   - Click **"Create a resource"**
   - Search for **"Azure Pass"** or **"Free Account"**
   - Follow the setup wizard

---

## Step 2: Access Azure AD / Entra ID

### Method A: Using Search Bar
1. In the top search bar, search for **"Azure AD"** or **"Entra ID"**
2. Click on **"Azure Active Directory"** or **"Microsoft Entra ID"**

### Method B: Using Left Sidebar
1. Click the **hamburger menu** (☰) at the top left
2. Go to **Identity** → **Azure Active Directory** (or **Microsoft Entra ID**)

---

## Step 3: Register a New Application

1. In the left sidebar, click **"App registrations"**
2. Click **"+ New registration"**
3. Fill in the form:

| Field | Value |
|-------|-------|
| **Name** | `Cloud Heroes Africa Backend` |
| **Supported account types** | `Accounts in any organizational directory (Any Azure AD directory - Multitenant)` |
| **Redirect URI (optional)** | - |

4. Click **"Register"**

---

## Step 4: Configure Redirect URI

After registration, you'll see your app details:

1. In the left sidebar, click **"Authentication"**
2. Scroll to **"Web"** section
3. Click **"+ Add a URI"**
4. Paste: `http://localhost:5000/api/auth/azure/callback`
5. Click **"Save"**

---

## Step 5: Get Your Credentials

### Step 5a: Copy Client ID (Application ID)
1. Go back to the **Overview** tab
2. Copy the **"Application (client) ID"**
3. Save this value - it's your `AZURE_CLIENT_ID`

### Step 5b: Copy Tenant ID (Directory ID)
1. Still on the **Overview** tab
2. Copy the **"Directory (tenant) ID"**
3. Save this value - it's your `AZURE_TENANT_ID`

### Step 5c: Create Client Secret
1. In the left sidebar, click **"Certificates & secrets"**
2. Click the **"Client secrets"** tab
3. Click **"+ New client secret"**
4. Give it a description: `Cloud Heroes Development`
5. Set expiration: **24 months** (recommended for development)
6. Click **"Add"**
7. **Immediately copy the "Value"** (not the ID!) - this is your `AZURE_CLIENT_SECRET`

**⚠️ WARNING:** The secret value only appears once! Copy it immediately.

---

## Step 6: Get Tenant ID (Alternative Method)

If you need the tenant ID later:

1. Go to **Azure AD** → **Overview**
2. Look for **"Directory (tenant) ID"** or **"Tenant ID"**
3. Click on it to copy
4. Or construct it from the URL format:
   ```
   https://login.microsoftonline.com/{tenant-id}/v2.0/.well-known/openid-configuration
   ```

---

## Step 7: Configure API Permissions (Optional but Recommended)

1. In the left sidebar, click **"API permissions"**
2. Click **"+ Add a permission"**
3. Select **"Microsoft Graph"**
4. Choose **"Delegated permissions"**
5. Search for and select:
   - `openid`
   - `profile`
   - `email`
6. Click **"Add permissions"**
7. Click **"Grant admin consent for [Your Organization]"** (if you have admin access)

---

## Step 8: Update Your .env File

1. Open [`backend/.env`](backend/.env)
2. Find the **MICROSOFT ENTRA ID / AZURE AD** section
3. Replace the placeholder values:

```dotenv
# MICROSOFT ENTRA ID / AZURE AD (Administrators & Volunteers)
AZURE_CLIENT_ID=<your_azure_client_id>
AZURE_TENANT_ID=<your_azure_tenant_id>
AZURE_CLIENT_SECRET=<your_azure_client_secret>
AZURE_CALLBACK_URL=http://localhost:5000/api/auth/azure/callback
```

### Example:
```dotenv
AZURE_CLIENT_ID=a1b2c3d4-e5f6-7g8h-9i10-j11k12l13m14
AZURE_TENANT_ID=f1e2d3c4-b5a6-7890-1234-567890abcdef
AZURE_CLIENT_SECRET=ABC123~XYZ_abc123xyz.def456
AZURE_CALLBACK_URL=http://localhost:5000/api/auth/azure/callback
```

4. **Save the .env file**

---

## Step 9: Verify Configuration in Backend Code

The backend uses the `OIDCStrategy` for Azure. Check [backend/src/routes/auth.routes.js](backend/src/routes/auth.routes.js) to ensure it's configured correctly:

```javascript
const AzureStrategy = require('passport-azure-ad').OIDCStrategy;

passport.use(new AzureStrategy({
    identityMetadata: `https://login.microsoftonline.com/${process.env.AZURE_TENANT_ID}/v2.0/.well-known/openid-configuration`,
    clientID: process.env.AZURE_CLIENT_ID,
    clientSecret: process.env.AZURE_CLIENT_SECRET,
    callbackURL: process.env.AZURE_CALLBACK_URL,
    responseType: 'code id_token',
    responseMode: 'form_post'
  },
  async (iss, sub, profile, accessToken, refreshToken, done) => {
    // Profile handling...
  }
));
```

---

## Step 10: Restart Your Backend

```bash
npm start
```

You should now see:
```
✅ MongoDB Connected
🚀 Server running on port 5000
```

**Without the Azure authentication errors!** ✅

---

## Testing Azure OAuth Flow

1. Start your frontend (in another terminal):
   ```bash
   cd frontend
   npm run dev
   ```

2. Navigate to your application and click **"Login with Microsoft"**

3. You'll be redirected to Microsoft login

4. Sign in with your Azure AD account

5. You should be redirected back and logged in

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `AADSTS900144: The request body must contain the following parameter: 'client_id'` | Verify `AZURE_CLIENT_ID` is set correctly in `.env` |
| `AADSTS700016: Application with identifier 'xxx' was not found in the directory` | Check that your `AZURE_CLIENT_ID` is correct |
| `Invalid redirect URI` | Ensure `AZURE_CALLBACK_URL` in `.env` matches the registered redirect URI in Azure Portal |
| `Client secret has expired` | Go to **Certificates & secrets** and create a new client secret |
| Can't see app registration | Make sure you're in the correct Azure AD directory |
| Permission denied errors | Check **API permissions** and grant admin consent if needed |

---

## Production Deployment

When deploying to production, update these URLs:

1. **In Azure Portal:**
   - Go to **Authentication** → **Web**
   - Add your production redirect URI:
     ```
     https://yourdomain.com/api/auth/azure/callback
     ```

2. **In Production .env:**
   ```dotenv
   AZURE_CALLBACK_URL=https://yourdomain.com/api/auth/azure/callback
   ```

3. **Create a new client secret** for production (don't reuse development secret)

---

## Supported User Types

The current setup supports:
- ✅ **Administrators** - Log in with Azure AD
- ✅ **Volunteers** - Log in with Azure AD
- ⚠️ **Students & Donors** - Use Google OAuth instead

You can modify the backend to support additional roles by editing [backend/src/routes/auth.routes.js](backend/src/routes/auth.routes.js)

---

## Additional Resources

- [Microsoft Entra ID Documentation](https://learn.microsoft.com/en-us/entra/)
- [Azure Portal](https://portal.azure.com/)
- [Passport.js Azure AD Strategy](http://www.passportjs.org/packages/passport-azure-ad/)
- [OAuth 2.0 Authorization Code Flow](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-auth-code-flow)
- [Tenant and Directory Terms](https://learn.microsoft.com/en-us/entra/fundamentals/how-subscriptions-associated-directory)

---

## ✅ Setup Complete!

Your Microsoft Azure AD / Entra ID OAuth is now configured and ready to use. Users can now:
- Sign up with Microsoft / Azure AD
- Log in with Microsoft / Azure AD
- Have their profile automatically created as Admin or Volunteer

Happy coding! 🚀
