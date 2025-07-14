# Career Recommendation System

A Flask-based web application that provides personalized career recommendations based on user skills, interests, and education level.

## Features

- **Personalized Career Recommendations**: Get career suggestions based on your skills, interests, and education level
- **Alternative Career Options**: Discover multiple career paths that match your profile
- **Detailed Career Information**: Access comprehensive details about each career including salary ranges, required skills, and growth potential
- **Confidence Scoring**: Understand how well each recommendation matches your profile
- **Modern Web Interface**: Clean and responsive design for optimal user experience

## Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Machine Learning**: scikit-learn, joblib
- **Data Processing**: pandas, numpy
- **Deployment**: Render (Cloud Platform)

## Local Development

### Prerequisites

- Python 3.9 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd rml
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

5. Open your browser and navigate to `http://localhost:5000`

## Deployment

### Render Deployment

This application is configured for deployment on Render. Follow these steps:

1. **Fork or clone** this repository to your GitHub account

2. **Sign up/Login** to [Render](https://render.com)

3. **Create a new Web Service**:
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Select the repository containing this project

4. **Configure the service**:
   - **Name**: `career-recommendation-app` (or your preferred name)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app --bind 0.0.0.0:$PORT`
   - **Root Directory**: Leave empty (or specify if your app is in a subdirectory)

5. **Environment Variables** (optional):
   - `FLASK_ENV`: `production`
   - `FLASK_DEBUG`: `0`

6. **Deploy**: Click "Create Web Service"

The application will be automatically deployed and available at the provided URL.

### Alternative Deployment Options

#### Vercel Deployment

The project includes `vercel.json` configuration for Vercel deployment:

1. Install Vercel CLI: `npm i -g vercel`
2. Run: `vercel` in the project directory
3. Follow the prompts to deploy

#### Heroku Deployment

1. Create a `Procfile`:
```
web: gunicorn app:app
```

2. Deploy using Heroku CLI or GitHub integration

## API Endpoints

- `GET /` - Home page
- `GET /recommend` - Recommendation form page
- `GET /about` - About page
- `POST /api/recommend` - Get career recommendations
- `GET /api/careers` - Get all available careers
- `GET /api/education-levels` - Get education levels
- `GET /api/skills` - Get available skills
- `GET /api/interests` - Get available interests

## Project Structure

```
rml/
├── app.py                 # Main Flask application
├── api/
│   └── index.py          # API endpoint for Vercel
├── models/               # ML model files
│   ├── career_recommendation_model.pkl
│   ├── career_label_encoder.pkl
│   ├── skills_mlb.pkl
│   └── interests_mlb.pkl
├── static/               # Static files (CSS, JS)
├── templates/            # HTML templates
├── requirements.txt      # Python dependencies
├── render.yaml          # Render deployment config
├── vercel.json          # Vercel deployment config
└── README.md           # This file
```

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -am 'Add feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support or questions, please open an issue in the GitHub repository. 
