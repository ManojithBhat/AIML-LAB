import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data
y = iris.target
labels = iris.target_names

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

class Naive_Bayes:
    def fit(self,X,y):
        self._classes = np.unique(y)
        self._mean = np.array([ X[y==c].mean(axis = 0) for c in self._classes])
        self._var = np.array([ X[y==c].var(axis = 0) for c in self._classes])
        self._priors = np.array([ X[y==c].shape[0]/len(y) for c in self._classes])

    def predict(self,X):
        return np.array([self._pred(x) for x in X])
    
    def _pred(self,x):
        posteriors = [ np.log(priors) + np.sum(np.log(np.maximum(self._pdf(idx, x), 1e-9))) for idx,priors in enumerate(self._priors)]
        return self._classes[np.argmax(posteriors)]
    
    def _pdf(self,idx,x):
        mean,var = self._mean[idx],self._var[idx]
        numerator = np.exp(-(x-mean)**2/(2*var))
        denominator = np.sqrt(2*np.pi*var)
        return numerator/denominator

nb = Naive_Bayes()
nb.fit(X_train,y_train)

y_pred = nb.predict(X_test)
accuracy = np.mean(y_pred == y_test)
print(accuracy)

# User input for prediction
sepal_len = float(input("Enter sepal length: "))
sepal_width = float(input("Enter sepal width: "))
petal_len = float(input("Enter petal length: "))
petal_width = float(input("Enter petal width: "))

# Prepare user input
user_input = np.array([[sepal_len, sepal_width, petal_len, petal_width]])

pred = nb.predict(user_input)
print(pred)

