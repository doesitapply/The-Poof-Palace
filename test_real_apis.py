#!/usr/bin/env python3
"""
The Poof Palace - Real API Testing Script
=========================================
This script tests all APIs with real calls to verify everything is working.
No mocks - only real results!
"""

import sys
import os
import time
from datetime import datetime

# Add current directory to path
sys.path.insert(0, os.getcwd())

def test_secure_config():
    """Test the secure configuration loading."""
    print("🔐 Testing Secure Configuration...")
    try:
        from modules.secure_config import load_secure_config
        config = load_secure_config()
        print("✅ Secure configuration loaded successfully")
        return config
    except Exception as e:
        print(f"❌ Configuration test failed: {e}")
        return None

def test_gemini_api(config):
    """Test Gemini API with real text generation."""
    print("\n🤖 Testing Gemini API...")
    try:
        import google.generativeai as genai
        
        # Configure Gemini
        genai.configure(api_key=config.get_secret('GEMINI_API_KEY'))
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        
        # Test prompt
        test_prompt = "You are Lil Poof, the cat queen of The Poof Palace. Write a short, witty royal decree about napping."
        
        print("📝 Generating text with Gemini...")
        response = model.generate_content(test_prompt)
        
        if response.text:
            print("✅ Gemini API working!")
            print(f"📜 Generated text: {response.text[:100]}...")
            return True
        else:
            print("❌ Gemini API returned empty response")
            return False
            
    except Exception as e:
        print(f"❌ Gemini API test failed: {e}")
        return False

def test_google_cloud_auth(config):
    """Test Google Cloud authentication."""
    print("\n☁️ Testing Google Cloud Authentication...")
    try:
        import vertexai
        
        project_id = config.get('GOOGLE_CLOUD_PROJECT_ID')
        location = config.get('GOOGLE_CLOUD_LOCATION', 'us-central1')
        
        if project_id == "your-gcp-project-id-here":
            print("⚠️ Google Cloud Project ID not configured")
            print("Please update GOOGLE_CLOUD_PROJECT_ID in your .env file")
            return False
        
        print(f"🔧 Initializing Vertex AI with project: {project_id}")
        vertexai.init(project=project_id, location=location)
        print("✅ Google Cloud authentication successful!")
        return True
        
    except Exception as e:
        print(f"❌ Google Cloud authentication failed: {e}")
        print("💡 Make sure you've run: gcloud auth application-default login")
        return False

def test_vertex_ai_imagen(config):
    """Test Vertex AI Imagen for real image generation."""
    print("\n🎨 Testing Vertex AI Imagen...")
    try:
        from vertexai.preview.vision_models import ImageGenerationModel
        
        model_name = config.get('IMAGEN_MODEL', 'imagegeneration@006')
        print(f"🖼️ Using Imagen model: {model_name}")
        
        model = ImageGenerationModel.from_pretrained(model_name)
        
        # Test prompt
        test_prompt = "A cute orange cat wearing a tiny crown, sitting on a velvet cushion, whimsical storybook illustration style"
        
        print("🎨 Generating image with Vertex AI Imagen...")
        response = model.generate_images(
            prompt=test_prompt,
            number_of_images=1,
            negative_prompt="ugly, deformed, blurry, photorealistic"
        )
        
        if response.images:
            # Save the test image
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_path = f"output/images/test_imagen_{timestamp}.png"
            
            response.images[0].save(location=output_path)
            print(f"✅ Vertex AI Imagen working! Image saved to: {output_path}")
            return True
        else:
            print("❌ Vertex AI Imagen returned no images")
            return False
            
    except Exception as e:
        print(f"❌ Vertex AI Imagen test failed: {e}")
        return False

