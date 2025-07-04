@echo off
title AI Career Recommendation System - Startup Script
color 0A

echo.
echo ========================================
echo   AI Career Recommendation System
echo   Complete Startup Script
echo ========================================
echo.

:: Check if we're in the right directory
if not exist "backend" (
    echo ERROR: Backend directory not found!
    echo Please run this script from the project root directory.
    echo.
    pause
    exit /b 1
)

if not exist "career-reco-frontend" (
    echo ERROR: Frontend directory not found!
    echo Please run this script from the project root directory.
    echo.
    pause
    exit /b 1
)

echo Checking prerequisites...
echo.

:: Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH!
    echo Please install Python 3.8 or higher from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation.
    echo.
    pause
    exit /b 1
) else (
    echo ✓ Python found
)

:: Check Node.js
node --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Node.js is not installed or not in PATH!
    echo Please install Node.js 16 or higher from https://nodejs.org/
    echo.
    pause
    exit /b 1
) else (
    echo ✓ Node.js found
)

echo.
echo Prerequisites check completed successfully!
echo.

:: Check if virtual environment exists
if not exist "backend\venv" (
    echo Setting up backend virtual environment...
    cd backend
    python -m venv venv
    call venv\Scripts\activate
    echo Installing Python dependencies...
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    cd ..
    echo ✓ Backend environment setup complete
    echo.
) else (
    echo ✓ Backend virtual environment found
)

:: Check if node_modules exists
if not exist "career-reco-frontend\node_modules" (
    echo Setting up frontend dependencies...
    cd career-reco-frontend
    npm install
    cd ..
    echo ✓ Frontend dependencies setup complete
    echo.
) else (
    echo ✓ Frontend dependencies found
)

echo.
echo Starting servers...
echo.

:: Start Backend Server
echo Starting Backend Server (Port 8000)...
cd backend
call venv\Scripts\activate
start "AI Career Recommendation - Backend Server" cmd /k "echo Backend Server Running on http://localhost:8000 && echo Press Ctrl+C to stop && python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000"
cd ..

:: Wait a moment for backend to start
timeout /t 3 /nobreak >nul

:: Start Frontend Server
echo Starting Frontend Server (Port 3000)...
cd career-reco-frontend
start "AI Career Recommendation - Frontend Server" cmd /k "echo Frontend Server Running on http://localhost:3000 && echo Press Ctrl+C to stop && npm run dev"
cd ..

echo.
echo ========================================
echo   System Startup Complete!
echo ========================================
echo.
echo Backend Server:  http://localhost:8000
echo Frontend Server: http://localhost:3000
echo API Documentation: http://localhost:8000/docs
echo.
echo Both servers are now running in separate windows.
echo.
echo To stop the system:
echo 1. Press Ctrl+C in each server window, OR
echo 2. Close the server windows
echo.
echo Press any key to open the website in your browser...
pause >nul

:: Open the website
start http://localhost:3000

echo.
echo Website opened in your default browser!
echo.
echo If you need to restart the system:
echo 1. Close all server windows
echo 2. Run this script again
echo.
echo Enjoy using the AI Career Recommendation System!
echo.
pause 