# 🖥️ Windows User Runbook: AI Career Recommendation System

**A Step-by-Step Guide for Non-Technical Users**

Welcome! This guide will help you set up and run the AI Career Recommendation System on your Windows computer. No technical knowledge required! 🚀

---

## 📋 What You'll Need

- **Windows 10 or 11** (Windows 7/8 will also work)
- **Internet connection** to download the project
- **About 30 minutes** of your time
- **Basic computer skills** (clicking, typing, following instructions)

---

## 🎯 What This System Does

This is an AI-powered career recommendation system that helps you discover suitable career paths based on:
- Your skills and interests
- Your education level
- Your preferred industry

It will suggest careers like Software Engineer, Doctor, Teacher, Graphic Designer, and many more!

---

## 📥 Step 1: Download the Project

### 1.1 Open Your Web Browser
- Open **Google Chrome**, **Microsoft Edge**, or **Firefox**
- Go to: https://github.com/belloibrahv/rml.git

### 1.2 Download the Project
- Click the green **"Code"** button
- Click **"Download ZIP"**
- Save the file to your **Desktop** (easier to find)

### 1.3 Extract the ZIP File
- Go to your **Desktop**
- Find the file named **"rml-main.zip"** (or similar)
- **Right-click** on it
- Select **"Extract All..."**
- Click **"Extract"**
- You'll now have a folder called **"rml-main"**

---

## 🐍 Step 2: Install Python

### 2.1 Check if Python is Already Installed
- Press **Windows key + R**
- Type **"cmd"** and press **Enter**
- In the black window, type: `python --version`
- Press **Enter**

**If you see something like "Python 3.x.x" → Skip to Step 3**
**If you see "python is not recognized" → Continue with Step 2.2**

### 2.2 Download Python
- Go to: https://www.python.org/downloads/
- Click the big **"Download Python"** button
- Save the file to your **Desktop**

### 2.3 Install Python
- Go to your **Desktop**
- Find the **Python installer** (ends with .exe)
- **Double-click** to run it
- **IMPORTANT**: Check the box that says **"Add Python to PATH"**
- Click **"Install Now"**
- Wait for installation to complete
- Click **"Close"**

---

## 🚀 Step 3: Set Up the Project

### 3.1 Open Command Prompt
- Press **Windows key + R**
- Type **"cmd"** and press **Enter**
- A black window will open

### 3.2 Navigate to the Project
In the black window, type these commands one by one (press Enter after each):

```cmd
cd Desktop
cd rml-main
```

### 3.3 Run the Installation Script
Type this command and press **Enter**:

```cmd
install.bat
```

**What will happen:**
- The script will create a virtual environment
- Install all necessary packages
- Set up everything automatically
- You'll see lots of text scrolling - this is normal!

**Wait for it to finish** (you'll see "Installation completed successfully!")

---

## 🎮 Step 4: Run the Application

### 4.1 Start the Application
In the same black window, type:

```cmd
cd backend
start.bat
```

### 4.2 What Happens Next
- A new black window will open
- You'll see text like "Starting AI Career Recommendation System"
- Wait until you see "Running on http://127.0.0.1:5001"
- **Keep this window open** (don't close it!)

### 4.3 Open the Application
- Open your **web browser** (Chrome, Edge, or Firefox)
- Type this address: `http://localhost:5001`
- Press **Enter**

**🎉 Congratulations! The application is now running!**

---

## 📝 Step 5: Using the Application

### 5.1 Fill Out the Form
You'll see a form with these fields:

1. **Name** (optional): Type your name
2. **Email** (optional): Type your email
3. **Education Level**: Click the dropdown and select your level
   - Secondary School
   - Diploma/Certificate
   - Bachelor's Degree
   - Master's Degree
   - PhD/Doctorate

4. **Skills**: Click the dropdown and select skills you have
   - You can select multiple skills
   - Examples: Programming, Communication, Leadership, etc.

5. **Interests**: Click the dropdown and select your interests
   - You can select multiple interests
   - Examples: Technology, Healthcare, Business, etc.

6. **Preferred Industry** (optional): Select an industry you prefer

### 5.2 Get Your Recommendation
- Click the **"Get Recommendation"** button
- Wait a few seconds
- Your career recommendation will appear!

### 5.3 Understanding Your Results
You'll see:
- **Primary Career**: Your best match
- **Alternative Careers**: Other good options
- **Confidence Score**: How well you match (percentage)
- **Career Details**: Salary, skills needed, growth potential

---

## 🛠️ Troubleshooting

### Problem: "Python is not recognized"
**Solution:**
- Make sure you checked "Add Python to PATH" during installation
- Restart your computer and try again
- Or reinstall Python with the PATH option checked

### Problem: "Port 5001 is in use"
**Solution:**
- Close any other applications you might have running
- Restart your computer
- Try running the application again

### Problem: "Installation failed"
**Solution:**
- Make sure you have internet connection
- Try running the installation script again
- If it still fails, try restarting your computer

### Problem: "Page not found" in browser
**Solution:**
- Make sure the black window is still open and running
- Check that you typed the address correctly: `http://localhost:5001`
- Try refreshing the page

### Problem: Application closes unexpectedly
**Solution:**
- Make sure you're running `start.bat` from the backend folder
- Check that Python is properly installed
- Try running the installation script again

---

## 🛑 How to Stop the Application

### To Stop the Application:
1. Go back to the black window that's running the application
2. Press **Ctrl + C**
3. Type **"Y"** and press **Enter**
4. The application will stop

### To Close Everything:
1. Close the black window(s)
2. You're done!

---

## 🔄 How to Run Again Later

### To Run the Application Again:
1. Press **Windows key + R**
2. Type **"cmd"** and press **Enter**
3. Type these commands:
   ```cmd
   cd Desktop
   cd rml-main
   cd backend
   start.bat
   ```
4. Open your browser and go to: `http://localhost:5001`

---

## 📞 Getting Help

### If Something Goes Wrong:
1. **Don't panic!** Most problems are easy to fix
2. **Restart your computer** - this solves many issues
3. **Follow the troubleshooting steps** above
4. **Ask for help** from someone with technical knowledge

### Common Issues and Solutions:

| Problem | Solution |
|---------|----------|
| Can't find the downloaded file | Check your Downloads folder |
| Python won't install | Make sure you're logged in as Administrator |
| Application won't start | Make sure you're in the right folder (backend) |
| Browser shows error | Make sure you typed the address correctly |
| Everything seems broken | Restart your computer and try again |

---

## 🎉 You're All Set!

You now have a working AI Career Recommendation System! 

**What you can do:**
- Get career recommendations based on your profile
- Explore different career options
- Learn about salary ranges and required skills
- Share the system with friends and family

**Remember:**
- Keep the black window open while using the application
- The application runs on your computer (no internet needed after setup)
- You can use it anytime by following the "Run Again Later" steps

**Happy career exploring! 🚀**

---

## 📱 Quick Reference Card

**To Start:**
1. Open Command Prompt
2. `cd Desktop\rml-main\backend`
3. `start.bat`
4. Open browser: `http://localhost:5001`

**To Stop:**
1. Press Ctrl + C in the black window
2. Type Y and press Enter

**If Stuck:**
1. Restart computer
2. Try again
3. Ask for help

---

*This runbook was created specifically for Windows users with no technical background. If you need help, don't hesitate to ask!* 