def test_instagram_api(config):
    """Test Instagram API connection."""
    print("\n📸 Testing Instagram API...")
    try:
        import requests
        
        access_token = config.get_secret('INSTAGRAM_ACCESS_TOKEN')
        user_id = config.get_secret('INSTAGRAM_USER_ID')
        
        # Test API connection
        url = f"https://graph.facebook.com/v18.0/{user_id}"
        params = {
            'fields': 'id,username,account_type',
            'access_token': access_token
        }
        
        print("🔗 Testing Instagram API connection...")
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Instagram API working! Account: {data.get('username', 'Unknown')}")
            return True
        else:
            print(f"❌ Instagram API test failed: {response.status_code} - {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Instagram API test failed: {e}")
        return False

def test_twitter_api(config):
    """Test Twitter API connection."""
    print("\n🐦 Testing Twitter API...")
    try:
        import requests
        
        bearer_token = config.get_secret('TWITTER_BEARER_TOKEN')
        
        # Test API connection
        url = "https://api.twitter.com/2/users/me"
        headers = {
            'Authorization': f'Bearer {bearer_token}'
        }
        
        print("🔗 Testing Twitter API connection...")
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Twitter API working! User: {data.get('data', {}).get('username', 'Unknown')}")
            return True
        else:
            print(f"❌ Twitter API test failed: {response.status_code} - {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Twitter API test failed: {e}")
        return False

def test_full_content_generation(config):
    """Test the complete content generation pipeline."""
    print("\n🏰 Testing Full Content Generation Pipeline...")
    try:
        from modules.orchestrator import Orchestrator
        
        print("🎭 Initializing orchestrator...")
        orchestrator = Orchestrator(config)
        
        print("🎨 Running content generation cycle...")
        orchestrator.run_daily_content_cycle()
        
        print("✅ Full content generation test completed!")
        return True
        
    except Exception as e:
        print(f"❌ Full content generation test failed: {e}")
        return False

def main():
    """Run all API tests."""
    print("🏰 The Poof Palace - Real API Testing 🏰")
    print("=" * 50)
    print("🧪 Testing all APIs with real calls (no mocks!)")
    print("=" * 50)
    
    # Test configuration
    config = test_secure_config()
    if not config:
        print("\n❌ Configuration test failed. Cannot proceed.")
        return
    
    # Test results tracking
    results = {}
    
    # Test Gemini API
    results['gemini'] = test_gemini_api(config)
    
    # Test Google Cloud authentication
    results['google_cloud'] = test_google_cloud_auth(config)
    
    # Test Vertex AI Imagen (only if Google Cloud auth works)
    if results['google_cloud']:
        results['vertex_ai'] = test_vertex_ai_imagen(config)
    else:
        print("\n⚠️ Skipping Vertex AI test - Google Cloud auth failed")
        results['vertex_ai'] = False
    
    # Test social media APIs
    results['instagram'] = test_instagram_api(config)
    results['twitter'] = test_twitter_api(config)
    
    # Test full pipeline (only if core APIs work)
    if results['gemini'] and results['google_cloud']:
        results['full_pipeline'] = test_full_content_generation(config)
    else:
        print("\n⚠️ Skipping full pipeline test - core APIs not working")
        results['full_pipeline'] = False
    
    # Print summary
    print("\n" + "=" * 50)
    print("📊 TEST RESULTS SUMMARY")
    print("=" * 50)
    
    for test_name, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test_name.upper():<15}: {status}")
    
    # Overall status
    passed_tests = sum(results.values())
    total_tests = len(results)
    
    print(f"\n🎯 Overall: {passed_tests}/{total_tests} tests passed")
    
    if passed_tests == total_tests:
        print("🎉 ALL TESTS PASSED! The Poof Palace is ready to rule!")
    elif passed_tests >= total_tests // 2:
        print("⚠️ Some tests failed, but core functionality is working")
    else:
        print("❌ Multiple tests failed. Check your API keys and setup.")
    
    print("\n🔧 Next steps:")
    if not results['google_cloud']:
        print("- Set up Google Cloud project and authentication")
    if not results['gemini']:
        print("- Check your Gemini API key")
    if not results['instagram']:
        print("- Verify Instagram API credentials")
    if not results['twitter']:
        print("- Check Twitter API credentials")

if __name__ == "__main__":
    main()
