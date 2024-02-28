import numpy as np

class DataStandardizer:
    def __init__(self):
        self.mean=None
        self.std=None
        
    def fit_transform(self,X):
        n=X.shape[1]
        X_mean=np.zeros(n)
        X_std=np.zeros(n)
        for i in range(n):
            mean=np.mean(X.iloc[:,i])
            std=np.std(X.iloc[:,i])
            X_mean[i]=mean
            X_std[i]=std
        self.mean=X_mean
        self.std=X_std
        X_standardized=(X-X_mean)/X_std   
        return X_standardized
    
    def transform(self,X):
        X_standardized=(X-self.mean)/self.std 
        return X_standardized