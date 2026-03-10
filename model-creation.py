"""House Price Prediction Model Training Script

Trains a simple linear regression model on sample (area -> price) data and
serializes the trained model to model.pkl for use by the FastAPI app.
"""

import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

# Sample training data: house areas (sq ft) and corresponding prices (USD)
X = np.array([[500], [1200], [2500], [2800], [3000]])
y = np.array([100000, 225000, 350000, 400000, 520000])

# Train the linear regression model
model = LinearRegression()
model.fit(X, y)

# Save the trained model to disk
joblib.dump(model, "model.pkl")
print("Model trained and saved.")
