import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import log_loss, mean_squared_error
import matplotlib.pyplot as plt

def sigmoid(z):
        return 1/(1 + np.exp(-z))

columns = [i for i in range(1,11)]
columns.append("label")
df = pd.read_csv("diabetes.txt",delimiter = "\t",names = columns,header = None)
headings = df[:1]
df = df[1:]
print(df)
df = df.astype(float)

age = df[1]
prog = df['label']

    
# df.plot.bar()
# df.show()
# x.show()

plt.plot(df)
plt.show()

print(df.describe())

X_train, X_test, y_train, y_test = train_test_split(df[columns[:-1]], df[columns[-1]], test_size=0.33, random_state=42)

X_train = np.array(X_train)
X_test = np.array(X_test)
y_train = np.array(y_train)
y_test = np.array(y_test)

W = np.random.rand(10,1)
b = np.random.rand()

X_train = X_train.T

numOfTrainSamples = X_train.shape[1]
numOfFeatures = X_train.shape[0]
Z = np.zeros(numOfTrainSamples)

y_train = np.expand_dims(y_train,axis =0)

y_train = y_train.astype(int)
for i in range(3):
    Z = np.dot(W.T,X_train,) + b


    # def sigmoid(z):
    #     return 1/(1 + np.exp(-z))

    # A = sigmoid(Z)

    # A = np.where(A < 0.5, 0, 1)

    J = mean_squared_error(y_train,Z)
    # print(J)
    dz = Z - y_train

    dw = np.dot(X_train,dz.T)/numOfTrainSamples

    db = np.sum(dz,axis =1)/numOfTrainSamples
    alpha = 0.1
    W = W - alpha * dw
    b = b - alpha *db

print(J)