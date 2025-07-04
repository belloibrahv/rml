from flask import Flask, request, jsonify, render_template
import os
import pickle
import json
from datetime import datetime
import sqlite3

app = Flask(__name__, static_folder="static", template_folder="templates")

# Database setup
def init_db():
    conn = sqlite3.connect('career_reco.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS recommendations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            education_level TEXT,
            skills TEXT,
            interests TEXT,
            preferred_industry TEXT,
            recommended_career TEXT,
            confidence_score REAL,
            alternative_careers TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

# Load models - Temporarily disabled due to compatibility issues
MODEL_DIR = os.path.join(os.path.dirname(__file__), "models")
career_model = None
label_encoder = None
skills_mlb = None
interests_mlb = None

print("📝 Using rule-based career recommendations (ML models temporarily disabled)")
print("🔧 This ensures the system works reliably while we resolve model compatibility issues")

# Comprehensive career database with education levels and descriptions
CAREER_DATABASE = {
    "Technology": {
        "Software Engineer": {
            "education": ["Bachelor's", "Master's"],
            "description": "Design and develop software applications and systems",
            "skills": ["Programming", "Problem Solving", "Teamwork"],
            "salary_range": "₦60,000 - ₦150,000+",
            "growth": "High"
        },
        "Data Scientist": {
            "education": ["Bachelor's", "Master's", "PhD"],
            "description": "Analyze complex data to help organizations make decisions",
            "skills": ["Statistics", "Programming", "Machine Learning"],
            "salary_range": "₦70,000 - ₦160,000+",
            "growth": "Very High"
        },
        "Web Developer": {
            "education": ["Secondary School", "Diploma", "Bachelor's"],
            "description": "Create and maintain websites and web applications",
            "skills": ["HTML/CSS", "JavaScript", "Design"],
            "salary_range": "₦40,000 - ₦120,000",
            "growth": "High"
        },
        "Cybersecurity Analyst": {
            "education": ["Bachelor's", "Master's"],
            "description": "Protect computer systems from cyber threats",
            "skills": ["Security", "Networking", "Problem Solving"],
            "salary_range": "₦60,000 - ₦140,000",
            "growth": "Very High"
        }
    },
    "Healthcare": {
        "Medical Doctor": {
            "education": ["Bachelor's", "Medical School"],
            "description": "Diagnose and treat patients' illnesses and injuries",
            "skills": ["Communication", "Critical Thinking", "Empathy"],
            "salary_range": "₦80,000 - ₦300,000+",
            "growth": "High"
        },
        "Nurse": {
            "education": ["Diploma", "Bachelor's"],
            "description": "Provide patient care and support in healthcare settings",
            "skills": ["Patient Care", "Communication", "Teamwork"],
            "salary_range": "₦45,000 - ₦100,000",
            "growth": "High"
        },
        "Pharmacist": {
            "education": ["Bachelor's", "PharmD"],
            "description": "Dispense medications and provide pharmaceutical care",
            "skills": ["Chemistry", "Attention to Detail", "Communication"],
            "salary_range": "₦60,000 - ₦130,000",
            "growth": "Medium"
        }
    },
    "Business": {
        "Business Analyst": {
            "education": ["Bachelor's", "Master's"],
            "description": "Analyze business processes and recommend improvements",
            "skills": ["Analysis", "Communication", "Problem Solving"],
            "salary_range": "₦50,000 - ₦120,000",
            "growth": "High"
        },
        "Marketing Manager": {
            "education": ["Bachelor's", "Master's"],
            "description": "Develop and execute marketing strategies",
            "skills": ["Creativity", "Communication", "Analytics"],
            "salary_range": "₦55,000 - ₦140,000",
            "growth": "Medium"
        },
        "Financial Analyst": {
            "education": ["Bachelor's", "Master's"],
            "description": "Analyze financial data and provide investment guidance",
            "skills": ["Mathematics", "Analysis", "Attention to Detail"],
            "salary_range": "₦50,000 - ₦130,000",
            "growth": "High"
        }
    },
    "Education": {
        "Teacher": {
            "education": ["Bachelor's", "Master's"],
            "description": "Educate students in various subjects and grade levels",
            "skills": ["Communication", "Patience", "Organization"],
            "salary_range": "₦35,000 - ₦80,000",
            "growth": "Medium"
        },
        "School Administrator": {
            "education": ["Bachelor's", "Master's"],
            "description": "Manage school operations and educational programs",
            "skills": ["Leadership", "Organization", "Communication"],
            "salary_range": "₦60,000 - ₦120,000",
            "growth": "Medium"
        }
    },
    "Creative Arts": {
        "Graphic Designer": {
            "education": ["Secondary School", "Diploma", "Bachelor's"],
            "description": "Create visual content for various media",
            "skills": ["Creativity", "Design Software", "Communication"],
            "salary_range": "₦35,000 - ₦90,000",
            "growth": "Medium"
        },
        "Content Writer": {
            "education": ["Secondary School", "Bachelor's"],
            "description": "Create written content for websites, blogs, and marketing",
            "skills": ["Writing", "Research", "Creativity"],
            "salary_range": "₦30,000 - ₦80,000",
            "growth": "High"
        },
        "Digital Marketing Specialist": {
            "education": ["Secondary School", "Bachelor's"],
            "description": "Manage online marketing campaigns and social media",
            "skills": ["Marketing", "Social Media", "Analytics"],
            "salary_range": "₦40,000 - ₦100,000",
            "growth": "High"
        }
    },
    "Engineering": {
        "Civil Engineer": {
            "education": ["Bachelor's", "Master's"],
            "description": "Design and oversee construction of infrastructure projects",
            "skills": ["Mathematics", "Problem Solving", "Project Management"],
            "salary_range": "₦55,000 - ₦130,000",
            "growth": "Medium"
        },
        "Mechanical Engineer": {
            "education": ["Bachelor's", "Master's"],
            "description": "Design and build mechanical devices and systems",
            "skills": ["Physics", "Design", "Problem Solving"],
            "salary_range": "₦55,000 - ₦130,000",
            "growth": "Medium"
        },
        "Electrical Engineer": {
            "education": ["Bachelor's", "Master's"],
            "description": "Design electrical systems and electronic devices",
            "skills": ["Physics", "Mathematics", "Problem Solving"],
            "salary_range": "₦60,000 - ₦140,000",
            "growth": "Medium"
        }
    }
}

# Education levels
EDUCATION_LEVELS = [
    "Secondary School",
    "Diploma/Certificate", 
    "Bachelor's Degree",
    "Master's Degree",
    "PhD/Doctorate"
]

# Popular skills and interests
POPULAR_SKILLS = [
    "Programming", "Data Analysis", "Communication", "Leadership", "Problem Solving",
    "Creativity", "Teamwork", "Project Management", "Marketing", "Sales",
    "Mathematics", "Science", "Writing", "Design", "Research",
    "Customer Service", "Teaching", "Healthcare", "Finance", "Engineering"
]

POPULAR_INTERESTS = [
    "Technology", "Healthcare", "Business", "Education", "Creative Arts",
    "Science", "Engineering", "Finance", "Marketing", "Social Impact",
    "Environment", "Sports", "Travel", "Food", "Fashion",
    "Music", "Gaming", "Reading", "Fitness", "Photography"
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/recommend")
def recommend_page():
    return render_template("recommend.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/api/recommend", methods=["POST"])
def recommend():
    try:
        data = request.json
        name = data.get("name", "")
        email = data.get("email", "")
        education_level = data.get("education_level", "")
        skills = data.get("skills", [])
        interests = data.get("interests", [])
        preferred_industry = data.get("preferred_industry", "")
        
        # Validate inputs
        if not skills and not interests:
            return jsonify({"success": False, "message": "Please provide skills or interests"})
        
        if not education_level:
            return jsonify({"success": False, "message": "Please select your education level"})
        
        # Ensure skills and interests are lists
        skills = skills if isinstance(skills, list) else []
        interests = interests if isinstance(interests, list) else []
        
        # Get primary recommendation
        try:
            print(f"Getting recommendation for: skills={skills}, interests={interests}, education={education_level}, industry={preferred_industry}")
            primary_career = get_career_recommendation(skills, interests, education_level, preferred_industry)
            print(f"Primary career recommended: {primary_career}")
        except Exception as e:
            print(f"Error in career recommendation: {e}")
            return jsonify({"success": False, "message": "Unable to generate career recommendation. Please try with different skills or interests."})
        
        if not primary_career:
            return jsonify({"success": False, "message": "Unable to generate career recommendation. Please try with different skills or interests."})
        
        # Get alternative careers
        try:
            alternative_careers = get_alternative_careers(skills, interests, education_level, primary_career)
        except Exception as e:
            print(f"Error getting alternative careers: {e}")
            alternative_careers = []
        
        # Calculate confidence score
        try:
            confidence = calculate_confidence(skills, interests, education_level, primary_career)
        except Exception as e:
            print(f"Error calculating confidence: {e}")
            confidence = 0.7  # Default confidence
        
        # Save recommendation to database
        try:
            conn = sqlite3.connect('career_reco.db')
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO recommendations (name, email, education_level, skills, interests, 
                                           preferred_industry, recommended_career, confidence_score, alternative_careers)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (name, email, education_level, json.dumps(skills), json.dumps(interests), 
                  preferred_industry, primary_career, confidence, json.dumps(alternative_careers)))
            conn.commit()
            conn.close()
        except Exception as db_error:
            print(f"Database error: {db_error}")
            # Continue without saving to database
        
        # Get career details
        try:
            career_details = get_career_details(primary_career)
        except Exception as e:
            print(f"Error getting career details: {e}")
            return jsonify({"success": False, "message": "Career details not found. Please try again."})
        
        if not career_details:
            print(f"Career '{primary_career}' not found in database. Available careers: {list_all_careers()}")
            return jsonify({"success": False, "message": f"Career '{primary_career}' not found. Please try again with different skills or interests."})
        
        return jsonify({
            "success": True,
            "primary_career": primary_career,
            "career_details": career_details,
            "alternative_careers": alternative_careers,
            "confidence": round(confidence * 100, 2),
            "skills_analyzed": skills,
            "interests_analyzed": interests,
            "education_level": education_level
        })
        
    except Exception as e:
        print(f"Recommendation error: {e}")
        return jsonify({"success": False, "message": "An error occurred while processing your request. Please try again."})

@app.route("/api/careers")
def get_careers():
    return jsonify({"careers": CAREER_DATABASE})

@app.route("/api/education-levels")
def get_education_levels():
    return jsonify({"education_levels": EDUCATION_LEVELS})

@app.route("/api/skills")
def get_skills():
    return jsonify({"skills": POPULAR_SKILLS})

@app.route("/api/interests")
def get_interests():
    return jsonify({"interests": POPULAR_INTERESTS})

def get_career_recommendation(skills, interests, education_level, preferred_industry):
    """Get career recommendation based on input parameters"""
    
    # Currently using rule-based recommendation only
    # ML models are temporarily disabled for compatibility
    return get_rule_based_career(skills, interests, education_level, preferred_industry)

def get_rule_based_career(skills, interests, education_level, preferred_industry):
    """Rule-based career recommendation"""
    
    # Ensure inputs are lists
    skills = skills if isinstance(skills, list) else []
    interests = interests if isinstance(interests, list) else []
    
    # Define skill and interest mappings (only careers that exist in CAREER_DATABASE)
    skill_mappings = {
        "programming": ["Software Engineer", "Web Developer", "Data Scientist"],
        "data": ["Data Scientist", "Business Analyst", "Financial Analyst"],
        "design": ["Graphic Designer", "Web Developer"],
        "marketing": ["Marketing Manager", "Digital Marketing Specialist", "Content Writer"],
        "finance": ["Financial Analyst", "Business Analyst"],
        "healthcare": ["Medical Doctor", "Nurse", "Pharmacist"],
        "teaching": ["Teacher", "School Administrator"],
        "engineering": ["Civil Engineer", "Mechanical Engineer", "Electrical Engineer"]
    }
    
    interest_mappings = {
        "technology": ["Software Engineer", "Data Scientist", "Web Developer"],
        "healthcare": ["Medical Doctor", "Nurse", "Pharmacist"],
        "business": ["Business Analyst", "Marketing Manager", "Financial Analyst"],
        "education": ["Teacher", "School Administrator"],
        "creative": ["Graphic Designer", "Content Writer", "Digital Marketing Specialist"],
        "science": ["Data Scientist", "Medical Doctor"],
        "engineering": ["Civil Engineer", "Mechanical Engineer", "Electrical Engineer"]
    }
    
    # Check skills first
    for skill in skills:
        if isinstance(skill, str):
            skill_lower = skill.lower()
            for keyword, careers in skill_mappings.items():
                if keyword in skill_lower:
                    for career in careers:
                        if is_career_suitable_for_education(career, education_level):
                            return career
    
    # Check interests
    for interest in interests:
        if isinstance(interest, str):
            interest_lower = interest.lower()
            for keyword, careers in interest_mappings.items():
                if keyword in interest_lower:
                    for career in careers:
                        if is_career_suitable_for_education(career, education_level):
                            return career
    
    # Check preferred industry if specified
    if preferred_industry and preferred_industry in CAREER_DATABASE:
        for career, details in CAREER_DATABASE[preferred_industry].items():
            if is_career_suitable_for_education(career, education_level):
                return career
    
    # Default recommendations based on education level (only careers that exist in CAREER_DATABASE)
    default_careers = {
        "Secondary School": ["Web Developer", "Content Writer", "Digital Marketing Specialist"],
        "Diploma/Certificate": ["Nurse", "Web Developer", "Graphic Designer"],
        "Bachelor's Degree": ["Software Engineer", "Business Analyst", "Teacher"],
        "Master's Degree": ["Data Scientist", "Marketing Manager", "School Administrator"],
        "PhD/Doctorate": ["Medical Doctor", "Data Scientist", "School Administrator"]
    }
    
    # Get default career for education level
    default_career = default_careers.get(education_level, "Business Analyst")
    
    # Verify the default career exists in database, if not, find any suitable career
    if career_exists_in_database(default_career):
        return default_career
    
    # Fallback: find any career suitable for the education level
    for industry, careers in CAREER_DATABASE.items():
        for career, details in careers.items():
            if is_career_suitable_for_education(career, education_level):
                return career
    
    # Ultimate fallback: return first available career
    for industry, careers in CAREER_DATABASE.items():
        for career in careers.keys():
            return career
    
    return "Business Analyst"  # This should always exist

def get_alternative_careers(skills, interests, education_level, primary_career, count=3):
    """Get alternative career suggestions"""
    alternatives = []
    
    # Get careers from same industry as primary career
    primary_industry = None
    for industry, careers in CAREER_DATABASE.items():
        if primary_career in careers:
            primary_industry = industry
            break
    
    # First, try to get careers from the same industry
    if primary_industry:
        for career, details in CAREER_DATABASE[primary_industry].items():
            if career != primary_career and is_career_suitable_for_education(career, education_level):
                alternatives.append(career)
                if len(alternatives) >= count:
                    return alternatives
    
    # If we don't have enough alternatives, get from other industries
    for industry, careers in CAREER_DATABASE.items():
        if industry != primary_industry:
            for career, details in careers.items():
                if career != primary_career and is_career_suitable_for_education(career, education_level):
                    alternatives.append(career)
                    if len(alternatives) >= count:
                        return alternatives
    
    return alternatives[:count]

def calculate_confidence(skills, interests, education_level, career):
    """Calculate confidence score for recommendation"""
    base_confidence = 0.6
    
    # Ensure inputs are lists
    skills = skills if isinstance(skills, list) else []
    interests = interests if isinstance(interests, list) else []
    
    # Increase confidence based on education level match
    if is_career_suitable_for_education(career, education_level):
        base_confidence += 0.2
    
    # Increase confidence based on number of skills/interests
    if len(skills) > 0:
        base_confidence += 0.1
    if len(interests) > 0:
        base_confidence += 0.1
    
    # Additional confidence for having both skills and interests
    if len(skills) > 0 and len(interests) > 0:
        base_confidence += 0.05
    
    return min(base_confidence, 0.95)

def is_career_suitable_for_education(career, education_level):
    """Check if career is suitable for given education level"""
    # Normalize education level to match database format
    normalized_education = normalize_education_level(education_level)
    
    for industry, careers in CAREER_DATABASE.items():
        if career in careers:
            career_details = careers[career]
            return normalized_education in career_details["education"]
    return False

def career_exists_in_database(career):
    """Check if career exists in our database"""
    if not isinstance(career, str):
        return False
    
    for industry, careers in CAREER_DATABASE.items():
        if career in careers:
            return True
    return False

def get_career_details(career):
    """Get detailed information about a career"""
    for industry, careers in CAREER_DATABASE.items():
        if career in careers:
            return {
                "industry": industry,
                "details": careers[career]
            }
    return None

def list_all_careers():
    """List all careers available in the database"""
    all_careers = []
    for industry, careers in CAREER_DATABASE.items():
        all_careers.extend(list(careers.keys()))
    return all_careers

def normalize_education_level(education_level):
    """Convert frontend education level to database format"""
    mapping = {
        "Secondary School": "Secondary School",
        "Diploma/Certificate": "Diploma",
        "Bachelor's Degree": "Bachelor's",
        "Master's Degree": "Master's",
        "PhD/Doctorate": "PhD"
    }
    return mapping.get(education_level, education_level)

if __name__ == "__main__":
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5001)
