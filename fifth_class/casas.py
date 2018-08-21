from sklearn import linear_model
from sklearn.model_selection import train_test_split

import pandas as pd


columns = ['size',
           'rooms',
           'value']

df = pd.read_csv("ex1data2.csv", names=columns)

print df.head()

# utiliza 25% do dataset para teste
train, test = train_test_split(df, test_size=0.2)

clf = linear_model.LinearRegression(normalize=True)
xs = train[['size', 'rooms']]
fs = train[['value']]

test_xs = test[['size', 'rooms']]
test_fs = test[['value']]

clf.fit(xs, fs)
predictions = clf.predict(test_xs)
score = clf.score(xs, fs)
print score


thetas = clf.coef_
independent = clf.intercept_
print thetas
print independent