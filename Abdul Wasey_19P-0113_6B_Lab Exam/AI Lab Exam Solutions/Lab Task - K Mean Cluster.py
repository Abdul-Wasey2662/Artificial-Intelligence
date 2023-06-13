import pandas as pd
import numpy as np
from collections import Counter

np.random.seed(16)

def euclidian_distance(query,X):
        difference = np.array(X) - np.array(query)
        sqrd_diff = np.square(difference)
        sum_sqrd_diff = np.sum(sqrd_diff, axis = 1)
        distance = np.sqrt(sum_sqrd_diff)
        return distance

df = pd.read_csv("fruit_data_with_colors.txt",delimiter = "\t")
X = np.array(df[["mass","width","height","color_score"]])

K = 4

centroidIndex = np.random.randint(0,58,(K,))
centroids = X[centroidIndex]

for i in range(10):
    print('iter:',i+1, end = '\n')
    clusters = [[],[],[],[]]

    for x in X:
        id = np.argmin(euclidian_distance(x,centroids))
        # print(x,id)
        clusters[id].append(x)

    c = np.array(clusters, dtype = object)

    for x in range(K):
        centroids[x] = np.mean(c[x], axis = 0)
        print(centroids[x])

    print()
    
