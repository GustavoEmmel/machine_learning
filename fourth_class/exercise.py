import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, calinski_harabaz_score


df = pd.read_csv('adult.csv')

# getting hours-per-week
df = df.iloc[:,12:13]
# print df.head()

# cl = KMeans(n_clusters=3, init='k-means++', n_init=10, max_iter=300)
# cl = cl.fit(df)
#
# labels = cl.labels_
# centroids = cl.cluster_centers_
# print centroids
# print labels
# print silhouette_score(df, labels, 'euclidean', 200)

for k in xrange(2, 21):
    cl = KMeans(n_clusters=k, init='k-means++', n_init=10, max_iter=300)
    cl = cl.fit(df)
    labels = cl.labels_
    score_km = silhouette_score(df, labels, 'euclidean', 200)
    score_ca = calinski_harabaz_score(df, labels)
    print k, score_km, score_ca

print "resultados de clustering sobre horas semanais"
print "pelo silhoute score com 14 clusters teremos o melhor resultado"
print "pelo calinsk score quanto mais clusters o melhor resultado"
print "fim 1"





df = pd.read_csv('adult.csv')

df = df.iloc[:,5:6]

df.columns = ['maritage status']
print df.head(10)

statuses = pd.unique(df.values.ravel('K'))
# print statuses

## one hot enconder

foo = np.zeros((len(df), 7))
for index, row in df.iterrows():

    if row['maritage status'] == ' Married-civ-spouse':
        foo[index][0] = 1
    if row['maritage status'] == ' Divorced':
        foo[index][1] = 1
    if row['maritage status'] == ' Married-spouse-absent':
        foo[index][2] = 1
    if row['maritage status'] == ' Never-married':
        foo[index][3] = 1
    if row['maritage status'] == ' Separated':
        foo[index][4] = 1
    if row['maritage status'] == ' Married-AF-spouse':
        foo[index][5] = 1
    if row['maritage status'] == ' Widowed':
        foo[index][6] = 1


# print foo
#
# cl = KMeans(n_clusters=3, init='k-means++', n_init=10, max_iter=300)
# cl = cl.fit(foo)
#
# labels = cl.labels_
# centroids = cl.cluster_centers_
# print centroids
# print labels
# print silhouette_score(foo, labels, 'euclidean', 200)

for k in xrange(2, 21):
    cl = KMeans(n_clusters=k, init='k-means++', n_init=10, max_iter=300)
    cl = cl.fit(foo)
    labels = cl.labels_
    score_km = silhouette_score(foo, labels, 'euclidean', 200)
    score_ca = calinski_harabaz_score(foo, labels)
    print k, score_km, score_ca

print "numa matriz de estados civeis (7 diferentes status)"
print "encontramos para ambos score o 100% de eficacia em cluster em 7"
print "fim 2"