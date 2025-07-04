@echo off
REM AI Career Recommendation System - Installation Script for Windows
REM This script sets up the project with all necessary dependencies

echo 🚀 AI Career Recommendation System - Installation Script
echo ==================================================

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed. Please install Python 3.8 or higher first.
    pause
    exit /b 1
)

REM Check Python version
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set python_version=%%i
echo ✅ Python version: %python_version%

REM Navigate to backend directory
if not exist "backend" (
    echo ❌ Backend directory not found. Please run this script from the project root.
    pause
    exit /b 1
)

cd backend

REM Create virtual environment
echo 📦 Creating virtual environment...
if exist "venv" (
    echo ⚠️  Virtual environment already exists. Removing old one...
    rmdir /s /q venv
)

python -m venv venv

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call venv\Scripts\activate.bat

REM Upgrade pip
echo ⬆️  Upgrading pip...
python -m pip install --upgrade pip

REM Install dependencies
echo 📚 Installing dependencies...
pip install -r requirements.txt

echo.
echo ✅ Installation completed successfully!
echo.
echo 🎯 To start the application:
echo    cd backend
echo    venv\Scripts\activate.bat
echo    python run.py
echo.
echo    Or simply run:
echo    start.bat
echo.
echo 🌐 The application will be available at: http://localhost:5001
echo.
echo 📖 For more information, see README.md
pause 