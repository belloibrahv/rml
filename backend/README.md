# Career Recommendation System Backend

This is the backend API for the Career Recommendation System, built with FastAPI.

## Features

- Career prediction based on skills, interests, and education
- Feature importance analysis
- Alternative career suggestions
- Confidence scoring
- RESTful API endpoints

## Project Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI application
│   ├── config/          # Configuration files
│   │   └── settings.py  # Application settings
│   ├── models/          # Database models
│   ├── routers/         # API routes
│   │   └── predict.py   # Prediction endpoints
│   ├── services/        # Business logic
│   │   └── predictor.py # Career prediction service
│   └── utils/           # Utility functions
├── requirements.txt     # Backend dependencies
└── README.md           # This file
```

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the API:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

Swagger UI: `http://localhost:8000/docs`

ReDoc: `http://localhost:8000/redoc`

## Endpoints

- `POST /predict/career` - Get career recommendation
- `GET /predict/careers` - List available careers
- `GET /predict/skills` - List available skills
- `GET /predict/interests` - List available interests

## Environment Variables

The application uses the following environment variables:

- `API_V1_STR`: API version prefix
- `PROJECT_NAME`: Project name
- `VERSION`: API version
- `MODEL_PATH`: Path to the trained model
- `LABEL_ENCODER_PATH`: Path to the label encoder
- `SKILLS_ENCODER_PATH`: Path to the skills encoder
- `INTERESTS_ENCODER_PATH`: Path to the interests encoder
- `DATABASE_URL`: Database connection URL
