
# this file is to be ignored


import pandas



mydata = pandas.DataFrame(data2015)

# Display the number of rows
print(len(mydata))
# Displays the number of columns
print(len(mydata.columns))

print(mydata.drop_duplicates(data2015, index=['Year', 'Hunters', 'Days']))


import pandas as pd
mydata = pandas.DataFrame(data2015)

#Display the first 7 rows
result = mydata.head(7)
print("First 10 rows of the DataFrame:")
print(result)


# making data frame from csv file
mydata = pandas.DataFrame(data2015, index_col =['Year', 'Hunters', 'Days'])
  
# retrieving row by loc method
print(mydata.loc["3", "5"])
  

print(mydata['Days'].mean())