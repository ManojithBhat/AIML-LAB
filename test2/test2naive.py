from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
import numpy as np


class naiveBayes():

    def fit(self,X,y):
        self._classes = np.unique(y)
        self._mean = np.array([X[y==label].mean(axis=0) for label in self._classes])
        self._var = np.array([X[y == label].var(axis=0) for label in self._classes])
        self._priors = np.array([X[y==label].shape[0]/len(y) for label in self._classes]) #its len of y 

    def predictions(self,X):
        return [self._pred(x) for x in X]
    
    def _pred(self,x):
        posteriors = [np.log(priors) + np.sum(np.log(np.maximum(self._pdf(idx,x),1e-9))) for idx,priors in enumerate(self._priors)] #its prios in enumerate
        return np.argmax(posteriors) #its argmax

    def _pdf(self,idx,x):
        mean,var = self._mean[idx],self._var[idx]
        numerator = np.exp(-(x-mean)**2/(2*var)) #its power is 2
        denominator = np.sqrt(2*np.pi*var)
        return numerator/denominator
    
iris = load_iris()
X = iris.data
y = iris.target

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

nb = naiveBayes()
nb.fit(X_train,y_train)

pred = nb.predictions(X_test)

accuacy = accuracy_score(y_test,pred)

print("Accuracy is : ",accuacy)

sepal_len = float(input("Enter sepal length: "))
sepal_width = float(input("Enter sepal width: "))
petal_len = float(input("Enter petal length: "))
petal_width = float(input("Enter petal width: "))

user_input = np.array([[sepal_len, sepal_width, petal_len, petal_width]])

prediction = nb.predictions(user_input)
print("predictions :", prediction)


    
