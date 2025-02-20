import numpy as np
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

#data and data preprocessing
iris = load_iris()
X = iris.data
y = iris.target

mask = (y==0) | ( y == 1)

X = X[mask]
y = y[mask]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

#model logic
def sigmoid(z):
    return 1.0/(1.0 + np.exp(-z))

def logistic_regression(X,y,max_iterations=1000,learning_rate = 0.01):
    X = np.hstack([np.ones((X.shape[0],1)),X])
    weights = np.zeros(X.shape[1])
    
    for _ in range(max_iterations):
        z = np.dot(X,weights)
        h = sigmoid(z)
        gradient = np.dot(X.T,(h-y))/y.shape[0]
        weights -= gradient*learning_rate

    return weights


def predict(data,weights,scalar):
    data_std = scalar.transform(data)
    data_std = np.hstack([np.ones((data_std.shape[0],1)),data_std])
    z = np.dot(data_std,weights)
    h = sigmoid(z)
    pred = h > 0.5
    return "Setosa" if pred[0] == 0 else "Versicolor"


sc = StandardScaler()
X_train_std = sc.fit_transform(X_train)
X_test_std = sc.transform(X_test)

weights = logistic_regression(X_train,y_train,1000,0.01)

y_pred = sigmoid(np.dot(np.hstack([np.ones((X_test.shape[0],1)),X_test]),weights)) > 0.5

accuracy = accuracy_score(y_pred,y_test)

print("The accuracy of the model is : ",accuracy)

sepal_len = float(input("Enter the sepal length : "))
sepal_width = float(input("Enter the speal width : "))
petal_len = float(input("Enter the petal length : "))
petal_width = float(input("Enter the petal width : "))

X_input = np.array([sepal_len,sepal_width,petal_len,petal_width])
X_input = X_input.reshape(1,-1)

pred = predict(X_input,weights,sc)
print(pred)