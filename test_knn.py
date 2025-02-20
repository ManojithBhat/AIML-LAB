from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris
import numpy as np
from sklearn.model_selection import train_test_split

iris = load_iris()
X = iris.data
y = iris.target

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25, random_state=42)

def euclidean_distance(point1,point2):
    return np.sqrt(np.sum((point1 - point2)**2))

def KNN(train_data,train_label,test_point,k=3):
    distances = []

    for i in range(len(train_data)):
        distance = euclidean_distance(train_data[i],test_point)
        distances.append((distance,train_label[i]))

    distances = sorted(distances,key = lambda x:x[0])
    nearest_neighbors = distances[:k]

    class_labels = {}
    for neighbor in nearest_neighbors:
        label = neighbor[1]
        class_labels[label] = class_labels.get(label,0) + 1
    predicted_class = max(class_labels,key= class_labels.get)
    return predicted_class


knn_pred = [KNN(X_train,y_train,X_test[i],3) for i in range(len(X_test))]

accuracy = accuracy_score(y_test,knn_pred)
print("Accuracy of the model is : ",accuracy)

#get the user input
petal_len = float(input("Enter petal length : "))
sepal_len = float(input("Enter sepal length : "))
petal_wid = float(input("Enter petal width : "))
sepal_wid = float(input("Enter sepal width : "))

input_np = np.array([sepal_len,sepal_wid,petal_len,petal_wid])
input_np = input_np.reshape(1,-1)

pred = KNN(X_train,y_train,input_np[0],3)

iris = {
    0:"Setosa",
    1:"Versicolor",
    2:"Virginica"
}


print(iris.get(pred,"unknown"))