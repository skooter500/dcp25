import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/tuneindex.csv')
# Count tune types and plot
tune_counts = df['tune_type'].value_counts()
tune_counts.plot(kind='bar')
plt.show()