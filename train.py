import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib  # This is the tool that saves your model

print("Downloading Data... (this might take a minute)")
mnist = fetch_openml('mnist_784', version=1, as_frame=False, parser='auto')
X, y = mnist['data'], mnist['target']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training Model...")
# We use a simple model so it's small and fast
clf = LogisticRegression(solver='lbfgs', max_iter=1000, tol=0.1)
clf.fit(X_train, y_train)

print("Model Accuracy:", clf.score(X_test, y_test))

# SAVE THE MODEL
print("Saving model to 'digit_model.pkl'...")
joblib.dump(clf, 'digit_model.pkl')
print("Done! You can now run the app.")