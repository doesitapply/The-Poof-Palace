#!/usr/bin/env python3
"""
The Poof Palace Setup Verification Script
=========================================

This script verifies that your Poof Palace Autonomous Engine is properly configured
and ready to launch. Run this before starting the main engine.

Usage: python setup_verification.py
"""

import os
import sys
import yaml
import requests
from pathlib import Path

def check_file_exists(filepath, description):
    """Check if a required file exists."""
    if os.path.exists(filepath):
        print(f"✅ {description}: {filepath}")
        return True
    else:
        print(f"❌ {description}: {filepath} - MISSING")
        return False

def check_directory_exists(dirpath, description):
    """Check if a required directory exists."""
    if os.path.exists(dirpath) and os.path.isdir(dirpath):
        print(f"✅ {description}: {dirpath}")
        return True
    else:
        print(f"❌ {description}: {dirpath} - MISSING")
        return False

def check_config_validity():
    """Check if config.yaml is valid and has required fields."""
    try:
        with open('config.yaml', 'r') as f:
            config = yaml.safe_load(f)
        
        required_fields = [
            'OLLAMA_API_BASE_URL', 'COMFYUI_API_BASE_URL', 'OLLAMA_MODEL',
            'COMFYUI_LORA_NAME', 'COMFYUI_CHECKPOINT_NAME', 'BRAND_NAME', 'MASCOT_NAME'
        ]
        
        missing_fields = []
        for field in required_fields:
            if field not in config:
                missing_fields.append(field)
        
        if missing_fields:
            print(f"❌ Config missing required fields: {missing_fields}")
            return False
        else:
            print("✅ Config file is valid with all required fields")
            return True
            
    except Exception as e:
        print(f"❌ Config file error: {e}")
        return False

def check_lore_bible():
    """Check if lore_bible.txt exists and has content."""
    try:
        with open('lore_bible.txt', 'r') as f:
            content = f.read().strip()
        
        if len(content) > 50:  # Basic check for substantial content
            print("✅ Lore bible has substantial content")
            return True
        else:
            print("❌ Lore bible appears to be empty or too short")
            return False
            
    except Exception as e:
        print(f"❌ Lore bible error: {e}")
        return False

def check_local_services():
    """Check if local AI services are running."""
    config = {}
    try:
        with open('config.yaml', 'r') as f:
            config = yaml.safe_load(f)
    except:
        print("❌ Cannot load config to check services")
        return False
    
    # Check Ollama
    try:
        response = requests.get(f"{config['OLLAMA_API_BASE_URL']}/api/tags", timeout=5)
        if response.status_code == 200:
            print("✅ Ollama service is running")
            ollama_ok = True
        else:
            print("❌ Ollama service not responding properly")
            ollama_ok = False
    except:
        print("❌ Ollama service is not running or not accessible")
        ollama_ok = False
    
    # Check ComfyUI
    try:
        response = requests.get(f"{config['COMFYUI_API_BASE_URL']}/system_stats", timeout=5)
        if response.status_code == 200:
            print("✅ ComfyUI service is running")
            comfyui_ok = True
        else:
            print("❌ ComfyUI service not responding properly")
            comfyui_ok = False
    except:
        print("❌ ComfyUI service is not running or not accessible")
        comfyui_ok = False
    
    return ollama_ok and comfyui_ok

def main():
    """Main verification function."""
    print("🏰 The Poof Palace Setup Verification")
    print("=" * 50)
    
    all_good = True
    
    # Check file structure
    print("\n📁 Checking File Structure:")
    files_to_check = [
        ('config.yaml', 'Configuration file'),
        ('lore_bible.txt', 'Lore bible'),
        ('main.py', 'Main entry point'),
        ('requirements.txt', 'Dependencies file'),
        ('modules/__init__.py', 'Modules package init'),
        ('modules/api_clients.py', 'API clients module'),
        ('modules/orchestrator.py', 'Orchestrator module'),
        ('modules/data_models.py', 'Data models module'),
    ]
    
    for filepath, description in files_to_check:
        if not check_file_exists(filepath, description):
            all_good = False
    
    # Check directories
    print("\n📂 Checking Directories:")
    dirs_to_check = [
        ('output/images', 'Images output directory'),
        ('output/logs', 'Logs output directory'),
    ]
    
    for dirpath, description in dirs_to_check:
        if not check_directory_exists(dirpath, description):
            all_good = False
    
    # Check config validity
    print("\n⚙️  Checking Configuration:")
    if not check_config_validity():
        all_good = False
    
    # Check lore bible
    print("\n📖 Checking Lore Bible:")
    if not check_lore_bible():
        all_good = False
    
    # Check local services
    print("\n🤖 Checking Local AI Services:")
    if not check_local_services():
        all_good = False
        print("\n💡 To fix service issues:")
        print("   - Start Ollama: ollama serve")
        print("   - Start ComfyUI: python main.py --listen")
    
    # Final result
    print("\n" + "=" * 50)
    if all_good:
        print("🎉 SUCCESS! The Poof Palace is ready to launch!")
        print("   Run: python main.py")
        print("   Her Royal Floofiness awaits! 👑🐱")
    else:
        print("⚠️  Some issues found. Please fix them before launching.")
        print("   Check the errors above and try again.")
    
    return all_good

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

