#!/bin/bash

# Build script for Render deployment
echo "🚀 Starting build process..."

# Upgrade pip
python -m pip install --upgrade pip

# Install setuptools and wheel first
pip install setuptools>=68.0.0 wheel

# Install dependencies
pip install -r requirements.txt

echo "✅ Build completed successfully!" 