import numpy as np
import pandas as pd

zeros = np.zeros((5, 5))
print zeros

ones = np.ones((2, 4))
print ones

equals = np.full((3,6), 7.)
print equals

identity = np.eye(2)
print identity

randons = np.random.random((2,8))
print(randons)


a = np.array([
    [10,20,30,40],
    [50,60,70,89],
    [90,100,110,120]
             ])

print(a)

# vou pegar as linhas 0 e 1 e as colunas 1 e 2
# o ultimo valor sempre eh excluido da busca

b = a[:2, 1:3]
print(b)

# para pegar uma linha especifica, no caso a linha 2 (indice 1)
c = a[1, :]
print c, c.shape

d = a[1:2, :]
print d, d.shape


# ----------------

a = np.arange(3*3).reshape(3,3)
print a

# multiplicando todos os valores da matriz por 3
print a*3

# cast all numbers in array to float32
x = np.array([
    [10, 20],
    [30, 40]
], dtype=np.float32)

y = np.array([
    [50, 60],
    [70, 80]
], dtype=np.float32)

print x, y

v = np.array([90, 100])
w = np.array([110, 120])

# somando matrizes
print v.dot(w)
print np.dot(v, w)

print ""
print x
# imprimindo matriz transposta
print x.T

# concatenando matrizes

print "------------"
a = np.array(
    [10,20,30]
)
print a
print a.reshape(1, a.size)
print ""
b = np.array([
    [10,20,30],
    [40,50,60]
])
print b
print ""

print np.concatenate((a.reshape(1, a.size),b), axis=0)

print ""

print " Pandas "

s = pd.Series([1,3,5,np.nan,6,8])
print s


dates = pd.date_range('20130101', periods=6)
print dates

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print df

print ""

print df.head() # primeiros n-1
print df.tail(3) # ultimos 3
print df.index # linhas
print df.columns # colunas
print df.values # matrix

print ""

print df.describe() # sumary
print df.T
print df.sort_index(axis=1, ascending=False)
print df.sort_values(by='B') # ordernar pela coluna B crescente

print ""

print df['A']
print df[0:3]
print df.loc[dates[0]]
print df.loc[:,['A','B']]
print df.loc['20130102':'20130104',['A','B']]
print df.loc['20130102',['A','B']]

print "mediana"
print df.mean()

print ""


df = pd.DataFrame({
    'A' : ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
    'B' : ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
    'C' : np.random.randn(8),
    'D' : np.random.randn(8)})
print df
print df.groupby('A').sum()
