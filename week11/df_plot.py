import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/tuneindex.csv')

print(df.head())
print("\n" * 5)
print(df.info())
print("\n" * 5)
print(df.describe())

print(df['title'])                    # Single column
print("\n" * 5)
print(df[['title', 'tune_type']])     # Multiple columns
print("\n" * 5)
# Filter rows
filt = df['tune_type'] == 'reel'
print(len(filt))
print(filt[0])

f1 = [False] * 24482
f1[0] = True
print(df[f1])  # Only reels
print("\n" * 5)

print("\n" * 5)
pop = df[df['downloaded'] > 1000]
sorted = pop.sort_values("downloaded", ascending=False)
print(sorted[["title", "file_name"]])    # Popular tunes


sorted[["title", "file_name"]].plot()

plt.plot(sorted["downloaded"], sorted["title"])

# Sort
dsorted = df.sort_values('downloaded', ascending=True)
print("\n" * 5)

df.sort_values("title", ascending = True, inplace=True)



ax = df['tune_type'].value_counts().plot.bar(figsize=(10, 6))

# Customize it (matplotlib)
ax.set_title('Tune Types in Irish Traditional Music', fontsize=16)
ax.set_xlabel('Tune Type', fontsize=12)
ax.set_ylabel('Count', fontsize=12)
ax.grid(axis='y', alpha=0.3)

plt.show()

print(df[["title", "downloaded"]].head())
