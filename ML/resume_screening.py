import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
df = pd.read_csv('resume_dataset_200k_enhanced.csv')

# Explore
print("First 5 rows:")
print(df.head())
print("\nData info:")
print(df.info())
print("\nStatistical summary:")
print(df.describe())

# Clean (handle missing values, outliers)
df = df.dropna()

# Encode categorical variables
le_edu = LabelEncoder()
le_uni = LabelEncoder()
le_comp = LabelEncoder()

df['education_level'] = le_edu.fit_transform(df['education_level'])
df['university_tier'] = le_uni.fit_transform(df['university_tier'])
df['company_type'] = le_comp.fit_transform(df['company_type'])

# Prepare features and target
X = df.drop(['hired', 'candidate_id'], axis=1)  # Remove target and ID
y = df['hired']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale numerical features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train model
print("\nTraining Random Forest model...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Evaluate
predictions = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, predictions)

print(f"\nModel Accuracy: {accuracy:.4f}")
print("\nClassification Report:")
print(classification_report(y_test, predictions))

# Feature importance
feature_importance = pd.DataFrame({
    'feature': X.columns,
    'importance': model.feature_importances_
}).sort_values('importance', ascending=False)

print("\nTop 10 Most Important Features:")
print(feature_importance.head(10))