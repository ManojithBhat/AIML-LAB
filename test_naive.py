from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

class NaiveBayes():
    def _fit(self, X, y):
        self._classes = np.unique(y)
        self._mean = np.array([X[y == c].mean(axis=0) for c in self._classes])
        self._var = np.array([X[y == c].var(axis=0) + 1e-9 for c in self._classes])  # Add small value to variance
        self._priors = np.array([X[y == c].shape[0] / len(y) for c in self._classes])

    def predictions(self, X_test):
        return np.array([self.pred(x) for x in X_test])

    def pred(self, x):
        posteriors = [np.log(prior) + np.sum(np.log(self._pdf(idx, x))) for idx, prior in enumerate(self._priors)]
        return self._classes[np.argmax(posteriors)]

    def _pdf(self, idx, x):
        mean, var = self._mean[idx], self._var[idx]
        numerator = np.exp(-((x - mean) ** 2) / (2 * var))
        denominator = np.sqrt(2 * np.pi * var)
        return np.maximum(numerator / denominator, 1e-9)  # Avoid zero probabilities

nb = NaiveBayes()
nb._fit(X_train, y_train)

prediction = nb.predictions(X_test)
accuracy = accuracy_score(y_test, prediction)
print("The accuracy of the model is:", accuracy)

sepal_len = float(input("Enter sepal length: "))
sepal_width = float(input("Enter sepal width: "))
petal_len = float(input("Enter petal length: "))
petal_width = float(input("Enter petal width: "))

user_input = np.array([[sepal_len, sepal_width, petal_len, petal_width]])

pred = nb.predictions(user_input)
print("Predicted class:", pred)
