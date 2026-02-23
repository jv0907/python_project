import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
data = pd.read_csv("dataset.cv")

# Convert labels to numeric
data['label'] = data['label'].map({'ham': 0, 'spam': 1})

# Features and target
X = data['message']
y = data['label']

# Text Vectorization
vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized, y, test_size=0.2, random_state=42
)

# Model
model = MultinomialNB()
model.fit(X_train, y_train)

# Accuracy
y_pred = model.predict(X_test)
print("Model Accuracy:", accuracy_score(y_test, y_pred))

# Save model & vectorizer
joblib.dump(model, "spam_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Model and Vectorizer saved successfully!")