# AI-Powered Career Recommendation System 🚀

A comprehensive career recommendation system that helps users discover suitable career paths based on their skills, interests, education level, and preferred industry. Built with Flask backend and modern HTML/CSS/JavaScript frontend.

## 🌟 Features

### Core Functionality
- **Intelligent Career Matching**: Rule-based recommendation system that analyzes skills, interests, and education level
- **Multi-Industry Support**: Covers Technology, Healthcare, Business, Education, Creative Arts, and Engineering
- **Education Level Compatibility**: Recommendations tailored to Secondary School, Diploma, Bachelor's, Master's, and PhD levels
- **Detailed Career Information**: Salary ranges (in Naira), required skills, growth potential, and job descriptions
- **Alternative Career Suggestions**: Provides backup career options based on user profile
- **Confidence Scoring**: Shows recommendation confidence based on input quality

### User Experience
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Interactive Form**: Easy-to-use interface with skill and interest selection
- **Real-time Validation**: Form validation and error handling
- **Detailed Results**: Comprehensive career recommendations with actionable insights

### Technical Features
- **Flask Backend**: Robust Python backend with RESTful API
- **SQLite Database**: Lightweight database for storing recommendations
- **Rule-based AI**: Reliable recommendation engine without external dependencies
- **Error Handling**: Comprehensive error handling and fallback mechanisms
- **Logging**: Detailed logging for debugging and monitoring

## 🏗️ Project Structure

```
rml/
├── backend/
│   ├── app/
│   │   ├── app.py              # Main Flask application
│   │   │   ├── index.html      # Landing page
│   │   │   ├── recommend.html  # Recommendation form
│   │   │   └── about.html      # About page
│   │   └── static/             # CSS, JS, and assets
│   ├── run.py                  # Application entry point
│   ├── requirements.txt        # Python dependencies
│   ├── start.sh               # Linux/Mac startup script
│   ├── start.bat              # Windows startup script
│   └── README.md              # Backend documentation
├── career_reco.db             # SQLite database
└── README.md                  # This file
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Git

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/belloibrahv/rml.git
   cd ai-career-recommendation
   ```

2. **Navigate to Backend Directory**
   ```bash
   cd backend
   ```

3. **Create Virtual Environment**
   ```bash
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   
   # On Windows
   python -m venv venv
   venv\Scripts\activate
   ```

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Application**
   ```bash
   # Using Python directly
   python run.py
   
   # Or using the provided scripts
   # On macOS/Linux
   chmod +x start.sh
   ./start.sh
   
   # On Windows
   start.bat
   ```

6. **Access the Application**
   - Open your web browser
   - Navigate to: `http://localhost:5001`
   - The application will be ready to use!

## 📋 Usage Guide

### Getting Career Recommendations

1. **Fill Out the Form**
   - Enter your name and email (optional)
   - Select your education level
   - Choose relevant skills from the dropdown
   - Select your interests
   - Optionally specify a preferred industry

2. **Submit and Get Results**
   - Click "Get Recommendation"
   - View your personalized career recommendation
   - Explore alternative career options
   - Check confidence score and detailed information

3. **Understanding Results**
   - **Primary Career**: Your best match based on inputs
   - **Alternative Careers**: Backup options to consider
   - **Confidence Score**: How well your profile matches the recommendation
   - **Career Details**: Salary range, required skills, growth potential

### Supported Education Levels
- Secondary School
- Diploma/Certificate
- Bachelor's Degree
- Master's Degree
- PhD/Doctorate

### Available Industries
- **Technology**: Software Engineering, Data Science, Web Development, Cybersecurity
- **Healthcare**: Medical Doctor, Nursing, Pharmacy
- **Business**: Business Analysis, Marketing, Finance
- **Education**: Teaching, School Administration
- **Creative Arts**: Graphic Design, Content Writing, Digital Marketing
- **Engineering**: Civil, Mechanical, Electrical Engineering

## 🛠️ Development

### Running in Development Mode
```bash
cd backend
python run.py
```

The application runs in debug mode by default, which enables:
- Auto-reload on code changes
- Detailed error messages
- Development server features

### Database
The application uses SQLite for data storage:
- Database file: `career_reco.db`
- Automatically created on first run
- Stores user recommendations and analytics

### API Endpoints
- `GET /` - Landing page
- `GET /recommend` - Recommendation form
- `GET /about` - About page
- `POST /api/recommend` - Get career recommendations
- `GET /api/careers` - List all careers
- `GET /api/education-levels` - List education levels
- `GET /api/skills` - List available skills
- `GET /api/interests` - List available interests

## 🔧 Configuration

### Port Configuration
The application runs on port 5001 by default. To change the port:
1. Edit `backend/run.py`
2. Modify the port number in the `app.run()` call
3. Restart the application

### Database Configuration
The SQLite database is automatically configured. For production use, consider:
- Using PostgreSQL or MySQL
- Implementing proper database migrations
- Setting up database backups

## 🐛 Troubleshooting

### Common Issues

**Port Already in Use**
```bash
# Kill existing process on port 5001
lsof -ti:5001 | xargs kill -9
# Or change port in run.py
```

**Dependencies Not Found**
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

**Virtual Environment Issues**
```bash
# Recreate virtual environment
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Database Issues**
```bash
# Remove and recreate database
rm career_reco.db
python run.py
```

## 📊 Features in Detail

### Career Database
The system includes 18 detailed career profiles across 6 industries:
- **Salary Information**: All salaries displayed in Nigerian Naira (₦)
- **Education Requirements**: Specific education levels for each career
- **Required Skills**: Key skills needed for success
- **Growth Potential**: Career growth prospects (High, Medium, Very High)

### Recommendation Algorithm
- **Skill Matching**: Analyzes user skills against career requirements
- **Interest Alignment**: Matches user interests with career fields
- **Education Compatibility**: Ensures recommendations match education level
- **Industry Preference**: Considers user's preferred industry
- **Fallback Logic**: Provides sensible defaults when exact matches aren't found

### User Interface
- **Responsive Design**: Works on all device sizes
- **Modern UI**: Clean, professional interface
- **Interactive Elements**: Dropdowns, checkboxes, and form validation
- **Result Display**: Clear, organized presentation of recommendations

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes**
4. **Test thoroughly**
5. **Commit your changes**: `git commit -m 'Add amazing feature'`
6. **Push to the branch**: `git push origin feature/amazing-feature`
7. **Open a Pull Request**

### Development Guidelines
- Follow PEP 8 Python style guidelines
- Add comments for complex logic
- Include error handling
- Test your changes before submitting

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with Flask and modern web technologies
- Career data sourced from industry research
- UI/UX inspired by modern web design principles
- Special thanks to the open-source community

## 📞 Support

If you encounter any issues or have questions:
1. Check the troubleshooting section above
2. Search existing issues in the GitHub repository
3. Create a new issue with detailed information
4. Include your operating system, Python version, and error messages

## 🔮 Future Enhancements

Planned features for future releases:
- Machine learning model integration
- User accounts and recommendation history
- Advanced analytics and insights
- Mobile app version
- Multi-language support
- Integration with job boards
- Career path visualization

---

**Made with ❤️ for helping people find their perfect career path!** 
