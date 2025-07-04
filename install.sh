#!/bin/bash

# AI Career Recommendation System - Installation Script
# This script sets up the project with all necessary dependencies

echo "🚀 AI Career Recommendation System - Installation Script"
echo "=================================================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher first."
    exit 1
fi

# Check Python version
python_version=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo "✅ Python version: $python_version"

# Navigate to backend directory
if [ ! -d "backend" ]; then
    echo "❌ Backend directory not found. Please run this script from the project root."
    exit 1
fi

cd backend

# Create virtual environment
echo "📦 Creating virtual environment..."
if [ -d "venv" ]; then
    echo "⚠️  Virtual environment already exists. Removing old one..."
    rm -rf venv
fi

python3 -m venv venv

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "📚 Installing dependencies..."
pip install -r requirements.txt

# Make startup script executable
echo "🔧 Making startup script executable..."
chmod +x start.sh

echo ""
echo "✅ Installation completed successfully!"
echo ""
echo "🎯 To start the application:"
echo "   cd backend"
echo "   source venv/bin/activate"
echo "   python run.py"
echo ""
echo "   Or simply run:"
echo "   ./start.sh"
echo ""
echo "🌐 The application will be available at: http://localhost:5001"
echo ""
echo "📖 For more information, see README.md" 