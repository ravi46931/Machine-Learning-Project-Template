import numpy as np
from src.constants import *

class LinearRegression:
    def __init__(self):
        self._weight=None
        self._bias=None
        self._cost=None
    
    @property
    def weight(self):
        return self._weight
    
    @property
    def bias(self):
        return self._bias
    
    @property
    def cost(self):
        return self._cost
    
    def calculate_cost(self,X,y,W,b):   
        m=X.shape[0]
        err_sum=0
        for i in range(m):
            err_sum = err_sum + (np.dot(W, X[i,:])+b -y[i])**2
        loss=(1/2*m)*err_sum    
        return loss

    def calculate_gradient(self,XQ,y,W,b):         
        m=XQ.shape[0]
        n=XQ.shape[1]
        grad_sum_b=0
        grad_sum_W=np.zeros(n)
        for i in range(m):
            grad_sum_b = grad_sum_b + np.dot(W, XQ[i,:]) +b - y[i]
            for j in range(n):
                grad_sum_W[j] = grad_sum_W[j] + (np.dot(W, XQ[i,:]) +b -y[i])*XQ[i,j]
        return grad_sum_W, grad_sum_b

    def gradient_descent(self,X,y, iterations, alpha):         
        n=X.shape[1]
        m=X.shape[0]
        W=np.random.random_sample(n)
        b=np.random.randint(100)
        cost=np.zeros(iterations)
        for i in range(iterations):
            temp_b=0
            temp_W=np.zeros(n)
            temp_b=b-(alpha/m)*self.calculate_gradient(X, y, W, b)[1]
            temp_W=W-(alpha/m)*self.calculate_gradient(X, y, W, b)[0]
            b=temp_b
            W=temp_W
            cost[i]=self.calculate_cost(X, y, W, b)
        self._weight=W
        self._bias=b
        self._cost=cost
        
    def fit(self, X,y, iterations=ITERATION, alpha=ALPHA):
        self.gradient_descent(X, y, iterations, alpha)
    
    def predict(self, X):
        predicted=np.dot(X,self._weight) + self._bias
        return predicted
    