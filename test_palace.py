#!/usr/bin/env python3
"""
The Poof Palace Test Script
===========================

This script tests The Poof Palace Autonomous Engine by running
a content generation cycle immediately instead of waiting for the scheduler.

Usage: python test_palace.py
"""

import yaml
from modules.orchestrator import Orchestrator

def test_palace():
    """Test The Poof Palace content generation immediately."""
    print("🏰 The Poof Palace Test Mode")
    print("=" * 40)
    print("")
    print("👑 Testing Her Royal Floofiness...")
    print("")
    
    try:
        # Load configuration
        print("📋 Loading configuration...")
        config = yaml.safe_load(open('config.yaml'))
        print("✅ Configuration loaded")
        
        # Initialize orchestrator
        print("🔧 Initializing orchestrator...")
        orchestrator = Orchestrator(config)
        print("✅ Orchestrator ready")
        
        print("")
        print("🚀 Starting immediate content generation test...")
        print("=" * 40)
        
        # Run the content cycle immediately
        orchestrator.run_daily_content_cycle()
        
        print("")
        print("🎉 Test completed successfully!")
        print("👑 Her Royal Floofiness is working perfectly!")
        
    except Exception as e:
        print(f"❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_palace()

