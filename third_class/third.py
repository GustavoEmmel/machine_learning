import numpy as np
from sklearn import preprocessing

"""
Transformacao de dados
"""



X = np.array(
    [
        [1, -1, 2],
        [0, 0, 1],
        [-1, 0, 2]
    ]
)

print X
binarizer = preprocessing.Binarizer(threshold=0.0).fit(X)
binarizer.transform(X)
print X