import pandas as pd
import numpy as np

data = pd.read_excel('Online Retail.xlsx', 'Online Retail', index_col=None)
data = data.loc[data['Country'].str.contains("Italy")]


# Add extra fields
data['TotalAmount'] = data['Quantity'] * data['UnitPrice']
data['InvoiceYear'] = data['InvoiceDate'].dt.year
data['InvoiceMonth'] = data['InvoiceDate'].dt.month
data['InvoiceYearMonth'] = data['InvoiceYear'].map(str) + "-" + data['InvoiceMonth'].map(str)

print data.head()

print data.describe()

print len(data['InvoiceNo'].unique())

print "Get top ranked ranked customers based on the total amount"
customers_amounts = data.groupby('CustomerID')['TotalAmount'].agg(np.sum).sort_values(ascending=False)
print customers_amounts.head(20)


print "Frequently sold items by quantitiy"
gp_stockcode = data.groupby('Description')
gp_stockcode_frq_quantitiy = gp_stockcode['Quantity'].agg(np.sum).sort_values(ascending=False)
print gp_stockcode_frq_quantitiy.head(20)

print "Frequently sold items by total amount"
gp_stockcode_frq_amount = gp_stockcode['TotalAmount'].agg(np.sum).sort_values(ascending=False)
print gp_stockcode_frq_amount.head(20)


print len(data[data['Description'].isnull()])

for i, d in data[data['Description'].isnull()].iterrows():
    data['Description'][i] = "Code-" + str(d['StockCode'])

print len(data[data['Description']==data['StockCode'].map(lambda x: "Code-"+str(x))])

gp_invoiceno = data.groupby('InvoiceNo')

print gp_invoiceno

# transactions = []
# for name,group in gp_invoiceno:
#     transactions.append(list(group['Description'].map(str)))
#
# df_transactons = pd.get_dummies(transactions)
#
# print transactions
# print df_transactons

# from apyori import apriori
# rules = apriori(transactions, min_support = 0.005, min_confidence = 0.2, min_lift = 3, min_length = 2)
# # Get the results
# results = list(rules)
#
# print results



# data_xls.to_csv('online_retail.csv', encoding='utf-8', index=False)

# df = pd.read_csv('online_retail.csv')
#
# df = df.loc[df['Country'].str.contains("Italy")]
# df = df.reset_index(drop=True)
#
# products = pd.unique(df['Description'].values.ravel('K'))

# print len(df[df['Description'].isnull()])


# print products


# gp_invoiceno = df.groupby('InvoiceNo')
#
# print gp_invoiceno

# transactions = []
# for name,group in gp_invoiceno:
#     transactions.append(list(group['Description'].map(str)))
#
# print transactions
#
#
# from apyori import apriori
# rules = apriori(transactions, min_support = 0.005, min_confidence = 0.2, min_lift = 3, min_length = 2)
# # Get the results
# results = list(rules)
# print results