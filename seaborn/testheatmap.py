import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tips = pd.read_csv('tips.csv') 

sns.scatterplot(x='total_bill', y='tip', hue='sex', data = tips)
plt.show()
