# pandas are easy to learn :)

import pandas as pd

# creating dataframes from scratch

data = {
    'apples': [3, 2, 0, 1],
    'oranges': [0, 3, 7, 2]
}

# Pass the dataframe to the DataFrame Constructor

purchases = pd.DataFrame(data, index=['June', 'Robert', 'Lily', 'David'])
# purchases = pd.DataFrame(data)

# print(purchases)
"""Locating a customer's order by using their name"""
print(purchases.loc['Lily']) 
# print(purchases)


# df = pd.read_csv('purchases.csv', index_col=0)
# print(df)




# '''For an SQL database...Install pysqlite3 and import sqlite3'''
# #df = pd.read_sql_query("SELECT * FROM purchases", con)
# df = df.set_index('index')
# #df


# making data frame from csv file
data = pd.read_csv("nba.csv", index_col ="Year")
  
# retrieving row by loc method
first = data.loc["Avery Bradley"]
second = data.loc["R.J. Hunter"]
  