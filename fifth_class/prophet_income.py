import pandas as pd

#encoding=utf-8
from matplotlib import pyplot as plt
import numpy as np

def hypothesis(x, t0, t1):
    return t0 + t1 * x


def cost_function(X, fx, h, t0, t1):
    soma = 0.
    N = len(X)

    for i in range(N):
        soma += (h(X[i], t0, t1) - fx[i]) ** 2.

    return (1. / (2. * float(N))) * soma

df = pd.read_csv('ex1data1.csv')

print df.head()

t0 = 0.5  # altere os pesos aqui
t1 = 0  # altere os pesos aqui

X = df['populacao']
fx = df['lucro']

print cost_function(X, fx, hypothesis, t0, t1)




def update_t0(X, fx, h, t0, t1, alpha):
    """
    Atualiza t0 com base nos N valores passados para esta funcao.
    """

    N = len(X)
    soma = 0.

    for i in range(N):
        soma += (h(X[i], t0, t1) - fx[i])

    return t0 - ((alpha * (1. / float(N))) * soma)


def update_t1(X, fx, h, t0, t1, alpha):
    """
    Atualiza t1 com base nos N valores passados para esta funcao.
    """
    N = len(X)

    soma = 0.
    for i in range(N):
        soma += (h(X[i], t0, t1) - fx[i]) * X[i]

    return t1 - ((alpha * (1. / float(N))) * soma)


t0 = 0.1
t1 = 1.
alpha = 0.5
df = pd.read_csv('ex1data1.csv')
X = df['populacao']
fx = df['lucro']






temp0 = update_t0(X, fx, hypothesis, t0, t1, alpha)
temp1 = update_t1(X, fx, hypothesis, t0, t1, alpha)

print 'antigo theta0: %f novo theta0: %f' % (t0, temp0)
print 'antigo theta1: %f novo theta1: %f' % (t1, temp1)

t0 = 0.1  # theta 0
t1 = 1.  # theta 1
alpha = 0.1  # taxa de aprendizado

df = pd.read_csv('ex1data1.csv')
X = df['populacao']
fx = df['lucro']

threshold = 0.001  # diferenca aceitavel entre custos
batch_size = 2  # tamanho do batch
epoch = 0
max_epoch = 10  # maximo numero de iteracoes permitido

prev = np.inf  # custo anterior
curr = cost_function(X, fx, hypothesis, t0, t1)  # custo atual
while (abs(curr - prev) > threshold) and (epoch < max_epoch):
    bc = 0  # contador de quantas instancias passaram pelo batch

    for i in range(batch_size):
        X_local = X[bc:(bc + batch_size)]
        fx_local = fx[bc:(bc + batch_size)]

        temp0 = update_t0(X_local, fx_local, hypothesis, t0, t1, alpha)
        temp1 = update_t1(X_local, fx_local, hypothesis, t0, t1, alpha)

        t0 = temp0
        t1 = temp1

        bc += 1

    prev = curr
    curr = cost_function(X, fx, hypothesis, t0, t1)
    print 'custo na epoca %d: %f' % (epoch, curr)
    epoch += 1