import pandas as pd

data = {
    'masala': ["Millie", "Dan", "Fib", "Kate"],
    'plain': ["Marto", "Mercy", "Aaron", "Sandra"],
    'plain': ["Marto", "Mercy", "Aaron", "Sandra"]
}

purchases = pd.DataFrame(data, index=["Jan", "Feb", "March", "April"])
print(purchases.drop_duplicates(data))