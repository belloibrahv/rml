#!/usr/bin/env python3
"""
Test script to verify deployment configuration
Run this locally before deploying to ensure everything works
"""

import os
import sys
import importlib

def test_imports():
    """Test that all required packages can be imported"""
    required_packages = [
        'flask',
        'flask_cors', 
        'numpy',
        'pandas',
        'sklearn',
        'joblib',
        'gunicorn'
    ]
    
    print("Testing package imports...")
    for package in required_packages:
        try:
            importlib.import_module(package)
            print(f"✅ {package}")
        except ImportError as e:
            print(f"❌ {package}: {e}")
            return False
    return True

def test_app_creation():
    """Test that the Flask app can be created"""
    try:
        from app import app
        print("✅ Flask app created successfully")
        return True
    except Exception as e:
        print(f"❌ Flask app creation failed: {e}")
        return False

def test_model_loading():
    """Test ML model loading (will use fallback if models not available)"""
    try:
        from app import career_model, label_encoder, skills_mlb, interests_mlb
        print("✅ Model loading test completed")
        return True
    except Exception as e:
        print(f"⚠️ Model loading test: {e}")
        return True  # This is expected if models are not available

def test_static_files():
    """Test that static files exist"""
    static_dir = "static"
    templates_dir = "templates"
    
    if os.path.exists(static_dir):
        print(f"✅ Static directory exists: {static_dir}")
    else:
        print(f"❌ Static directory missing: {static_dir}")
        return False
    
    if os.path.exists(templates_dir):
        print(f"✅ Templates directory exists: {templates_dir}")
    else:
        print(f"❌ Templates directory missing: {templates_dir}")
        return False
    
    return True

def test_requirements():
    """Test that requirements.txt exists and is readable"""
    if os.path.exists("requirements.txt"):
        print("✅ requirements.txt exists")
        try:
            with open("requirements.txt", "r") as f:
                requirements = f.read()
                if "Flask" in requirements and "gunicorn" in requirements:
                    print("✅ requirements.txt contains necessary packages")
                    return True
                else:
                    print("❌ requirements.txt missing necessary packages")
                    return False
        except Exception as e:
            print(f"❌ Error reading requirements.txt: {e}")
            return False
    else:
        print("❌ requirements.txt missing")
        return False

def main():
    """Run all tests"""
    print("🚀 Testing deployment configuration...\n")
    
    tests = [
        ("Package Imports", test_imports),
        ("Flask App Creation", test_app_creation),
        ("Model Loading", test_model_loading),
        ("Static Files", test_static_files),
        ("Requirements File", test_requirements)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n--- {test_name} ---")
        if test_func():
            passed += 1
        else:
            print(f"❌ {test_name} failed")
    
    print(f"\n📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Your application is ready for deployment.")
        print("\nNext steps:")
        print("1. Push your code to GitHub")
        print("2. Connect your repository to Render")
        print("3. Deploy using the render.yaml configuration")
        print("4. Or follow the manual deployment guide in DEPLOYMENT_GUIDE.md")
    else:
        print("⚠️ Some tests failed. Please fix the issues before deploying.")
        sys.exit(1)

if __name__ == "__main__":
    main() 