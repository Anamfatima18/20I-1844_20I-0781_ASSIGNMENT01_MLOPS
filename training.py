import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler
from joblib import dump

# Step 1: Load the dataset
url = (
    "https://archive.ics.uci.edu/ml/machine-learning-databases/"
    "heart-disease/processed.cleveland.data"
)
columns = [
    'age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg',
    'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target'
]
data = pd.read_csv(url, names=columns, na_values="?")

# Step 2: Preprocess the dataset
# Drop rows with missing values for simplicity
data = data.dropna()

# Feature and Target Variables
X = data.drop('target', axis=1)
y = data['target'].apply(lambda x: 1 if x > 0 else 0)  # Binary classification

# Step 3: Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Step 4: Model training
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# Step 5: Evaluation
predictions = model.predict(X_test_scaled)
print("Accuracy:", accuracy_score(y_test, predictions))
print("Classification Report:\n", classification_report(y_test, predictions))

# Save the trained model and scaler
dump(model, 'model.joblib')
dump(scaler, 'scaler.joblib')
