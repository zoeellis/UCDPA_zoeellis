#import CSV file into Pandas DataFrame

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt  #for visulisation
import seaborn as sns #for visulisation
data = pd.read_csv("/Users/zoeellis/Library/Containers/com.microsoft.Excel/Data/Desktop/Homelessness Report December 2021.csv")
data.head()
print(data)

#Extracting a pattern using regex
#count the total number of adults across all regions

#Checking to see if there is any missing data
print(data.isnull().sum())
# No missing Data Found

#Checking to see if there is any duplicate data
bool_series = data.duplicated()
print('Boolean series:')
print(bool_series)
#no duplicate data

#Interators

#merge Data Frama

#Visualaise with Seabourn 1

#Visualaise with Seabourn 2

