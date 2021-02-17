import sys
sys.path.insert(1, './lib/python3.8/site-packages')
import pandas as pd
import googletrans
import matplotlib.pyplot as plt; plt.rcdefaults()


data = pd.read_csv('covid.csv') 

print(data.isna().sum)