import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv('adult.csv')

df = df.iloc[:,5:6]
print df.head()

statuses = pd.unique(df.values.ravel('K'))
print statuses

new_df = df[1].replace(['Never-married'], 1)
