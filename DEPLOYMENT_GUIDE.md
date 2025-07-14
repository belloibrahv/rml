# Render Deployment Guide

This guide will walk you through deploying the Career Recommendation System to Render.

## Prerequisites

1. **GitHub Account**: Make sure your code is pushed to a GitHub repository
2. **Render Account**: Sign up at [render.com](https://render.com)

## Step-by-Step Deployment

### 1. Prepare Your Repository

Ensure your repository contains all the necessary files:
- `app.py` (main Flask application)
- `requirements.txt` (Python dependencies)
- `render.yaml` (Render configuration)
- `models/` directory (ML model files)
- `static/` and `templates/` directories

### 2. Deploy to Render

#### Option A: Using render.yaml (Recommended)

1. **Connect to Render**:
   - Go to [render.com](https://render.com)
   - Sign up/Login with your GitHub account
   - Click "New +" → "Blueprint"
   - Connect your GitHub repository

2. **Deploy**:
   - Render will automatically detect the `render.yaml` file
   - Click "Apply" to deploy
   - Your service will be created automatically

#### Option B: Manual Configuration

1. **Create Web Service**:
   - Go to [render.com](https://render.com)
   - Click "New +" → "Web Service"
   - Connect your GitHub repository

2. **Configure Settings**:
   - **Name**: `career-recommendation-app`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app --bind 0.0.0.0:$PORT`
   - **Root Directory**: Leave empty

3. **Environment Variables** (optional):
   - `FLASK_ENV`: `production`
   - `FLASK_DEBUG`: `0`

4. **Deploy**:
   - Click "Create Web Service"
   - Wait for the build to complete

### 3. Verify Deployment

1. **Check Build Logs**:
   - Monitor the build process in the Render dashboard
   - Ensure all dependencies are installed successfully

2. **Test Your Application**:
   - Visit the provided URL (e.g., `https://your-app-name.onrender.com`)
   - Test the career recommendation functionality
   - Verify all API endpoints are working

## Troubleshooting

### Common Issues

1. **Build Failures**:
   - Check that all dependencies are in `requirements.txt`
   - Ensure Python version compatibility
   - Verify file paths are correct

2. **Application Not Starting**:
   - Check the start command: `gunicorn app:app --bind 0.0.0.0:$PORT`
   - Verify `app.py` contains the Flask app instance
   - Check logs for error messages

3. **ML Models Not Loading**:
   - Ensure `models/` directory is included in the repository
   - Check file permissions
   - Verify model files are not corrupted

4. **Static Files Not Loading**:
   - Check that `static/` directory is properly configured
   - Verify file paths in templates

### Debugging Tips

1. **Check Logs**:
   - Use Render's log viewer to debug issues
   - Look for Python errors or import issues

2. **Test Locally First**:
   - Run `python app.py` locally to ensure it works
   - Test with `gunicorn app:app` locally

3. **Environment Variables**:
   - Ensure `PORT` is available (Render sets this automatically)
   - Check that `FLASK_ENV` is set to `production`

## Configuration Files

### render.yaml
```yaml
services:
  - type: web
    name: career-recommendation-app
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn app:app --bind 0.0.0.0:$PORT
    envVars:
      - key: PYTHON_VERSION
        value: 3.9.16
      - key: FLASK_ENV
        value: production
      - key: FLASK_DEBUG
        value: 0
```

### requirements.txt
```
Flask==3.0.0
Werkzeug==3.0.1
flask-cors==4.0.0
numpy==1.24.3
pandas==2.0.3
scikit-learn==1.3.0
joblib==1.3.2
gunicorn==21.2.0
```

## Post-Deployment

### Monitoring

1. **Health Checks**:
   - Monitor your application's health in the Render dashboard
   - Set up alerts for downtime

2. **Performance**:
   - Monitor response times
   - Check resource usage

3. **Updates**:
   - Push changes to GitHub to trigger automatic redeployment
   - Test changes locally before pushing

### Custom Domain (Optional)

1. **Add Custom Domain**:
   - Go to your service settings in Render
   - Add your custom domain
   - Configure DNS settings

2. **SSL Certificate**:
   - Render provides automatic SSL certificates
   - No additional configuration needed

## Support

If you encounter issues:

1. **Check Render Documentation**: [docs.render.com](https://docs.render.com)
2. **Review Logs**: Use Render's log viewer
3. **Community Support**: Render has an active community forum
4. **GitHub Issues**: Report bugs in your repository

## Success Checklist

- [ ] Application builds successfully
- [ ] All dependencies are installed
- [ ] Flask app starts without errors
- [ ] ML models load correctly
- [ ] Static files are served properly
- [ ] API endpoints respond correctly
- [ ] Career recommendation functionality works
- [ ] Application is accessible via the provided URL
- [ ] No errors in the logs

Your application should now be successfully deployed on Render! 🚀 