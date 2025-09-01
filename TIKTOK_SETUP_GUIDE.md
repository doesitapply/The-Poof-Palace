# 🎵 TikTok API Setup Guide for The Poof Palace

## 🎯 Overview
This guide will help you set up TikTok API integration for The Poof Palace autonomous content engine.

## 📋 Prerequisites
- TikTok Developer Account
- TikTok App with Content Posting API access
- Video content creation capability

## 🚀 Step-by-Step Setup

### 1. Create TikTok Developer Account
1. Go to [TikTok Developer Portal](https://developers.tiktok.com/)
2. Sign in with your TikTok account
3. Apply for a developer account (usually approved quickly)

### 2. Create a New App
1. In the Developer Portal, click "Create App"
2. Fill in the required information:
   - **App Name**: "The Poof Palace"
   - **App Description**: "Autonomous content generation for The Poof Palace brand"
   - **Website URL**: Your website (or placeholder)
   - **Category**: "Entertainment" or "Lifestyle"

### 3. Get API Credentials
1. Go to your app's "Keys and Tokens" tab
2. You'll need these credentials:
   - **Client Key** (App ID)
   - **Client Secret** (App Secret)
   - **Access Token** (User Access Token)

### 4. Enable Content Posting API
1. In your app settings, ensure you have:
   - **Content Posting API** access enabled
   - **Video Upload** permissions
   - **User Authorization** configured

### 5. Update Configuration
Replace the placeholder values in `config.yaml`:

```yaml
# TikTok API credentials (from TikTok Developer Portal)
TIKTOK_ACCESS_TOKEN: "your_actual_access_token_here"
TIKTOK_CLIENT_KEY: "your_actual_client_key_here"
```

## 🧪 Testing the Integration

### Test with Mock Mode (Current)
```bash
source venv/bin/activate
python -c "
import yaml
from modules.api_clients import TikTokClient
config = yaml.safe_load(open('config.yaml'))
tiktok = TikTokClient(config)
result = tiktok.post_video('test_video.mp4', 'Test video from The Poof Palace! 👑🐱')
print(f'Result: {result}')
"
```

### Test with Real Credentials
Once you've added your real credentials, the same test will post to TikTok!

## 🔧 Features Implemented

✅ **TikTok Content Posting API Integration**
✅ **Video Upload Support**
✅ **Caption and Description Support**
✅ **Privacy Settings Configuration**
✅ **Error Handling**
✅ **Mock Mode** for testing

## 📝 Current Limitations

- **Video Content**: Currently uses placeholder (needs real video files)
- **Rate Limits**: TikTok has strict rate limits
- **API Access**: May require approval for Content Posting API

## 🚀 Next Steps

1. **Get TikTok Developer Account**
2. **Create App and Get Credentials**
3. **Update config.yaml with real credentials**
4. **Test posting functionality**
5. **Run full Poof Palace system**

## 🎉 Expected Results

Once configured, The Poof Palace will:
- ✅ Generate witty, royal captions
- ✅ Post videos to TikTok automatically
- ✅ Create platform-specific content
- ✅ Run autonomously 24/7

## 🆘 Troubleshooting

### Common Issues:
- **"Invalid credentials"**: Check your API keys are correct
- **"Rate limit exceeded"**: Wait between requests
- **"App not approved"**: Ensure your app has proper permissions

### Need Help?
- Check TikTok API documentation
- Verify your app permissions
- Test with simple video uploads first

## 🎬 Video Content Creation

For The Poof Palace, you'll need to create video content. Consider:
- **Short animations** of Lil Poof
- **Slideshow videos** with generated images
- **Text-based videos** with royal captions
- **AI-generated video** content

---

**Ready to make Her Royal Floofiness go viral on TikTok? Let's get TikTok connected!** 👑🐱✨🎵
