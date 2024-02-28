import numpy as np

# Metrics 

# Mean absolute error
def mae(act,pred):
    diff=act-pred
    n=diff.shape[0]
    val=np.abs(diff)/n
    return val.sum()

# Mean squared error
def mse(act,pred):
    diff=act-pred
    square_diff=diff**2
    n=diff.shape[0]
    return square_diff.sum()/n

# Root mean squared error
def rmse(act, pred):
    return np.sqrt(mse(act,pred))

# R2 score 
def r2_score(act, pred):
    diff=act-pred
    diff=diff**2
    rss=diff.sum()
    diff2=act-np.mean(act)
    diff2=diff2**2
    tss=diff2.sum()
    score=1-(rss)/(tss)
    return score

# Adjusted R2 score
def adjusted_r2_score(act, pred, X):
    r2=r2_score(act, pred)
    n=act.shape[0]
    p=X.shape[1]
    score=1-(1-r2)*(n-1)/(n-p-1)
    return score

# mean_absolute_percentage_error
def mape(act, pred): 
    n=act.shape[0]
    diff_frac=np.abs(act-pred)/act
    sum=diff_frac.sum()
    return sum/n

# median_absolute_error
def med_ae(act, pred):   
    abs_val=np.abs(act-pred)
    return np.median(abs_val)