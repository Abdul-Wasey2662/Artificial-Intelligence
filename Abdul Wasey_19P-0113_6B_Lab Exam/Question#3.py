import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import log_loss
from sklearn.metrics import accuracy_score,confusion_matrix

columns = [i for i in range(1,61)]
df = pd.read_csv("Summary of Weather",delimiter = ",",names = columns,header = None)
df=df.drop("Precipitation" , axis=1)

print(df)

X_train, X_test, y_train, y_test = train_test_split(df[columns[:-1]], df[columns[-1]], test_size=0.35, random_state=42)

X_train = np.array(X_train)
X_test = np.array(X_test)
y_train = np.array(y_train)
y_test = np.array(y_test)

W = np.random.rand(60,1)

b = np.random.rand()

X_train = X_train.T

numOfTrainSamples = X_train.shape[1]
numOfFeatures = X_train.shape[0]
y_train = np.expand_dims(y_train,axis =0)

learning_rates = [0.1,0.01,0.001]
# alpha = 0.01

for alpha in learning_rates:
    print("Learning Rate: ", alpha)
    for i in range(5):
        print("Epoch",i+1,":", end = '')
        Z = np.dot(W.T,X_train,) + b

        def sigmoid(z):
            return 1/(1 + np.exp(-z))

        A = sigmoid(Z)

        A = np.where(A < 0.5, 0, 1)


        J = log_loss(y_train,A)
        # print(y_train, A)
        print(J)
        dz = A - y_train

        dw =  np.dot(X_train,dz.T)/numOfTrainSamples

        db = np.sum(dz,axis =1)/numOfTrainSamples
        
        W = W - alpha * dw
        b = b - alpha *db

        print("Accuracy Score: ", end = "")
        print(accuracy_score(y_train[0],A[0]))

        print("Confusion Matrix: ")
        print(confusion_matrix(y_train[0],A[0]), end = "\n\n")