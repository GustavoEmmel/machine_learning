import numpy as np
from sklearn.model_selection import train_test_split

a = np.arange(10).reshape((5,2))
b = np.array([1,0,1,0,0])
# print a
# print b


x_train, x_test, y_train, y_test = train_test_split(
    a, b, test_size=0.2)

print x_train
print y_train
print x_test
print y_test