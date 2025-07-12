# AI Career Recommendation System 🚀

A modern, intelligent career recommendation system that helps users discover suitable career paths based on their skills, interests, and education level.

## 🌟 Features

- **Intelligent Career Matching**: Rule-based recommendation system
- **Multi-Industry Support**: Technology, Healthcare, Business, Education, Creative Arts, Engineering
- **Education Level Compatibility**: Tailored recommendations for all education levels
- **Detailed Career Information**: Salary ranges, required skills, growth potential
- **Alternative Career Suggestions**: Multiple career options
- **Confidence Scoring**: Shows recommendation confidence
- **Responsive Design**: Works on all devices

## 🏗️ Project Structure

```
rml/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── vercel.json           # Vercel deployment config
├── runtime.txt           # Python version
├── static/               # CSS, JS, and assets
├── templates/            # HTML templates
└── README.md            # This file
```

## 🚀 Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/belloibrahv/rml.git
   cd rml
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the application**
   - Open your browser
   - Go to: `http://localhost:5002`

### Vercel Deployment

1. **Connect to Vercel**
   - Go to [vercel.com](https://vercel.com)
   - Sign up/Login with GitHub
   - Click "New Project"
   - Import repository: `belloibrahv/rml`

2. **Configure settings**
   - Framework: `Other`
   - Build Command: (leave empty)
   - Output Directory: (leave empty)
   - Install Command: `pip install -r requirements.txt`

3. **Add environment variables**
   ```
   FLASK_ENV=production
   FLASK_DEBUG=0
   ```

4. **Deploy**
   - Click "Deploy"
   - Your app will be live at: `https://your-project-name.vercel.app`

## 📋 API Endpoints

- `GET /` - Landing page
- `GET /recommend` - Recommendation form
- `GET /about` - About page
- `POST /api/recommend` - Get career recommendations
- `GET /api/careers` - List all careers
- `GET /api/education-levels` - List education levels
- `GET /api/skills` - List available skills
- `GET /api/interests` - List available interests

## 🎯 Supported Careers

### Technology
- Software Engineer
- Data Scientist
- Web Developer
- Cybersecurity Analyst

### Healthcare
- Medical Doctor
- Nurse
- Pharmacist

### Business
- Business Analyst
- Marketing Manager
- Financial Analyst

### Education
- Teacher
- School Administrator

### Creative Arts
- Graphic Designer
- Content Writer
- Digital Marketing Specialist

### Engineering
- Civil Engineer
- Mechanical Engineer
- Electrical Engineer

## 🛠️ Technologies Used

- **Backend**: Flask, Python
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: Vercel
- **Database**: In-memory (no external dependencies)

## 📊 Features in Detail

### Career Database
- 18 detailed career profiles
- Salary information in Nigerian Naira (₦)
- Education requirements
- Required skills
- Growth potential indicators

### Recommendation Algorithm
- Skill matching analysis
- Interest alignment
- Education compatibility
- Industry preference consideration
- Fallback logic for edge cases

### User Interface
- Responsive design
- Modern, clean interface
- Interactive form elements
- Clear result presentation

## 🔧 Development

### Running in Development Mode
```bash
python app.py
```

The application runs in debug mode by default, which enables:
- Auto-reload on code changes
- Detailed error messages
- Development server features

### Project Structure
```
app.py              # Main Flask application
requirements.txt    # Python dependencies
vercel.json         # Vercel configuration
runtime.txt         # Python version specification
static/             # Static files (CSS, JS)
templates/          # HTML templates
```

## 🚀 Deployment

### Vercel (Recommended)
- Automatic HTTPS
- Global CDN
- Serverless functions
- Easy GitHub integration

### Other Platforms
- Heroku
- Railway
- Render
- DigitalOcean

## 📝 License

This project is licensed under the MIT License.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📞 Support

If you encounter any issues:
1. Check the troubleshooting section
2. Review the documentation
3. Create an issue on GitHub

---

**Made with ❤️ for helping people find their perfect career path!** 
