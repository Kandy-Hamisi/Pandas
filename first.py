# pandas are easy to learn :)

import pandas as pd

# creating dataframes from scratch

data = {
    'apples': [3, 2, 0, 1],
    'oranges': [0, 3, 7, 2]
}

# Pass the dataframe to the DataFrame Constructor

purchases = pd.DataFrame(data, index=['June', 'Robert', 'Lily', 'David'])

# print(purchases)
print(purchases.loc['June']) '''Locating a customer's order by using their name'''


# df = pd.read_csv('purchases.csv', index_col=0)
# print(df)





'''For an SQL database...Install pysqlite3 and import sqlite3'''
#df = pd.read_sql_query("SELECT * FROM purchases", con)
df = df.set_index('index')
#df