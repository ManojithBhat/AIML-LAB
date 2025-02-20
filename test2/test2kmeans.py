from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import numpy as np

iris = load_iris()
X = iris.data[:,:2] #slice 0 to 2 columns

def kmeans(X,max_iterations, k=3):
    random_points = np.random.choice(X.shape[0],k,replace=False)
    centroids = X[random_points]

    for _ in range(max_iterations):
        distances = np.linalg.norm(X[:,None] - centroids,axis=2)
        points = np.argmin(distances,axis=1)
        centroids = np.array([X[points==i].mean(axis=0) for i in range(k)]) #remember this here, it is range(k) and points==i

    return centroids,points

k=3
centroids,labels = kmeans(X,2000,3)

colors = ['r','g','b']

for i in range(k): #iterate over k 
    plt.scatter(X[i==labels,0],X[labels == i,1],c = colors[i],label=f"cluster {i+1}")

plt.scatter(centroids[:,0],centroids[:,1],marker='x',c='black',label=f"Centroids")

plt.title("KNN scatter plot")
plt.xlabel("sepal length")
plt.ylabel("sepal width")
plt.legend()
plt.show()



