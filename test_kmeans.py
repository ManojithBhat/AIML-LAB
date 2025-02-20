import numpy as np
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

iris = load_iris()

X = iris.data[:,:2]

def Kmeans(X,max_iterations=1000,k=2):
    central_points = np.random.choice(X.shape[0],k,replace=False)
    centroids = X[central_points]

    for _ in range(max_iterations):
        distances = np.linalg.norm(X[:,None]-centroids,axis=2)
        labels = np.argmin(distances,axis=1)
        centroids = np.array([X[labels == i].mean(axis=0) for i in range(k)])

    return centroids,labels

k = 2

centroids, labels = Kmeans(X,1000,k)

colors = ['r','g','b']

for i in range(k):
    plt.scatter(X[labels==i,0],X[labels==i,1], c = colors[i],label=f'class {i+1}')

plt.scatter(centroids[:,0],centroids[:,1],c='black',marker='x',label=f'centroid {i+1}')

plt.title("Kmeans clustering of the iris dataset")
plt.xlabel("sepal length")
plt.ylabel("sepal width")
plt.legend()
plt.show()

