
import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib

print("Downloading Data... (this might take a minute)")
mnist = fetch_openml('mnist_784', version=1, as_frame=False, parser='auto')
X, y = mnist['data'], mnist['target']

# --- FIX 1: Normalize Data (0 to 1) ---
X = X / 255.0 
# --------------------------------------

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training Model...")
# Increased max_iter for better convergence
clf = LogisticRegression(solver='lbfgs', max_iter=2000, tol=1e-4) 
clf.fit(X_train, y_train)

print("Model Accuracy:", clf.score(X_test, y_test))

print("Saving model to 'digit_model.pkl'...")
joblib.dump(clf, 'digit_model.pkl')
print("Done! Run this, then run the app.")