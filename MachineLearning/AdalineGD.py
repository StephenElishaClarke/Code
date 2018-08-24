import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


class AdalineGD(object):
   
   """ 
   ADAptive LINear NEuron Classifier

   Parameters
   ----------
   eta: float
   n_ter: int

   Attributes
   ----------
   w_: 1D array
   errors_: list
   
   """

   def __init__(self, eta=0.01, n_iter=50):
       self.eta = eta
       self.n_iter = n_iter

   def fit(self, X, y):
       
       """
       
       Parameters
       ----------
       X : {array-like}, shape = [n_samples, n_features]
       Training vectors,

       y : array-like, shape = [n_samples]
       Target values.

       Returns
       -------
       self : object
       
       """

       self.w_ = np.zeros(1+X.shape[1])
       self.cost_ = []

       for i in range(self.n_iter):
           output = self.net_input(X)
           errors = y-output
           self.w_[1:] += self.eta * X.T.dot(errors)
           self.w_[0] += self.eta * errors.sum()
           cost = (errors**2).sum() / 2.0
           self.cost_.append(cost)
       return self

   def net_input(self, X):
       return np.dot(X, self.w_[1:]+self.w_[0])

   def activation(self, X):
       return self.net_input(X)


   def predict(self, X):
       return np.where(self.activation(X) >= 0.0, 1, -1)

#####################################################
### Run Perceptron on Iris Data  ####################
#####################################################


df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',header=None)

y = df.iloc[0:100,4].values
y = np.where(y == 'Iris-setosa',-1, 1)  # Boolean 1 - when true returns -1 and not 'Iris-setosa'
X = df.iloc[0:100,[0, 2]].values

X_std = np.copy(X)
X_std[:,0] = (X[:,0] - X[:,0].mean()) / X[:,0].std()
X_std[:,1] = (X[:,1] - X[:,1].mean()) / X[:,1].std()

ada = AdalineGD(n_iter=15, eta=0.01)
ada.fit(X_std, y)

####################################################
### Plot Decision Surface ##########################
####################################################

def plot_decision_regions(X, y, classifier, resolution=0.02):

   # setup marker generator and color map
   markers = ('s', 'x', 'o', '^', 'v')
   colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
   cmap = ListedColormap(colors[:len(np.unique(y))])
   
   x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1 
   x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1 
   xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
   np.arange(x2_min, x2_max, resolution))

   Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
   Z = Z.reshape(xx1.shape)

   plt.contourf(xx1, xx2, Z, alpha=0.4, cmap=cmap)
   plt.xlim(xx1.min(), xx1.max())
   plt.ylim(xx2.min(), xx2.max())

   # plot class samples
   for idx, cl in enumerate(np.unique(y)):
      plt.scatter(x=X[y == cl, 0], y=X[y == cl, 1],alpha=0.8, c=cmap(idx),marker=markers[idx], label=cl)


plot_decision_regions(X_std, y, classifier=ada)
plt.title('Adaline - Gradient Descent')
plt.xlabel('sepal length [standardized]')
plt.ylabel('petal length [standardized]')
plt.legend(loc='upper left')
plt.show()
plt.plot(range(1, len(ada.cost_) + 1), ada.cost_, marker='o')
plt.xlabel('Epochs')
plt.ylabel('Sum-squared-error')
plt.show()
