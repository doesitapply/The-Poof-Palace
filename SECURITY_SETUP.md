# 🔒 The Poof Palace - Security Setup Guide

## Overview

This guide will help you set up a secure environment for The Poof Palace Autonomous Engine, protecting all your API keys and sensitive information.

## 🛡️ Security Architecture

The Poof Palace uses a multi-layered security approach:

1. **Environment Variables**: All secrets stored in `.env` files
2. **Git Protection**: `.gitignore` prevents accidental commits of sensitive files
3. **Secure Config Loader**: Validates and safely loads configuration
4. **Masked Logging**: Sensitive data is never logged in plain text

## 🚀 Quick Setup

### Step 1: Create Your Environment File

```bash
# Copy the template to create your secure environment file
cp secrets_template.env .env
```

### Step 2: Add Your API Keys

Edit the `.env` file and replace the placeholder values with your actual API keys:

```bash
# Example .env file
GEMINI_API_KEY=AIzaSyATLPVRkr2WFPjNFSqE0Q8MFJsAcdkTXDU
GOOGLE_CLOUD_PROJECT_ID=your-actual-project-id
INSTAGRAM_ACCESS_TOKEN=your_actual_instagram_token
# ... etc
```

### Step 3: Verify Security

```bash
# Test the secure configuration
cd the_poof_palace
python -m modules.secure_config
```

## 📋 Required API Keys

### Google Cloud Services
- **GEMINI_API_KEY**: From [Google AI Studio](https://aistudio.google.com/)
- **GOOGLE_CLOUD_PROJECT_ID**: Your Google Cloud Project ID
- **GOOGLE_CLOUD_LOCATION**: Region (e.g., us-central1)

### Social Media APIs
- **INSTAGRAM_ACCESS_TOKEN**: From [Meta Developer Dashboard](https://developers.facebook.com/)
- **INSTAGRAM_USER_ID**: Your Instagram Business Account ID
- **TWITTER_API_KEY**: From [Twitter Developer Portal](https://developer.twitter.com/)
- **TIKTOK_ACCESS_TOKEN**: From [TikTok Developer Portal](https://developers.tiktok.com/)

### E-commerce (Future Features)
- **SHOPIFY_API_KEY**: From your Shopify Partner Dashboard
- **PRINTFUL_API_KEY**: From Printful API settings

## 🔐 Security Best Practices

### ✅ DO:
- Keep your `.env` file local and never commit it
- Use different API keys for development and production
- Regularly rotate your API keys
- Use environment-specific configurations
- Monitor API usage and set up alerts

### ❌ DON'T:
- Commit `.env` files to version control
- Share API keys in chat messages or emails
- Use production keys in development
- Hardcode secrets in your code
- Log sensitive information in plain text

## 🏗️ File Structure

```
the_poof_palace/
├── .env                          # 🔒 Your secrets (NEVER commit)
├── secrets_template.env          # 📋 Template for setup
├── .gitignore                    # 🛡️ Protects sensitive files
├── config.yaml                   # ⚙️ Non-sensitive configuration
├── modules/
│   ├── secure_config.py          # 🔐 Secure configuration loader
│   └── ...
└── SECURITY_SETUP.md             # 📖 This guide
```

## 🧪 Testing Your Setup

### Test 1: Configuration Loading
```bash
python -m modules.secure_config
```

Expected output:
```
✅ Loaded environment variables from .env
✅ Loaded configuration from config.yaml
🔐 Loaded GEMINI_API_KEY from environment variable
✅ All required secrets validated successfully
```

### Test 2: Security Validation
```bash
# This should fail if secrets are missing
python -c "
from modules.secure_config import load_secure_config
config = load_secure_config()
print('✅ Security setup is working!')
"
```

## 🚨 Troubleshooting

### "Missing required secrets" Error
- Check that your `.env` file exists
- Verify all required API keys are filled in
- Ensure no placeholder values remain

### "File not found" Error
- Make sure you're running from the correct directory
- Check that `config.yaml` exists
- Verify the `.env` file is in the right location

### API Key Validation Errors
- Test your API keys individually
- Check API key permissions and quotas
- Verify the keys are for the correct services

## 🔄 Environment Management

### Development Environment
```bash
# .env.development
ENVIRONMENT=development
DEBUG_MODE=true
GEMINI_API_KEY=your_dev_key_here
```

### Production Environment
```bash
# .env.production
ENVIRONMENT=production
DEBUG_MODE=false
GEMINI_API_KEY=your_prod_key_here
```

## 📊 Monitoring and Alerts

### API Usage Monitoring
- Set up Google Cloud monitoring for API quotas
- Monitor Instagram API rate limits
- Track Twitter API usage

### Security Alerts
- Set up alerts for unusual API usage
- Monitor for failed authentication attempts
- Track configuration changes

## 🆘 Emergency Procedures

### If API Keys Are Compromised
1. Immediately revoke the compromised keys
2. Generate new API keys from the respective platforms
3. Update your `.env` file with new keys
4. Test the system with new keys
5. Monitor for any unauthorized usage

### If Configuration Is Corrupted
1. Restore from `secrets_template.env`
2. Re-enter your API keys
3. Test the configuration
4. Check logs for any issues

## 📞 Support

If you encounter issues with the security setup:

1. Check this guide first
2. Verify your API keys are correct
3. Test with the provided validation scripts
4. Check the logs for specific error messages

## 🎯 Next Steps

Once your security setup is complete:

1. **Test the Google Cloud Integration**: Verify Gemini and Vertex AI access
2. **Test Social Media APIs**: Ensure posting functionality works
3. **Set up Monitoring**: Configure alerts and usage tracking
4. **Deploy Securely**: Use environment-specific configurations

---

**Remember**: Security is an ongoing process. Regularly review and update your security practices as The Poof Palace grows! 👑🐱
