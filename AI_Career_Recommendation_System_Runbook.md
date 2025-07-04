# AI Career Recommendation System - Complete Runbook
## From Setup to Deployment on Windows

---

## 📋 Table of Contents
1. [Prerequisites](#prerequisites)
2. [System Overview](#system-overview)
3. [Installation Guide](#installation-guide)
4. [Backend Setup](#backend-setup)
5. [Frontend Setup](#frontend-setup)
6. [Database Setup](#database-setup)
7. [Running the System](#running-the-system)
8. [Testing the System](#testing-the-system)
9. [Troubleshooting](#troubleshooting)
10. [Deployment](#deployment)
11. [Maintenance](#maintenance)
12. [FAQs](#faqs)

---

## 🎯 Prerequisites

### For Beginners (No Programming Experience)
- **Windows 10 or 11** (64-bit)
- **Internet connection** for downloading software
- **Basic computer skills** (downloading, installing, running programs)
- **Patience** - First setup may take 30-60 minutes

### For Intermediate Users
- Basic understanding of command line
- Familiarity with web browsers
- Knowledge of file systems

### For Advanced Users
- Python programming experience
- Web development knowledge
- Database management skills

### Required Software
1. **Python 3.8 or higher** - [Download Here](https://www.python.org/downloads/)
2. **Node.js 16 or higher** - [Download Here](https://nodejs.org/)
3. **Git** - [Download Here](https://git-scm.com/)
4. **Visual Studio Code** (Recommended) - [Download Here](https://code.visualstudio.com/)

---

## 🏗️ System Overview

### What This System Does
- **Input**: User provides age, education, skills, and interests
- **Process**: AI analyzes the data using machine learning
- **Output**: Personalized career recommendations with confidence scores

### System Architecture
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │   Backend       │    │   Database      │
│   (Next.js)     │◄──►│   (FastAPI)     │◄──►│   (SQLite)      │
│   Port: 3000    │    │   Port: 8000    │    │   Local File    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### What You'll Be Running
1. **Backend Server** - Handles AI predictions and data processing
2. **Frontend Website** - User interface for input and results
3. **Database** - Stores career data and user information

---

## 🚀 Installation Guide

### Step 1: Download the Project

#### Option A: Using Git (Recommended)
```bash
# Open Command Prompt as Administrator
# Navigate to your desired folder (e.g., C:\Projects)
cd C:\Projects

# Clone the project
git clone https://github.com/your-username/ai-career-recommendation.git

# Navigate into the project folder
cd ai-career-recommendation
```

#### Option B: Manual Download
1. Download the project ZIP file
2. Extract to `C:\Projects\ai-career-recommendation`
3. Open Command Prompt in the extracted folder

### Step 2: Verify Prerequisites

#### Check Python Installation
```bash
python --version
# Should show Python 3.8 or higher
```

#### Check Node.js Installation
```bash
node --version
# Should show v16 or higher
```

#### Check Git Installation
```bash
git --version
# Should show Git version
```

### Step 3: Project Structure
After installation, your folder should look like this:
```
ai-career-recommendation/
├── backend/
│   ├── app/
│   ├── requirements.txt
│   └── venv/
├── career-reco-frontend/
│   ├── src/
│   ├── package.json
│   └── next.config.ts
├── data.csv
└── README.md
```

---

## ⚙️ Backend Setup

### Step 1: Navigate to Backend Directory
```bash
cd backend
```

### Step 2: Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# You should see (venv) at the beginning of your command line
```

### Step 3: Install Python Dependencies
```bash
# Upgrade pip first
python -m pip install --upgrade pip

# Install required packages
pip install -r requirements.txt
```

**Expected Output:**
```
Collecting fastapi==0.115.13
  Downloading fastapi-0.115.13-py3-none-any.whl (92 kB)
...
Successfully installed fastapi-0.115.13 uvicorn-0.32.1 ...
```

### Step 4: Verify Backend Installation
```bash
# Check if all packages are installed
pip list

# Should show packages like:
# fastapi
# uvicorn
# scikit-learn
# pandas
# numpy
# joblib
```

### Step 5: Test Backend Setup
```bash
# Start the backend server
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Expected Output:**
```
INFO:     Will watch for changes in these directories: ['C:\\...\\backend']
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [12345] using StatReload
INFO:     Started server process [12346]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

### Step 6: Test Backend API
1. Open your web browser
2. Go to: `http://localhost:8000/docs`
3. You should see the FastAPI documentation page
4. Click "Try it out" on any endpoint to test

---

## 🎨 Frontend Setup

### Step 1: Navigate to Frontend Directory
```bash
# Open a new Command Prompt window
cd C:\Projects\ai-career-recommendation\career-reco-frontend
```

### Step 2: Install Node.js Dependencies
```bash
# Install all required packages
npm install
```

**Expected Output:**
```
added 1234 packages, and audited 1235 packages in 2m
found 0 vulnerabilities
```

### Step 3: Verify Frontend Installation
```bash
# Check if packages are installed
npm list --depth=0

# Should show packages like:
# next
# react
# typescript
# tailwindcss
```

### Step 4: Test Frontend Setup
```bash
# Start the frontend development server
npm run dev
```

**Expected Output:**
```
> career-reco-frontend@0.1.0 dev
> next dev

- ready started server on 0.0.0.0:3000, url: http://localhost:3000
- event compiled client and server successfully in 2.3s
```

### Step 5: Test Frontend Website
1. Open your web browser
2. Go to: `http://localhost:3000`
3. You should see the career recommendation homepage
4. Click "Get Started" to test the form

---

## 🗄️ Database Setup

### Step 1: Verify Database Files
The system uses SQLite, which is file-based and doesn't require separate installation.

```bash
# Navigate to backend directory
cd C:\Projects\ai-career-recommendation\backend

# Check if database file exists
dir app\db\career_reco.db
```

### Step 2: Initialize Database (If Needed)
```bash
# Run database initialization script
python scripts\init_db.py
```

### Step 3: Load Sample Data
```bash
# Load career data and models
python scripts\load_models.py
```

---

## 🏃‍♂️ Running the System

### Method 1: Manual Start (Recommended for Development)

#### Terminal 1: Backend Server
```bash
# Navigate to backend directory
cd C:\Projects\ai-career-recommendation\backend

# Activate virtual environment
venv\Scripts\activate

# Start backend server
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

#### Terminal 2: Frontend Server
```bash
# Open new Command Prompt
# Navigate to frontend directory
cd C:\Projects\ai-career-recommendation\career-reco-frontend

# Start frontend server
npm run dev
```

### Method 2: Batch Script (Easier for Beginners)

#### Create Start Script
1. Create a new file: `start_system.bat`
2. Add the following content:

```batch
@echo off
echo Starting AI Career Recommendation System...
echo.

echo Starting Backend Server...
cd /d C:\Projects\ai-career-recommendation\backend
call venv\Scripts\activate
start "Backend Server" cmd /k "python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000"

echo Starting Frontend Server...
cd /d C:\Projects\ai-career-recommendation\career-reco-frontend
start "Frontend Server" cmd /k "npm run dev"

echo.
echo System is starting up...
echo Backend: http://localhost:8000
echo Frontend: http://localhost:3000
echo.
echo Press any key to open the website...
pause >nul
start http://localhost:3000
```

3. Save the file in your project root directory
4. Double-click `start_system.bat` to run

### Method 3: Using Visual Studio Code

1. Open VS Code
2. Open the project folder: `File > Open Folder > ai-career-recommendation`
3. Open Terminal: `Terminal > New Terminal`
4. Run the following commands:

```bash
# Terminal 1: Backend
cd backend
venv\Scripts\activate
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

```bash
# Terminal 2: Frontend
cd career-reco-frontend
npm run dev
```

---

## 🧪 Testing the System

### Step 1: Verify Both Servers Are Running

#### Check Backend (Terminal 1)
```bash
# Should show:
INFO:     Uvicorn running on http://0.0.0.0:8000
```

#### Check Frontend (Terminal 2)
```bash
# Should show:
- ready started server on 0.0.0.0:3000
```

### Step 2: Test Backend API
1. Open browser: `http://localhost:8000/docs`
2. Click "Try it out" on `/model/skills`
3. Click "Execute"
4. Should return a list of skills

### Step 3: Test Frontend Website
1. Open browser: `http://localhost:3000`
2. Click "Get Started" or "Get Recommendation"
3. Fill out the form:
   - Age: 25
   - Education: Bachelor's
   - Skills: Python, Machine Learning
   - Interests: Technology, Research
4. Click "Get Recommendation"
5. Should show career recommendations

### Step 4: Test Complete Workflow
1. Go to: `http://localhost:3000/recommend/form`
2. Fill the form completely
3. Submit and verify results
4. Check that confidence scores are displayed
5. Verify feature importance is shown

---

## 🔧 Troubleshooting

### Common Issues and Solutions

#### Issue 1: "Python is not recognized"
**Solution:**
```bash
# Reinstall Python and check "Add to PATH"
# Or manually add Python to PATH:
# 1. Open System Properties > Environment Variables
# 2. Add C:\Python39\ and C:\Python39\Scripts\ to PATH
```

#### Issue 2: "Node is not recognized"
**Solution:**
```bash
# Reinstall Node.js and check "Add to PATH"
# Or restart Command Prompt after installation
```

#### Issue 3: "Port 8000 is already in use"
**Solution:**
```bash
# Find process using port 8000
netstat -ano | findstr :8000

# Kill the process (replace XXXX with PID)
taskkill /PID XXXX /F

# Or use a different port:
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8001
```

#### Issue 4: "Port 3000 is already in use"
**Solution:**
```bash
# Find process using port 3000
netstat -ano | findstr :3000

# Kill the process (replace XXXX with PID)
taskkill /PID XXXX /F

# Or use a different port:
npm run dev -- -p 3001
```

#### Issue 5: "Module not found" errors
**Solution:**
```bash
# Backend: Reinstall dependencies
cd backend
venv\Scripts\activate
pip install -r requirements.txt

# Frontend: Reinstall dependencies
cd career-reco-frontend
npm install
```

#### Issue 6: "Database connection error"
**Solution:**
```bash
# Check if database file exists
dir backend\app\db\career_reco.db

# If not, run initialization:
cd backend
python scripts\init_db.py
python scripts\load_models.py
```

#### Issue 7: "Model loading error"
**Solution:**
```bash
# Check if model files exist
dir backend\app\models\*.pkl

# If not, retrain models:
cd backend
python enhanced_train_model.py
```

#### Issue 8: "CORS error" in browser
**Solution:**
```bash
# Check if backend is running on correct port
# Ensure frontend is calling correct backend URL
# Check browser console for specific error
```

#### Issue 9: "Slow performance"
**Solution:**
```bash
# Check system resources
# Close unnecessary applications
# Restart servers
# Check for memory leaks
```

#### Issue 10: "Cannot access website"
**Solution:**
```bash
# Check if servers are running
# Verify ports are correct
# Check Windows Firewall
# Try accessing via IP: http://127.0.0.1:3000
```

### Advanced Troubleshooting

#### Check System Logs
```bash
# Backend logs are in the terminal
# Frontend logs are in the terminal
# Check browser console (F12) for frontend errors
```

#### Verify Network Configuration
```bash
# Test localhost connectivity
ping localhost

# Test port connectivity
telnet localhost 8000
telnet localhost 3000
```

#### Reset Everything
```bash
# Stop all servers (Ctrl+C)
# Delete node_modules and reinstall
cd career-reco-frontend
rmdir /s node_modules
npm install

# Delete venv and recreate
cd ..\backend
rmdir /s venv
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🚀 Deployment

### Local Production Setup

#### Step 1: Build Frontend for Production
```bash
cd career-reco-frontend
npm run build
```

#### Step 2: Start Production Servers
```bash
# Backend (Production)
cd backend
venv\Scripts\activate
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000

# Frontend (Production)
cd career-reco-frontend
npm start
```

### Windows Service Setup (Advanced)

#### Create Windows Service for Backend
1. Install NSSM: `choco install nssm`
2. Create service:
```bash
nssm install CareerRecommendationBackend "C:\Projects\ai-career-recommendation\backend\venv\Scripts\python.exe" "-m uvicorn app.main:app --host 0.0.0.0 --port 8000"
nssm set CareerRecommendationBackend AppDirectory "C:\Projects\ai-career-recommendation\backend"
```

#### Create Windows Service for Frontend
```bash
nssm install CareerRecommendationFrontend "C:\Program Files\nodejs\node.exe" "C:\Projects\ai-career-recommendation\career-reco-frontend\node_modules\.bin\next start"
nssm set CareerRecommendationFrontend AppDirectory "C:\Projects\ai-career-recommendation\career-reco-frontend"
```

### Cloud Deployment (Advanced)

#### Deploy to Azure
1. Create Azure App Service
2. Configure deployment slots
3. Set up CI/CD pipeline
4. Configure environment variables

#### Deploy to AWS
1. Create EC2 instance
2. Install required software
3. Configure security groups
4. Set up load balancer

---

## 🔄 Maintenance

### Daily Operations

#### Start System
```bash
# Use start_system.bat or manual commands
```

#### Monitor System
```bash
# Check if servers are running
netstat -ano | findstr :8000
netstat -ano | findstr :3000

# Check system resources
tasklist | findstr python
tasklist | findstr node
```

#### Stop System
```bash
# Press Ctrl+C in each terminal
# Or kill processes:
taskkill /F /IM python.exe
taskkill /F /IM node.exe
```

### Weekly Maintenance

#### Update Dependencies
```bash
# Backend
cd backend
venv\Scripts\activate
pip install --upgrade pip
pip install --upgrade -r requirements.txt

# Frontend
cd career-reco-frontend
npm update
```

#### Backup Database
```bash
# Copy database file
copy backend\app\db\career_reco.db backup\career_reco_%date%.db
```

#### Check Logs
```bash
# Review terminal outputs
# Check for errors
# Monitor performance
```

### Monthly Maintenance

#### System Updates
```bash
# Update Python
python -m pip install --upgrade pip

# Update Node.js (download new version)
# Update system packages
```

#### Performance Optimization
```bash
# Clean up temporary files
# Optimize database
# Review and update models
```

#### Security Updates
```bash
# Update dependencies
# Review security patches
# Update SSL certificates
```

---

## ❓ FAQs

### For Beginners

**Q: What if I don't know programming?**
A: This runbook is designed for non-programmers. Follow the step-by-step instructions and use the batch script for easy startup.

**Q: How long does setup take?**
A: First-time setup: 30-60 minutes. Subsequent runs: 2-3 minutes.

**Q: What if something doesn't work?**
A: Check the troubleshooting section. Most issues are common and have simple solutions.

**Q: Can I run this on any Windows computer?**
A: Yes, as long as it meets the prerequisites (Windows 10/11, 4GB RAM minimum).

**Q: Do I need internet to run the system?**
A: Only for initial setup and updates. The system runs locally once installed.

### For Intermediate Users

**Q: How do I customize the system?**
A: Modify the code in `backend/app/` and `career-reco-frontend/src/` directories.

**Q: Can I add new careers?**
A: Yes, edit the career data in `backend/app/models/` and retrain the model.

**Q: How do I change the port numbers?**
A: Modify the port in the startup commands or configuration files.

**Q: Can I use a different database?**
A: Yes, modify the database configuration in `backend/app/database/`.

### For Advanced Users

**Q: How do I deploy to production?**
A: See the deployment section for cloud deployment options.

**Q: Can I integrate with external APIs?**
A: Yes, add API integrations in `backend/app/services/`.

**Q: How do I optimize performance?**
A: Use caching, database optimization, and load balancing techniques.

**Q: Can I add authentication?**
A: Yes, implement JWT or OAuth in the backend services.

### Technical Questions

**Q: What's the system architecture?**
A: Three-tier: Frontend (Next.js) → Backend (FastAPI) → Database (SQLite).

**Q: How does the AI work?**
A: Random Forest algorithm trained on career data with feature engineering.

**Q: What's the accuracy of predictions?**
A: 87.3% accuracy based on test data.

**Q: Can I retrain the model?**
A: Yes, use `enhanced_train_model.py` with new data.

**Q: How do I backup the system?**
A: Backup the entire project folder and database file.

---

## 📞 Support

### Getting Help

1. **Check this runbook first** - Most issues are covered here
2. **Check the troubleshooting section** - Common solutions provided
3. **Review error messages** - They often contain the solution
4. **Search online** - Use error messages as search terms
5. **Ask for help** - Provide error messages and system details

### Useful Commands

```bash
# Check system status
netstat -ano | findstr :8000
netstat -ano | findstr :3000

# Check Python version
python --version

# Check Node.js version
node --version

# Check disk space
dir

# Check memory usage
tasklist | findstr python
tasklist | findstr node
```

### Emergency Reset

If everything stops working:

```bash
# 1. Stop all processes
taskkill /F /IM python.exe
taskkill /F /IM node.exe

# 2. Restart Command Prompt as Administrator

# 3. Navigate to project
cd C:\Projects\ai-career-recommendation

# 4. Reinstall everything
cd backend
rmdir /s venv
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

cd ..\career-reco-frontend
rmdir /s node_modules
npm install

# 5. Start system
cd ..\backend
venv\Scripts\activate
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# 6. New terminal for frontend
cd ..\career-reco-frontend
npm run dev
```

---

## 🎉 Congratulations!

You've successfully set up and are running the AI Career Recommendation System! 

### What You Can Do Now:
- ✅ Get career recommendations for yourself
- ✅ Test the system with different inputs
- ✅ Customize the interface
- ✅ Add new career data
- ✅ Deploy to production
- ✅ Share with others

### Next Steps:
1. **Explore the system** - Try different inputs and see results
2. **Customize** - Modify the interface or add features
3. **Deploy** - Set up for production use
4. **Maintain** - Keep the system updated and running
5. **Improve** - Add new features or enhance existing ones

### Remember:
- Keep the system updated
- Backup your data regularly
- Monitor performance
- Document any customizations
- Share feedback and improvements

**Happy Career Planning! 🚀** 