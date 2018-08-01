# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 14:36:49 2018

@author: Everton Thomas e Gustavo Emmel

Suporte: Fração das transações que contém X e Y

Confiança: Frequência que itens em Y aparecem em transações que contem X

Lift: Probabilidade de ocorrência de X e Y independente de um ou outro
    1 = Indica independêcia
    1 < Indica correlação positiva
    1 > Indica correção negativa

 Encontrar, para um único país (ex Italia),
 regras usando o algoritmo apriori, como visto no exemplo no jupyter.
 Utilizar medidas de suporte, confiança e lift Testar alguns valores
 Definir possíveis melhores valores para tais medidas utilizadas

"""

import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

data = pd.read_excel('Online Retail.xlsx', 'Online Retail', index_col=None)
data = data.loc[data['Country'].str.contains("France")]

# print data.head()

dummies = pd.get_dummies(data['StockCode'])

combine = pd.concat([data['InvoiceNo'], dummies], axis=1)

transactions = combine.groupby(['InvoiceNo']).sum().reset_index()

transactions = transactions.drop(['InvoiceNo'], axis=1)

#Alguns itens aparecem com indicador 2, ao inves de 0 e 1.
#Entao normalizo tudo para 1 quando
transactions[~transactions.isin([0,1])] = 1

#encontrando regras com no minimo 5% de suporte
frequent_items = apriori(transactions, min_support=0.05, use_colnames=True)

#encontrar regras com lift maior que 1
rules = association_rules(frequent_items, metric='lift', min_threshold=1)
print rules

#10 primeiras regras com maior suporte
print "ordenado por suporte"
print rules.sort_values('support', ascending= False).head(10)

#10 primeiras regras com maior confianca
print "ordenado por confianca"
print rules.sort_values('confidence', ascending= False).head(10)

#10 primeiras regras com maior lift
print "ordenado por lift"
print rules.sort_values('lift', ascending= False).head(10)

# pegamos os dados de vendas da Franca agrupando os itens por stock code e chegamos nas conclusoes a seguir:

#selecionando regras com lift maior que 2, confianca maior que 0.6 e suporte maior que 0.1
print "melhores combos com lift maior que 2"
print rules[(rules['lift'] >= 2) & (rules['confidence'] >= 0.6) & (rules['support'] >= 0.1 )]
# so possuem 2 combos com lift maior que 2
print rules[(rules['lift'] >= 1) & (rules['confidence'] >= 0.6) & (rules['support'] >= 0.1 )]
# quando baixamos o lift para 1 temos 8 combinacaoes
print rules[(rules['lift'] >= 0.5) & (rules['confidence'] >= 0.9) & (rules['support'] >= 0.1 )]
# percebemos que temos 2 combinacoes com alto lift e alta confianca
print rules[(rules['lift'] >= 0.9) & (rules['confidence'] >= 0.9) & (rules['support'] >= 0.1 )]