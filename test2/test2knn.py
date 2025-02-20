from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

iris = load_iris()
X = iris.data
y = iris.target
label = iris.target_names

X_train,X_test, y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

def euclidean_distance(point1,point2):
    return np.sqrt(np.sum((point1-point2)**2))

def knn(X_data,y_label,data_point,k=3):
    distances = []

    for i in range(len(X_data)):
        distance = euclidean_distance(data_point,X_data[i])
        distances.append((distance,y_label[i])) #it is (())
    
    distances = sorted(distances,key=lambda x:x[0])
    nearest_neigbors = distances[:k] #have an eye on this 

    classes = {}
    for neighbors in nearest_neigbors:
        label = neighbors[1]
        classes[label] = classes.get(label,0) + 1
    
    return  max(classes,key=classes.get)

pred = [knn(X_train,y_train,X_test[i],3) for i in range(len(X_test))] #pass correctly the train and test 
accuracy  = accuracy_score(pred,y_test)

print("The accuacy of the model is : ",accuracy)

#take the input from the user 

petal_len = float(input("Enter petal length : "))
sepal_len = float(input("Enter sepal length : "))
petal_wid = float(input("Enter petal width : "))
sepal_wid = float(input("Enter sepal width : "))

X_data = [[sepal_len,sepal_wid,petal_len,petal_wid]]

prediction = knn(X_train,y_train,X_data,3)

print("prediction is ",label[prediction])

