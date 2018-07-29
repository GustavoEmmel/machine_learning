import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier

def getAccuracy(testset, predictions):
    correct = 0
    for id_test, test in testset.iterrows():
        if test[-1] == predictions.ix[id_test][0]:
            correct += 1
    return (correct / float(len(testset))) * 100.0


def main():
    # prepare data
    zoo = pd.read_csv('zoo.csv', nrows=None, header=0, index_col=0)
    trainset, testset, = train_test_split(zoo, test_size=0.2, train_size=0.3)

    # print trainset
    # print testset

    # k = 2

    for k in xrange(1, 6):

        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(trainset.iloc[:, 0:-1], trainset.iloc[:, -1])
        predicted_knn = knn.predict(testset.iloc[:, 0:-1])
        accuracy = getAccuracy(testset, pd.DataFrame(predicted_knn, index=testset.index.values))
        print "K value: ", k, " | Accuracy: ", accuracy

main()

