from sklearn import datasets
import numpy as np


### Step 2. Leia o dataset iris
iris = datasets.load_iris()
print iris

### Step 3. Crie as colunas para o dataset
# 1. sepal_length (in cm)
# 2. sepal_width (in cm)
# 3. petal_length (in cm)
# 4. petal_width (in cm)
# 5. class

columns = np.array([
    ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
])

foo = []
i = 0
for v in iris.target:
    foo.append(iris.target_names[v])
    i = 1 + i

iris_data = iris.data[:, :]
bar = []
i = 0
for v in iris.data:
    bar.append(np.append(iris_data[i], foo[i]))
    i = i + 1

foo_bar = np.concatenate((columns, bar), axis=0)

print foo_bar

### Step 4.  Algum dado ausente?


### Step 5 Verifique os valores das linhas 10 ate 29 da coluna

print foo_bar[10:30, 2:3]
