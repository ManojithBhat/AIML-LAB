from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np

def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))

def logistic_regression(X, y, num_iterations=200, learning_rate=0.001):
    X = np.hstack([np.ones((X.shape[0], 1)), X])  # Add bias term
    weights = np.zeros(X.shape[1])  # Initialize weights
    for _ in range(num_iterations):
        z = np.dot(X, weights)  # z = X * weights
        h = sigmoid(z)  # Sigmoid of z
        gradient = np.dot(X.T, (h - y)) / y.shape[0]  # Gradient of loss
        weights -= learning_rate * gradient  # Update weights
    return weights

def predict(input_data, weights, scaler):
    input_data_std = scaler.transform(input_data) 
    input_data_std = np.hstack([np.ones((input_data_std.shape[0], 1)), input_data_std])  
    prediction = sigmoid(np.dot(input_data_std, weights)) > 0.5  
    return "Setosa" if prediction[0] == 0 else "Versicolor"

# Load Iris dataset
iris = load_iris()
X = iris.data  # All features
y = iris.target  # All labels

# Filter to only include Setosa (label 0) and Versicolor (label 1)
mask = (y == 0) | (y == 1)
X = X[mask]
y = y[mask]

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=9)

# Standardize features
sc = StandardScaler()
X_train_std = sc.fit_transform(X_train)
X_test_std = sc.transform(X_test)

# Perform logistic regression
weights = logistic_regression(X_train_std, y_train)

# Make predictions on test data
y_pred = sigmoid(np.dot(np.hstack([np.ones((X_test_std.shape[0], 1)), X_test_std]), weights)) > 0.5

# Calculate accuracy
accuracy = np.mean(y_pred == y_test)
print(f"Accuracy on test data: {accuracy:.4f}")

# User input for prediction
sepal_len = float(input("Enter sepal length: "))
sepal_width = float(input("Enter sepal width: "))
petal_len = float(input("Enter petal length: "))
petal_width = float(input("Enter petal width: "))

# Prepare user input
user_input = np.array([[sepal_len, sepal_width, petal_len, petal_width]])

# Use the predict function
result = predict(user_input, weights, sc)

print(f"Prediction: {result}")