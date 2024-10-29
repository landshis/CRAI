import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from utils.data_loader import load_data
from utils.feature_extractor import extract_features

# Load and preprocess data
X, y = load_data()
X = extract_features(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluate and save model
preds = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, preds)}")
joblib.dump(model, 'model/model.pkl')
