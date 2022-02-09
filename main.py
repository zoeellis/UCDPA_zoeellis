#import CSV file into Pandas DataFrame

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv("/Users/zoeellis/Library/Containers/com.microsoft.Excel/Data/Desktop/Homelessness Report December 2021.csv")
data.head()
print(data)

#Extracting a pattern using regex

#Checking to see if there is any missing data
print(data.isnull().sum())
# No missing Data Found

#Checking to see if there is any duplicate data

#Visualaise with Seabourn 1

#Visualaise with Seabourn 2

