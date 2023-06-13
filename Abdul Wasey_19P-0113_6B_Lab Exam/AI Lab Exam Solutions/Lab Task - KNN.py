import pandas as pd
import numpy as np
from collections import Counter
from sklearn.metrics import accuracy_score,confusion_matrix

df = pd.read_csv("fruit_data_with_colors.txt",delimiter = "\t")
df.head()

X = df[["mass","width","height"]]

Y = df["fruit_label"]

trainX = np.array(X[:50])
trainY = np.array(Y[:50])
testX = np.array(X[50:])
testY = np.array(Y[50:])

class KNN:
    def __init__(self,k = 1):
        self.k = k
        
    def euclidian_distance(self,query,X):
        difference = np.array(X) - np.array(query)
        sqrd_diff = np.square(difference)
        sum_sqrd_diff = np.sum(sqrd_diff, axis = 1)
        distance = np.sqrt(sum_sqrd_diff)
        return distance
    
    def nearest_neighbours(self,distance):
        return np.argsort(distance)[:self.k]
    
    def predict(self,query,trainX,trainY):
        ed = self.euclidian_distance(query,trainX)
        nn = self.nearest_neighbours(ed)
        labels_nn = list(trainY[nn])
        return max(labels_nn, key = labels_nn.count) 
    
classifier = KNN(3)

predictions = [classifier.predict(x,trainX,trainY) for x in testX]
preds = np.array(predictions)

print("Predicted Outcomes: ", end = "")
print(preds, end = "\n\n")

print("Actual Outcomes: ", end = "")
print(testY, end = "\n\n")

print("Accuracy Score: ", end = "")
print(accuracy_score(testY,predictions), end = "\n\n")

print("Confusion Matrix: ")
print(confusion_matrix(testY,predictions), end = "\n\n")
