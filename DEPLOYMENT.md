# Deployment Guide 🚀

This guide will help you deploy the AI Career Recommendation System to various platforms.

## GitHub Deployment

### 1. Create a GitHub Repository

1. Go to [GitHub](https://github.com) and sign in
2. Click the "+" icon in the top right corner
3. Select "New repository"
4. Name your repository (e.g., `ai-career-recommendation`)
5. Make it public or private as preferred
6. **Don't** initialize with README, .gitignore, or license (we already have these)
7. Click "Create repository"

### 2. Push to GitHub

```bash
# Add the remote repository (replace with your GitHub username and repo name)
git remote add origin https://github.com/yourusername/ai-career-recommendation.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### 3. Verify Deployment

- Go to your GitHub repository
- You should see all the files uploaded
- The README.md will be displayed on the repository homepage

## Local Development Setup

### Quick Installation

**For macOS/Linux:**
```bash
# Clone the repository
git clone https://github.com/yourusername/ai-career-recommendation.git
cd ai-career-recommendation

# Run the installation script
./install.sh
```

**For Windows:**
```bash
# Clone the repository
git clone https://github.com/yourusername/ai-career-recommendation.git
cd ai-career-recommendation

# Run the installation script
install.bat
```

### Manual Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/ai-career-recommendation.git
cd ai-career-recommendation

# Navigate to backend
cd backend

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate.bat

# Install dependencies
pip install -r requirements.txt

# Run the application
python run.py
```

## Production Deployment

### Heroku Deployment

1. **Install Heroku CLI**
   ```bash
   # macOS
   brew install heroku/brew/heroku
   
   # Windows
   # Download from https://devcenter.heroku.com/articles/heroku-cli
   ```

2. **Create Heroku App**
   ```bash
   heroku login
   heroku create your-app-name
   ```

3. **Configure for Heroku**
   Create a `Procfile` in the backend directory:
   ```
   web: gunicorn app.app:app
   ```

4. **Add gunicorn to requirements.txt**
   ```
   gunicorn==20.1.0
   ```

5. **Deploy**
   ```bash
   cd backend
   git add .
   git commit -m "Add Heroku configuration"
   git push heroku main
   ```

### Docker Deployment

1. **Create Dockerfile** in the backend directory:
   ```dockerfile
   FROM python:3.11-slim
   
   WORKDIR /app
   
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   
   COPY . .
   
   EXPOSE 5001
   
   CMD ["python", "run.py"]
   ```

2. **Build and Run**
   ```bash
   cd backend
   docker build -t career-recommendation .
   docker run -p 5001:5001 career-recommendation
   ```

### VPS Deployment

1. **Set up your VPS** (Ubuntu recommended)
2. **Install dependencies**
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip python3-venv nginx
   ```

3. **Clone and set up the application**
   ```bash
   git clone https://github.com/yourusername/ai-career-recommendation.git
   cd ai-career-recommendation/backend
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

4. **Set up systemd service**
   Create `/etc/systemd/system/career-recommendation.service`:
   ```ini
   [Unit]
   Description=AI Career Recommendation System
   After=network.target
   
   [Service]
   User=www-data
   WorkingDirectory=/path/to/your/app/backend
   Environment="PATH=/path/to/your/app/backend/venv/bin"
   ExecStart=/path/to/your/app/backend/venv/bin/python run.py
   Restart=always
   
   [Install]
   WantedBy=multi-user.target
   ```

5. **Start the service**
   ```bash
   sudo systemctl enable career-recommendation
   sudo systemctl start career-recommendation
   ```

## Environment Variables

For production deployment, consider setting these environment variables:

```bash
export FLASK_ENV=production
export FLASK_DEBUG=0
export PORT=5001
export DATABASE_URL=your_database_url
```

## Security Considerations

1. **HTTPS**: Always use HTTPS in production
2. **Environment Variables**: Store sensitive data in environment variables
3. **Database**: Use a production database (PostgreSQL, MySQL) instead of SQLite
4. **Logging**: Implement proper logging for production
5. **Rate Limiting**: Add rate limiting for API endpoints
6. **Input Validation**: Ensure all user inputs are properly validated

## Monitoring

### Health Check Endpoint

Add a health check endpoint to your Flask app:

```python
@app.route("/health")
def health_check():
    return jsonify({"status": "healthy", "timestamp": datetime.now().isoformat()})
```

### Logging

Implement structured logging:

```python
import logging
from logging.handlers import RotatingFileHandler

if not app.debug:
    file_handler = RotatingFileHandler('logs/career_recommendation.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('Career Recommendation System startup')
```

## Troubleshooting

### Common Issues

1. **Port Already in Use**
   ```bash
   # Find process using port 5001
   lsof -i :5001
   # Kill the process
   kill -9 <PID>
   ```

2. **Permission Denied**
   ```bash
   # Make scripts executable
   chmod +x *.sh
   ```

3. **Database Issues**
   ```bash
   # Remove and recreate database
   rm career_reco.db
   python run.py
   ```

4. **Dependencies Issues**
   ```bash
   # Reinstall dependencies
   pip install -r requirements.txt --force-reinstall
   ```

## Support

If you encounter deployment issues:

1. Check the troubleshooting section above
2. Review the logs for error messages
3. Ensure all dependencies are installed correctly
4. Verify your Python version (3.8+ required)
5. Check that all required files are present

For additional help, create an issue in the GitHub repository with:
- Your operating system
- Python version
- Error messages
- Steps to reproduce the issue 