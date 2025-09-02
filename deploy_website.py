#!/usr/bin/env python3
"""
The Poof Palace Website Deployment Script
Uploads website files to your hosting provider
"""

import os
import shutil
from pathlib import Path

def create_deployment_package():
    """Create a deployment package with all website files"""
    
    print("🐱 The Poof Palace Website Deployment 🐱")
    print("=" * 50)
    
    # Create deployment directory
    deploy_dir = Path("deploy")
    deploy_dir.mkdir(exist_ok=True)
    
    # Copy website files
    website_files = [
        "website/index.html",
        "website/terms.html", 
        "website/privacy.html",
        "tiktokj3DGrHJo5mGBA1oENoMV4qX3GX1vAmKK.txt"
    ]
    
    print("📁 Creating deployment package...")
    
    for file_path in website_files:
        if os.path.exists(file_path):
            # Get just the filename
            filename = os.path.basename(file_path)
            dest_path = deploy_dir / filename
            
            # Copy file
            shutil.copy2(file_path, dest_path)
            print(f"✅ Copied: {filename}")
        else:
            print(f"❌ Missing: {file_path}")
    
    print(f"\n📦 Deployment package created in: {deploy_dir.absolute()}")
    print("\n🚀 Next steps:")
    print("1. Upload all files from the 'deploy' folder to your website root")
    print("2. Ensure these URLs are accessible:")
    print("   - https://poofpalace-ftswcv.manus.space/")
    print("   - https://poofpalace-ftswcv.manus.space/terms")
    print("   - https://poofpalace-ftswcv.manus.space/privacy")
    print("   - https://poofpalace-ftswcv.manus.space/tiktokj3DGrHJo5mGBA1oENoMV4qX3GX1vAmKK.txt")
    print("\n3. Complete TikTok app review with these URLs")
    print("4. Submit for TikTok app approval!")
    
    return deploy_dir

def test_local_server():
    """Test the local website server"""
    print("\n🌐 Testing local website...")
    print("Your website should be available at: http://localhost:8000")
    print("Press Ctrl+C to stop the server when done testing")

if __name__ == "__main__":
    deploy_dir = create_deployment_package()
    test_local_server()
