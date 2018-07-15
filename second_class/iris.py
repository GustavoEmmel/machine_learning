from sklearn import datasets
import numpy as np


### Step 2. Leia o dataset iris
iris = datasets.load_iris()
# print iris

### Step 3. Crie as colunas para o dataset
# 1. sepal_length (in cm)
# 2. sepal_width (in cm)
# 3. petal_length (in cm)
# 4. petal_width (in cm)
# 5. class

def Step3(iris):
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

    return foo_bar

# print Step3(iris)

### Step 4.  Algum dado ausente?


### Step 5 Verifique os valores das linhas 10 ate 29 da coluna

def Step5(iris):
    foo_bar = Step3(iris)
    return foo_bar[10:30, 2:3]

# print Step5(iris)

### Step 6. Certo, modifique os valores NaN por 1.0


### Step 7. Agora delete a coluna da classe

def Step7(iris):
    foo_bar = Step3(iris)
    foo_bar_baz = np.delete(foo_bar, 4, 1)  # delete second column of C
    return foo_bar_baz

# print Step7(iris)

### Step 8.  Coloque as 3 primeiras linhas como NaN

def Step8(iris):
    foo_bar_baz = Step7(iris)
    foo_bar_baz[1:4, :] = "NaN"
    return foo_bar_baz

# print Step8(iris)

### Step 9.  Delete as linhas que contenham NaN

def Step9(iris):
    foo_bar_baz = Step8(iris)

    i = 0
    for r in foo_bar_baz:
        if "NaN" in r:
            foo_bar_baz = np.delete(foo_bar_baz, (i), axis=0)
        else:
            i = 1 + i

    return foo_bar_baz

# print Step9(iris)

### Step 10. Reset o index para que ele inicie em 0 novamente

# print Step9(iris)[:2, :]

