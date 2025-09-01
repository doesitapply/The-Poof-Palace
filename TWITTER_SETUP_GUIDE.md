# 🐦 Twitter API Setup Guide for The Poof Palace

## 🎯 Overview
This guide will help you set up Twitter API v2 integration for The Poof Palace autonomous content engine.

## 📋 Prerequisites
- Twitter Developer Account
- Twitter App with API v2 access
- Read and Write permissions

## 🚀 Step-by-Step Setup

### 1. Create Twitter Developer Account
1. Go to [Twitter Developer Portal](https://developer.twitter.com/en/portal/dashboard)
2. Sign in with your Twitter account
3. Apply for a developer account (usually approved quickly)

### 2. Create a New App
1. In the Developer Portal, click "Create App"
2. Fill in the required information:
   - **App Name**: "The Poof Palace"
   - **App Description**: "Autonomous content generation for The Poof Palace brand"
   - **Website URL**: Your website (or placeholder)
   - **Callback URL**: Leave blank for now

### 3. Get API Credentials
1. Go to your app's "Keys and Tokens" tab
2. You'll need these 4 credentials:
   - **API Key** (Consumer Key)
   - **API Secret Key** (Consumer Secret)
   - **Access Token**
   - **Access Token Secret**

### 4. Enable API v2 Access
1. In your app settings, ensure you have:
   - **Read and Write** permissions
   - **API v2** access enabled
2. You may need to upgrade to Basic or Pro plan for full API v2 access

### 5. Update Configuration
Replace the placeholder values in `config.yaml`:

```yaml
# Twitter API v2 credentials (from Twitter Developer Portal)
TWITTER_API_KEY: "your_actual_api_key_here"
TWITTER_API_SECRET: "your_actual_api_secret_here"
TWITTER_ACCESS_TOKEN: "your_actual_access_token_here"
TWITTER_ACCESS_SECRET: "your_actual_access_token_secret_here"
```

## 🧪 Testing the Integration

### Test with Mock Mode (Current)
```bash
source venv/bin/activate
python -c "
import yaml
from modules.api_clients import TwitterClient
config = yaml.safe_load(open('config.yaml'))
twitter = TwitterClient(config)
result = twitter.post_tweet('Test tweet from The Poof Palace! 👑🐱')
print(f'Result: {result}')
"
```

### Test with Real Credentials
Once you've added your real credentials, the same test will post to Twitter!

## 🔧 Features Implemented

✅ **Twitter API v2 Integration**
✅ **Bearer Token Authentication**
✅ **Text-Only Tweets**
✅ **Media Upload Support** (placeholder)
✅ **Error Handling**
✅ **Mock Mode** for testing

## 📝 Current Limitations

- **Media Upload**: Currently uses placeholder (needs real image files)
- **Rate Limits**: Twitter has strict rate limits (300 tweets per 15 minutes)
- **API Access**: May require paid plan for full features

## 🚀 Next Steps

1. **Get Twitter Developer Account**
2. **Create App and Get Credentials**
3. **Update config.yaml with real credentials**
4. **Test posting functionality**
5. **Run full Poof Palace system**

## 🎉 Expected Results

Once configured, The Poof Palace will:
- ✅ Generate witty, royal captions
- ✅ Post to Twitter automatically
- ✅ Create platform-specific content
- ✅ Run autonomously 24/7

## 🆘 Troubleshooting

### Common Issues:
- **"Invalid credentials"**: Check your API keys are correct
- **"Rate limit exceeded"**: Wait 15 minutes between batches
- **"App not approved"**: Ensure your app has proper permissions

### Need Help?
- Check Twitter API documentation
- Verify your app permissions
- Test with simple text-only tweets first

---

**Ready to make Her Royal Floofiness tweet? Let's get Twitter connected!** 👑🐱✨
