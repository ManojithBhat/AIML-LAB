from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

iris = load_iris()
X = iris.data
y = iris.target
label = iris.target_names

mask = (y==0)| (y==1)

X = X[mask] #its just the mask not mask == y
y = y[mask]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
#ensure its train,test,train,test

def sigmoid(z):
    return 1.0/(1.0 + np.exp(-z))

def logistic_regression(X,y,max_iterations=1000,learning_rate=0.01):
    X = np.hstack([np.ones((X.shape[0],1)),X])
    weights = np.zeros(X.shape[1])

    for _ in range(max_iterations):
        z = np.dot(X,weights)
        h = sigmoid(z)
        gradient = np.dot(X.T,(h-y))/y.shape[0] #its h-y
        weights -= gradient*learning_rate
    return weights

def predict(X_data,weights,scalar):
    X_data = scalar.transform(X_data)
    return sigmoid(np.dot(np.hstack([np.ones((X_data.shape[0],1)),X_data]),weights)) > 0.5

sc = StandardScaler()
X_train = sc.fit_transform(X_train) #its fit_transform
X_test = sc.transform(X_test)

weights = logistic_regression(X_train,y_train)

pred = sigmoid(np.dot(np.hstack([np.ones((X_train.shape[0],1)),X_train]),weights)) > 0.5

accuracy = accuracy_score(pred,y_train)

print("The accuracy is : ",accuracy)

petal_len = float(input("Enter petal length : "))
sepal_len = float(input("Enter sepal length : "))
petal_wid = float(input("Enter petal width : "))
sepal_wid = float(input("Enter sepal width : "))

X_data = [[sepal_len,sepal_wid,petal_len,petal_wid]]

prediciton_data = predict(X_data,weights,sc)

print("The predciton is : ", label[prediciton_data[0]])
