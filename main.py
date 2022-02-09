#import CSV file into Pandas DataFrame

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv("/Users/zoeellis/Library/Containers/com.microsoft.Excel/Data/Desktop/Homelessness Report December 2021.csv")
data.head()
print(data)


