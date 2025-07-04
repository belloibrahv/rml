#!/usr/bin/env python3
"""
Simple script to test model loading and see what's actually in the model files
"""

import os
import pickle
import numpy as np

def test_models():
    MODEL_DIR = os.path.join(os.path.dirname(__file__), "app", "models")
    
    print("🔍 Testing model files...")
    print(f"Model directory: {MODEL_DIR}")
    
    model_files = [
        "career_recommendation_model.pkl",
        "career_label_encoder.pkl", 
        "skills_mlb.pkl",
        "interests_mlb.pkl"
    ]
    
    for model_file in model_files:
        file_path = os.path.join(MODEL_DIR, model_file)
        print(f"\n📁 Testing: {model_file}")
        
        if not os.path.exists(file_path):
            print(f"❌ File not found: {file_path}")
            continue
            
        try:
            with open(file_path, "rb") as f:
                model = pickle.load(f)
            
            print(f"✅ File loaded successfully")
            print(f"   Type: {type(model)}")
            print(f"   Shape (if array): {getattr(model, 'shape', 'N/A')}")
            
            # Check for specific attributes
            if hasattr(model, 'predict'):
                print(f"   ✅ Has 'predict' method")
            if hasattr(model, 'transform'):
                print(f"   ✅ Has 'transform' method")
            if hasattr(model, 'inverse_transform'):
                print(f"   ✅ Has 'inverse_transform' method")
            if hasattr(model, 'fit'):
                print(f"   ✅ Has 'fit' method")
                
        except Exception as e:
            print(f"❌ Error loading {model_file}: {e}")

if __name__ == "__main__":
    test_models() 