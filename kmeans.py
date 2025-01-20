import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data[:,:2]

def kmeans(X,max_iteration,k):
    random_points = np.random.choice(X.shape[0],k,replace=False)
    centroids = X[random_points]

    for _ in range(max_iteration):
        distances = np.linalg.norm(X[:,None]-centroids,axis = 2)
        labels = np.argmin(distances,axis=1)
        centroids = np.array([X[labels == i].mean(axis=0) for i in range(k)])

    return centroids,labels

k = 3

centroids,labels = kmeans(X,1000,3)

#plotting the graph
colors = ['r','g','b']
for i in range(k):
    #plot for every centroid
    plt.scatter(X[labels==i,0],X[labels==i,1],c=colors[i],label=f"cluster{i+1}")

plt.scatter(centroids[:,0],centroids[:,1],marker='x',color='black',label="centroid")

plt.title("Kmeans clustering for the iris dataset")
plt.xlabel("sepal length")
plt.ylabel("sepal width")
plt.legend()
plt.show()

