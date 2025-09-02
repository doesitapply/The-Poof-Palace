#!/usr/bin/env python3
"""
The Poof Palace - Security Setup Script
=======================================
This script helps you set up a secure environment for The Poof Palace.
It creates the necessary files and guides you through the setup process.
"""

import os
import shutil
import sys
from pathlib import Path

def print_banner():
    """Print the security setup banner."""
    print("""
🏰 The Poof Palace - Security Setup 🏰
=====================================
🔒 Setting up secure environment for Her Royal Floofiness
""")

def check_existing_files():
    """Check for existing security files."""
    files_to_check = ['.env', 'secrets_template.env', '.gitignore']
    existing_files = []
    
    for file in files_to_check:
        if os.path.exists(file):
            existing_files.append(file)
    
    return existing_files

def create_env_file():
    """Create the .env file from template."""
    template_path = "secrets_template.env"
    env_path = ".env"
    
    if os.path.exists(env_path):
        response = input(f"⚠️  {env_path} already exists. Overwrite? (y/N): ")
        if response.lower() != 'y':
            print(f"✅ Keeping existing {env_path}")
            return True
    
    if not os.path.exists(template_path):
        print(f"❌ Template file {template_path} not found!")
        return False
    
    try:
        shutil.copy2(template_path, env_path)
        print(f"✅ Created {env_path} from template")
        return True
    except Exception as e:
        print(f"❌ Error creating {env_path}: {e}")
        return False

def create_gitkeep_files():
    """Create .gitkeep files for empty directories."""
    directories = ['output/images', 'output/logs', 'output/videos']
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        gitkeep_path = os.path.join(directory, '.gitkeep')
        
        if not os.path.exists(gitkeep_path):
            with open(gitkeep_path, 'w') as f:
                f.write("# This file ensures the directory is tracked by git\n")
            print(f"✅ Created {gitkeep_path}")

def validate_env_file():
    """Validate that the .env file has been configured."""
    env_path = ".env"
    
    if not os.path.exists(env_path):
        print(f"❌ {env_path} not found!")
        return False
    
    # Check for placeholder values
    placeholder_values = [
        "your_gemini_api_key_here",
        "your-gcp-project-id-here",
        "your_instagram_access_token_here"
    ]
    
    try:
        with open(env_path, 'r') as f:
            content = f.read()
        
        found_placeholders = []
        for placeholder in placeholder_values:
            if placeholder in content:
                found_placeholders.append(placeholder)
        
        if found_placeholders:
            print(f"⚠️  Found placeholder values in {env_path}:")
            for placeholder in found_placeholders:
                print(f"   - {placeholder}")
            print("\nPlease edit .env and replace these with your actual API keys.")
            return False
        
        print(f"✅ {env_path} appears to be configured")
        return True
        
    except Exception as e:
        print(f"❌ Error reading {env_path}: {e}")
        return False

def test_secure_config():
    """Test the secure configuration loader."""
    try:
        # Add the current directory to Python path
        sys.path.insert(0, os.getcwd())
        
        from modules.secure_config import load_secure_config
        
        print("🧪 Testing secure configuration loader...")
        config = load_secure_config()
        
        print("✅ Secure configuration loaded successfully!")
        config.print_config_summary()
        
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("Make sure you're running this script from the the_poof_palace directory")
        return False
    except Exception as e:
        print(f"❌ Configuration test failed: {e}")
        return False

def print_next_steps():
    """Print the next steps for the user."""
    print("""
🎉 Security Setup Complete! 🎉
==============================

Next steps:

1. 📝 Edit your .env file with actual API keys:
   - Get Gemini API key from: https://aistudio.google.com/
   - Set up Google Cloud project for Vertex AI
   - Configure social media API keys

2. 🧪 Test your configuration:
   python -m modules.secure_config

3. 🚀 Launch The Poof Palace:
   python main.py

4. 📖 Read the full security guide:
   cat SECURITY_SETUP.md

🔒 Your secrets are now safely protected! 👑🐱
""")

def main():
    """Main setup function."""
    print_banner()
    
    # Check current directory
    if not os.path.exists("config.yaml"):
        print("❌ Error: config.yaml not found!")
        print("Please run this script from the the_poof_palace directory")
        sys.exit(1)
    
    # Check for existing files
    existing_files = check_existing_files()
    if existing_files:
        print(f"📁 Found existing files: {', '.join(existing_files)}")
    
    # Create .env file
    print("\n🔐 Setting up environment file...")
    if not create_env_file():
        print("❌ Failed to create .env file")
        sys.exit(1)
    
    # Create .gitkeep files
    print("\n📁 Creating directory structure...")
    create_gitkeep_files()
    
    # Validate .env file
    print("\n🔍 Validating environment file...")
    env_valid = validate_env_file()
    
    if not env_valid:
        print("\n⚠️  Please edit your .env file with actual API keys, then run:")
        print("   python setup_security.py --test")
        sys.exit(1)
    
    # Test secure configuration
    print("\n🧪 Testing secure configuration...")
    if test_secure_config():
        print_next_steps()
    else:
        print("\n❌ Configuration test failed. Please check your .env file.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        # Test mode - just validate existing setup
        print("🧪 Testing existing security setup...")
        if test_secure_config():
            print("✅ Security setup is working correctly!")
        else:
            print("❌ Security setup needs attention.")
            sys.exit(1)
    else:
        # Full setup mode
        main()
