from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import json
from datetime import datetime
import os

app = Flask(__name__, static_folder="../static", template_folder="../templates")
CORS(app)

# Comprehensive career database
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
        
        # Get primary recommendation using rule-based system
        primary_career = get_rule_based_career(skills, interests, education_level, preferred_industry)
        
        if not primary_career:
            return jsonify({"success": False, "message": "Unable to generate career recommendation. Please try with different skills or interests."})
        
        # Get alternative careers
        alternative_careers = get_alternative_careers(skills, interests, education_level, primary_career)
        
        # Calculate confidence score
        confidence = calculate_confidence(skills, interests, education_level, primary_career)
        
        # Get career details
        career_details = get_career_details(primary_career)
        
        if not career_details:
            return jsonify({"success": False, "message": "Career details not found. Please try again."})
        
        return jsonify({
            "success": True,
            "primary_career": primary_career,
            "alternative_careers": alternative_careers,
            "career_details": career_details,
            "confidence": confidence,
            "skills_analyzed": skills,
            "interests_analyzed": interests,
            "education_level": education_level,
            "recommendation_method": "rule_based"
        })
        
    except Exception as e:
        return jsonify({"success": False, "message": f"Error generating recommendation: {str(e)}"})

@app.route("/api/careers")
def get_careers():
    careers = []
    for industry, industry_careers in CAREER_DATABASE.items():
        for career, details in industry_careers.items():
            careers.append({"name": career, "industry": industry, "details": details})
    return jsonify({"careers": careers})

@app.route("/api/education-levels")
def get_education_levels():
    return jsonify({"education_levels": EDUCATION_LEVELS})

@app.route("/api/skills")
def get_skills():
    return jsonify({"skills": POPULAR_SKILLS})

@app.route("/api/interests")
def get_interests():
    return jsonify({"interests": POPULAR_INTERESTS})

def get_rule_based_career(skills, interests, education_level, preferred_industry):
    """Rule-based career recommendation"""
    
    # Ensure inputs are lists
    skills = skills if isinstance(skills, list) else []
    interests = interests if isinstance(interests, list) else []
    
    # Define skill and interest mappings
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
    
    # Default recommendations based on education level
    default_careers = {
        "Secondary School": ["Web Developer", "Content Writer", "Digital Marketing Specialist"],
        "Diploma/Certificate": ["Nurse", "Web Developer", "Graphic Designer"],
        "Bachelor's Degree": ["Software Engineer", "Business Analyst", "Teacher"],
        "Master's Degree": ["Data Scientist", "Marketing Manager", "School Administrator"],
        "PhD/Doctorate": ["Medical Doctor", "Data Scientist", "School Administrator"]
    }
    
    # Get default career for education level
    default_career = default_careers.get(education_level, "Business Analyst")
    
    # Verify the default career exists in database
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
    
    return "Business Analyst"

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
    
    return min(base_confidence, 0.95) * 100

def is_career_suitable_for_education(career, education_level):
    """Check if career is suitable for given education level"""
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

def normalize_education_level(education_level):
    """Normalize education level to match database format"""
    mapping = {
        "Secondary School": "Secondary School",
        "Diploma/Certificate": "Diploma",
        "Bachelor's Degree": "Bachelor's",
        "Master's Degree": "Master's",
        "PhD/Doctorate": "PhD"
    }
    return mapping.get(education_level, "Bachelor's")

# Export the Flask app for Vercel
handler = app 