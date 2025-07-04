import pandas as pd
import numpy as np
from sklearn.preprocessing import MultiLabelBinarizer, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import cross_val_score
import joblib

# Load the data
df = pd.read_csv('data.csv')

# Split multi-label columns into lists
df['Skills'] = df['Skills'].apply(lambda x: x.split(';'))
df['Interests'] = df['Interests'].apply(lambda x: x.split(';'))

# One-hot encode Skills and Interests
mlb_skills = MultiLabelBinarizer()
skills_encoded = mlb_skills.fit_transform(df['Skills'])
skills_df = pd.DataFrame(skills_encoded, columns=mlb_skills.classes_)

mlb_interests = MultiLabelBinarizer()
interests_encoded = mlb_interests.fit_transform(df['Interests'])
interests_df = pd.DataFrame(interests_encoded, columns=mlb_interests.classes_)

# One-hot encode Education
education_encoded = pd.get_dummies(df['Education'], prefix='Education')

# Combine all features
X = pd.concat([df[['Age']], education_encoded, skills_df, interests_df], axis=1)

# Encode target
le = LabelEncoder()
y = le.fit_transform(df['Recommended_Career'])

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model with cross-validation
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    min_samples_split=5,
    random_state=42
)

# Perform cross-validation
scores = cross_val_score(model, X_train, y_train, cv=5, scoring='accuracy')
print(f"Cross-validation scores: {scores}")
print(f"Mean cross-validation score: {scores.mean():.4f}")

# Train final model
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(
    y_test, y_pred,
    labels=np.arange(len(le.classes_)),
    target_names=le.classes_
))

# Calculate feature importance
feature_importance = model.feature_importances_
feature_names = X.columns

# Save model and encoders
joblib.dump(model, 'career_recommendation_model.pkl')
joblib.dump(le, 'career_label_encoder.pkl')
joblib.dump(mlb_skills, 'skills_mlb.pkl')
joblib.dump(mlb_interests, 'interests_mlb.pkl')
print("Model and encoders saved!")
