from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import fcluster
import pandas as pd
from sklearn.metrics import silhouette_score, calinski_harabaz_score

data = load_iris()
df = pd.DataFrame(
    data['data'],
    columns=data['feature_names']
)

cl = KMeans(n_clusters=3, init='k-means++', n_init=10, max_iter=300)
cl = cl.fit(df)


labels = cl.labels_
centroids = cl.cluster_centers_
# print centroids
# print labels
#
# for k in xrange(2, 10):
#     cl = KMeans(n_clusters=k, init='k-means++', n_init=10, max_iter=300)
#     cl = cl.fit(df)

z = linkage(df, 'single')
# print z

dendrogram(z)
plt.show()

k = 3
clusters = fcluster(z, k, criterion='maxclust')
# print clusters


score_km = silhouette_score(df, labels)
score_hi = silhouette_score(df, clusters)
print(score_km)
print(score_hi)
print()
print()

for k in xrange(2, 11):
    cl = KMeans(n_clusters=k, init='k-means++', n_init=10, max_iter=300)
    cl = cl.fit(df)
    labels = cl.labels_
    score_km = silhouette_score(df, labels)
    score_ca = calinski_harabaz_score(df, labels)
    print k, score_km, score_ca
