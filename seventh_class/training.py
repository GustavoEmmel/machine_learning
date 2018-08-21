import numpy as np
import pandas as pd
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import StratifiedKFold
from sklearn.metrics import confusion_matrix

def getAccuracy(testset, predictions):
    correct = 0
    for id_test, test in testset.iterrows():
        if test[-1] == predictions.ix[id_test][0]:
            correct += 1
    return (correct / float(len(testset))) * 100.0


rh = pd.read_csv('RH.csv', nrows=None, header=0, index_col=None)

trainset, testset, = train_test_split(rh, test_size=0.2)

n_folds = 5

print rh.head()

skf = StratifiedKFold(rh['left'], n_folds)

for i, (train_index, test_index) in enumerate(skf):
    x_train = rh.iloc[train_index]
    y_train = rh.iloc[train_index]['left']
    x_test = rh.iloc[test_index]
    y_test = rh.iloc[test_index]['left']

    x_train = x_train.drop(columns=['sales', 'salary', 'left'])
    x_test = x_test.drop(columns=['sales', 'salary', 'left'])
    print 'numero de instancias e distribuicao de classes no treino do fold %d:'% i, trainset.shape[0], Counter(x_train['left'])
    print 'numero de instancias e distribuicao de classes no teste do fold %d:'% i, testset.shape[0], Counter(x_test['left'])

    predictions = []
    k = 3

    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(trainset.iloc[:, :-1], x_train.iloc[:, :-1])
    predicted_knn = knn.predict(x_test.iloc[:, :-1])
    accuracy = getAccuracy(x_test, pd.DataFrame(predicted_knn, index=x_test.index.values))
    print accuracy