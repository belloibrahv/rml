#!/usr/bin/env python3
"""
Startup script for the AI Career Recommendation System
"""

import os
import sys
import subprocess
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ Error: Python 3.8 or higher is required")
        print(f"Current version: {sys.version}")
        sys.exit(1)
    print(f"✅ Python version: {sys.version.split()[0]}")

def check_dependencies():
    """Check if required dependencies are installed"""
    required_packages = [
        'flask', 'numpy', 'pandas', 'sklearn', 
        'joblib', 'werkzeug'
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            if package == 'sklearn':
                import sklearn
            else:
                __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"❌ Missing packages: {', '.join(missing_packages)}")
        print("Please install dependencies: pip install -r requirements.txt")
        sys.exit(1)
    print("✅ All dependencies are installed")

def check_model_files():
    """Check if ML model files exist"""
    model_dir = Path(__file__).parent / "app" / "models"
    required_models = [
        "career_recommendation_model.pkl",
        "career_label_encoder.pkl", 
        "skills_mlb.pkl",
        "interests_mlb.pkl"
    ]
    
    missing_models = []
    for model in required_models:
        if not (model_dir / model).exists():
            missing_models.append(model)
    
    if missing_models:
        print(f"⚠️  Warning: Missing model files: {', '.join(missing_models)}")
        print("The system will use fallback logic for recommendations")
    else:
        print("✅ All ML model files found")

def create_env_file():
    """Create .env file if it doesn't exist"""
    env_file = Path(__file__).parent / ".env"
    if not env_file.exists():
        env_content = """# Flask Configuration
FLASK_SECRET_KEY=your-secret-key-change-in-production
FLASK_ENV=development
DATABASE_URL=sqlite:///career_reco.db

# Application Settings
DEBUG=True
HOST=0.0.0.0
PORT=5000
"""
        with open(env_file, 'w') as f:
            f.write(env_content)
        print("✅ Created .env file")

def main():
    """Main startup function"""
    print("🚀 Starting AI Career Recommendation System")
    print("=" * 50)
    
    # Change to the correct directory
    os.chdir(Path(__file__).parent)
    
    # Run checks
    check_python_version()
    check_dependencies()
    check_model_files()
    create_env_file()
    
    print("\n🎯 Starting Flask application...")
    print("📍 Application will be available at: http://localhost:5001")
    print("🛑 Press Ctrl+C to stop the server")
    print("=" * 50)
    
    try:
        # Import and run the Flask app
        from app.app import app
        app.run(
            host='0.0.0.0',
            port=5001,
            debug=True
        )
    except KeyboardInterrupt:
        print("\n👋 Server stopped by user")
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 