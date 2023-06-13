import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import accuracy_score as asc
from sklearn.metrics import confusion_matrix as cm
import matplotlib.pyplot as plt

columns = []
columns.append("LABEL")

for i in range(1,14):
    columns.append(i)

c2 = ["LABEL"]
df = pd.read_csv("wine.data",delimiter = "," , names = columns , header = None)



TRAIN_X, TEST_X, TRAIN_Y, TEST_Y = tts(df[columns[1:]], df[columns[0]], test_size=0.30, random_state=42) #because the data is split into 70/30 that's why
X = np.array(TRAIN_X[[1,2,3,4,5,6,7,8,9,10,11,12,13]])

np.random.seed(16)

def eu_distance(query,X):
        difference = np.array(X) - np.array(query)
        squared_diff = np.square(difference)
        sum_squared_diff = np.sum(squared_diff, axis = 1)
        distance = np.sqrt(sum_squared_diff)
        return distance

K = 3

centroid_In = np.random.randint(0,125,(K,))
centroids = X[centroid_In]



for i in range(100):
    Clusters = [[],[],[],[]]

    for x in X:
        id = np.argmin(eu_distance(x,centroids))
        Clusters[id].append(x)

    c = np.array(Clusters, dtype = object)

    for x in range(K):
        centroids[x] = np.mean(c[x], axis = 0)
        

print("Model Trained")

predict = []

for x in TEST_X.T:
    temp = eu_distance(x,centroids)
    temp = np.argmin(temp)
    predict.append(temp+1)

predict = [np.argmin(eu_distance(x,centroids)) for x in TEST_X.T]
print(predict, np.array(TEST_Y))

print("Predicted Outcomes: ", end = "")
print(np.array(predict) , end = "\n\n")

print("Actual Outcomes: ", end = "")
print(np.array(TEST_Y) , end = "\n\n")

acc = asc(np.array(predict) , np.array(TEST_Y))
print("Accuracy = " , acc)

cfm = cm(np.array(predict) , np.array(TEST_Y))
print("Confusion Matrix = " , cfm)