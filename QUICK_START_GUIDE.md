# 🚀 Quick Start Guide - AI Career Recommendation System

## ⚡ Get Running in 5 Minutes

### Prerequisites (One-time setup)
1. **Install Python 3.8+**: [Download Here](https://www.python.org/downloads/) ✅ Check "Add to PATH"
2. **Install Node.js 16+**: [Download Here](https://nodejs.org/) ✅ Check "Add to PATH"
3. **Download the project**: Extract to `C:\Projects\ai-career-recommendation`

### 🎯 Super Quick Start (Windows)

#### Option 1: One-Click Start (Easiest)
1. Double-click `start_system.bat`
2. Wait for both servers to start
3. Website opens automatically at `http://localhost:3000`
4. **Done!** 🎉

#### Option 2: Manual Start (If batch file doesn't work)

**Step 1: Start Backend**
```bash
cd backend
venv\Scripts\activate
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Step 2: Start Frontend (New Command Prompt)**
```bash
cd career-reco-frontend
npm run dev
```

**Step 3: Open Website**
- Go to: `http://localhost:3000`
- Click "Get Started"
- Fill the form and get recommendations!

### 🧪 Test the System
1. Go to `http://localhost:3000/recommend/form`
2. Fill out the form:
   - Age: 25
   - Education: Bachelor's
   - Skills: Python, Machine Learning
   - Interests: Technology, Research
3. Click "Get Recommendation"
4. See your personalized career suggestions!

### 🛑 Stop the System
- Press `Ctrl+C` in each server window
- Or close the server windows

### 🔧 If Something Goes Wrong
1. **Port already in use**: Close other applications or restart computer
2. **Python/Node not found**: Reinstall and check "Add to PATH"
3. **Module errors**: Run `pip install -r requirements.txt` in backend folder
4. **Still stuck**: Check the full runbook: `AI_Career_Recommendation_System_Runbook.md`

### 📞 Need Help?
- Check the troubleshooting section in the full runbook
- Look at the error messages - they often tell you what's wrong
- Make sure both servers are running (you should see 2 command windows)

### 🎉 Success Indicators
✅ Backend shows: `Uvicorn running on http://0.0.0.0:8000`  
✅ Frontend shows: `ready started server on 0.0.0.0:3000`  
✅ Website loads at `http://localhost:3000`  
✅ Form submission returns career recommendations  

---

## 🚀 You're Ready to Go!

The AI Career Recommendation System is now running and ready to help you find your perfect career path! 

**Happy Career Planning! 🎯** 