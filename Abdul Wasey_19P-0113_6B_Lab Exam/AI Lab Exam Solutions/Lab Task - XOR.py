import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import log_loss

ERROR = 5

def sigmoid(z):
        return 1/(1 + np.exp(-z))


X = np.array([[0,0],[0,1],[1,0],[1,1]])
Y = np.array([0,1,1,0])

X=X.T

W = np.random.rand(2,1)
b = np.random.rand()
print(W)
print(X)
numOfTrainSamples = X.shape[1]
numOfFeatures = X.shape[0]
Z = np.zeros(numOfTrainSamples)

J = 7
count = 0
for x in range(10):
# while(J-ERROR > 1):
    count+=1
    Z = np.dot(W.T,X,) + b

    A = sigmoid(Z)
    A = np.where(A < 0.5, 0, 1)
    A = A.squeeze()

    J = log_loss(Y,A)

    dz = A - Y
    dz=np.expand_dims(dz,axis = 0)
    dw = np.dot(X,dz.T)/X.shape[0]

    db = np.sum(dz,axis =1)/X.shape[0]

    alpha = 0.01
    W = W - alpha * dw
    b = b - alpha *db

    print(count,":",J)
    
    # print(J)
    