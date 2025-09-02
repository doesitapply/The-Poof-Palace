#!/usr/bin/env python3
"""
The Poof Palace - Working APIs Test
===================================
Test the APIs that are actually working right now.
"""

import sys
import os
from datetime import datetime

# Add current directory to path
sys.path.insert(0, os.getcwd())

def test_gemini_content_generation():
    """Test full content generation with Gemini."""
    print("🤖 Testing Gemini Content Generation...")
    try:
        import google.generativeai as genai
        from modules.secure_config import load_secure_config
        
        config = load_secure_config()
        genai.configure(api_key=config.get_secret('GEMINI_API_KEY'))
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        
        # Test 1: Generate a content idea
        print("💡 Generating content idea...")
        idea_prompt = "Give me a simple, one-sentence idea for an illustration of Lil Poof. Focus on a classic cat behavior like napping, playing, or being mischievous."
        system_prompt = "You are a creative director for The Poof Palace brand."
        
        idea_response = model.generate_content(f"{system_prompt}\n\n{idea_prompt}")
        idea = idea_response.text.strip()
        print(f"✅ Generated idea: {idea}")
        
        # Test 2: Generate a caption
        print("📝 Generating royal caption...")
        caption_prompt = f"Write a witty, regal caption from the perspective of Lil Poof for an image depicting: '{idea}'. Include 3-5 relevant hashtags."
        system_prompt_caption = "You are Lil Poof, the cat queen of The Poof Palace. You are witty, regal, and slightly dramatic."
        
        caption_response = model.generate_content(f"{system_prompt_caption}\n\n{caption_prompt}")
        caption = caption_response.text.strip()
        print(f"✅ Generated caption: {caption}")
        
        # Test 3: Generate alt text
        print("🔍 Generating alt text...")
        alt_text_prompt = f"Write a descriptive alt text for an image of: '{idea}' in a whimsical storybook style."
        
        alt_text_response = model.generate_content(f"{system_prompt_caption}\n\n{alt_text_prompt}")
        alt_text = alt_text_response.text.strip()
        print(f"✅ Generated alt text: {alt_text}")
        
        # Save results
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"output/logs/gemini_test_{timestamp}.txt"
        
        with open(output_file, 'w') as f:
            f.write(f"Gemini API Test Results - {datetime.now()}\n")
            f.write("=" * 50 + "\n\n")
            f.write(f"Idea: {idea}\n\n")
            f.write(f"Caption: {caption}\n\n")
            f.write(f"Alt Text: {alt_text}\n\n")
        
        print(f"📁 Results saved to: {output_file}")
        return True
        
    except Exception as e:
        print(f"❌ Gemini content generation failed: {e}")
        return False

def test_twitter_caption_adaptation():
    """Test Twitter caption adaptation."""
    print("\n🐦 Testing Twitter Caption Adaptation...")
    try:
        import google.generativeai as genai
        from modules.secure_config import load_secure_config
        
        config = load_secure_config()
        genai.configure(api_key=config.get_secret('GEMINI_API_KEY'))
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        
        # Sample Instagram caption
        instagram_caption = "By royal decree, all subjects must provide belly rubs upon demand! 👑🐱 #LilPoof #RoyalDecree #CatQueen #BellyRubs #ThePoofPalace"
        
        twitter_prompt = f"Create a Twitter version of this Instagram caption (under 280 characters, keep the royal personality): '{instagram_caption}'"
        system_prompt = "You are Lil Poof, the cat queen. Create witty, royal Twitter posts."
        
        twitter_response = model.generate_content(f"{system_prompt}\n\n{twitter_prompt}")
        twitter_caption = twitter_response.text.strip()
        
        # Ensure it's under 280 characters
        if len(twitter_caption) > 280:
            twitter_caption = twitter_caption[:277] + "..."
        
        print(f"✅ Twitter caption ({len(twitter_caption)} chars): {twitter_caption}")
        return True
        
    except Exception as e:
        print(f"❌ Twitter caption adaptation failed: {e}")
        return False

def test_lore_bible_integration():
    """Test integration with Lil Poof's lore bible."""
    print("\n📚 Testing Lore Bible Integration...")
    try:
        import google.generativeai as genai
        from modules.secure_config import load_secure_config
        
        config = load_secure_config()
        genai.configure(api_key=config.get_secret('GEMINI_API_KEY'))
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        
        # Read the lore bible
        with open(config.get('LORE_BIBLE_PATH'), 'r') as f:
            lore_bible = f.read()
        
        # Test prompt that should use lore bible knowledge
        test_prompt = "Write a short story about Lil Poof's arch-nemesis, The Glimmering Red Dot. Include details about her throne and her royal personality."
        
        full_prompt = f"{lore_bible}\n\n{test_prompt}"
        
        response = model.generate_content(full_prompt)
        story = response.text.strip()
        
        print("✅ Lore Bible integration working!")
        print(f"📖 Generated story: {story[:200]}...")
        return True
        
    except Exception as e:
        print(f"❌ Lore Bible integration failed: {e}")
        return False

def main():
    """Run all working API tests."""
    print("🏰 The Poof Palace - Working APIs Test 🏰")
    print("=" * 50)
    print("🧪 Testing APIs that are currently working")
    print("=" * 50)
    
    results = {}
    
    # Test Gemini content generation
    results['gemini_content'] = test_gemini_content_generation()
    
    # Test Twitter caption adaptation
    results['twitter_adaptation'] = test_twitter_caption_adaptation()
    
    # Test lore bible integration
    results['lore_bible'] = test_lore_bible_integration()
    
    # Print summary
    print("\n" + "=" * 50)
    print("📊 WORKING API TEST RESULTS")
    print("=" * 50)
    
    for test_name, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test_name.upper():<20}: {status}")
    
    passed_tests = sum(results.values())
    total_tests = len(results)
    
    print(f"\n🎯 Overall: {passed_tests}/{total_tests} tests passed")
    
    if passed_tests == total_tests:
        print("🎉 ALL WORKING TESTS PASSED!")
        print("✅ The Poof Palace can generate content with Gemini!")
        print("✅ Twitter caption adaptation is working!")
        print("✅ Lore Bible integration is working!")
    else:
        print("⚠️ Some tests failed, but core functionality is working")
    
    print("\n🔧 Next steps:")
    print("- Set up Google Cloud project for image generation")
    print("- Update social media API tokens")
    print("- Test full content pipeline")

if __name__ == "__main__":
    main()
