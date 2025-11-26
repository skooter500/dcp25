---
marp: true
theme: default
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
style: |
  section {
    font-size: 28px;
  }
  h1 {
    color: #2d3748;
  }
  h2 {
    color: #667eea;
  }
  code {
    background: #f7fafc;
    padding: 2px 8px;
    border-radius: 4px;
  }
---

# **Introduction to Pandas**
## Data Analysis with Python

---

## What is Pandas? 🐼

**Pandas** is Python's most popular library for data analysis and manipulation

- Built on top of NumPy
- Provides easy-to-use data structures
- Essential for data science workflows
- Used by millions of data professionals

> "Pandas makes working with data feel natural and intuitive"

---

## Why Learn Pandas?

- **Industry Standard** - Used in data science, finance, research, and more
- **Powerful** - Handle datasets with millions of rows
- **Versatile** - Read/write Excel, CSV, SQL, JSON, and more
- **Fast** - Optimized C code under the hood
- **Open Source** - Free and constantly improving

---

## Core Data Structures

### **DataFrame** - The main workhorse
- 2D table with rows and columns
- Like an Excel spreadsheet, but programmable
- Each column can have different data types

### **Series** - A single column
- 1D array with labels
- Think of it as one column from a DataFrame

---

## Our Dataset: Irish Traditional Music 🎵

We'll be working with a real dataset of **24,000 traditional Irish tunes**

**Source:** The Session (thesession.org) - world's largest collection of Irish traditional music

**Format:** ABC notation - a text-based music notation system

---

## Dataset Features

### What's in our data?

| Column | Description | Example |
|--------|-------------|---------|
| `id` | Unique identifier | 1, 2, 3... |
| `title` | Tune name | "Cooley's" |
| `tune_type` | Category | reel, jig, hornpipe |
| `key_sig` | Musical key | Emin, Dmaj, Gmaj |
| `time_sig` | Time signature | 4/4, 6/8, 9/8 |
| `downloaded` | Popularity metric | 4432, 2721... |
| `notation` | ABC music code | Full tune notation |

---

## Sample Data

```
id  | title                | tune_type | key_sig | downloads
----|----------------------|-----------|---------|----------
1   | Cooley's             | reel      | Emin    | 4432
2   | Bucks Of Oranmore    | reel      | Dmaj    | 2721
3   | Boil The Breakfast   | reel      | Gmaj    | 812
10  | The Butterfly        | slip jig  | Emin    | 2767
12  | Cliffs Of Moher      | jig       | Ador    | 2850
```

---

## Types of Tunes in Irish Music

### **Reels** (4/4 time)
Fast dance tunes, most common type

### **Jigs** (6/8 time)
Bouncy, lilting rhythm

### **Hornpipes** (4/4 time)
Slower than reels, swung rhythm

### **Slip Jigs** (9/8 time)
Graceful, flowing tunes

---

## Essential Pandas Operations

```python
import pandas as pd

# Load data
df = pd.read_csv('tuneindex.csv')

# Explore
df.head()          # First 5 rows
df.info()          # Column types and info
df.describe()      # Statistical summary
```

---

## Essential Pandas Operations (cont.)

```python
# Select columns
df['title']                    # Single column
df[['title', 'tune_type']]     # Multiple columns

# Filter rows
df[df['tune_type'] == 'reel']  # Only reels
df[df['downloaded'] > 1000]    # Popular tunes

# Sort
df.sort_values('downloaded', ascending=False)
```

---

## Essential Pandas Operations (cont.)

```python
# Group and aggregate
df.groupby('tune_type')['downloaded'].mean()

# Count values
df['tune_type'].value_counts()

# Handle missing data
df.dropna()           # Remove missing
df.fillna(value)      # Fill missing
```

---

## Questions We'll Answer

1. What's the most popular tune type?
2. Which key signature is most common?
3. Is there a relationship between key and popularity?
4. What makes a tune popular?
5. How do different tune types compare?
6. Are certain time signatures more popular?

---

### Lesson 1: Load and Explore

```python
import pandas as pd

# Your first pandas code!
df = pd.read_csv('tuneindex.csv')

print(f"We have {len(df)} tunes!")
print(f"Columns: {list(df.columns)}")
print(f"\nFirst tune:")
print(df.iloc[0])
```

---

## Installing Pandas

```bash
pip install pandas
```

### Verify Installation
```python
import pandas as pd
print(pd.__version__)
```

---

## Let's Look at Real Data

```python
import pandas as pd

df = pd.read_csv('tuneindex.csv')

# What's the most popular tune?
most_popular = df.nlargest(1, 'downloaded')
print(most_popular[['title', 'tune_type', 'downloaded']])

# Output:
#   title     tune_type  downloaded
# 9 Banish Misfortune  jig    4292
```

## Common Pandas Patterns

You'll use these constantly:

```python
# Load → Filter → Group → Visualize
df = pd.read_csv('data.csv')
reels = df[df['tune_type'] == 'reel']
avg_by_key = reels.groupby('key_sig')['downloaded'].mean()
avg_by_key.plot(kind='bar')
```

This workflow applies to ANY dataset!

---

## Example: First Analysis

**Question:** How many tune types are in our dataset?

```python
import pandas as pd

df = pd.read_csv('tuneindex.csv')
tune_types = df['tune_type'].value_counts()

print(tune_types)
```

**Output:**
```
reel        12450
jig          7832
hornpipe     2234
slip jig      892
...
```

---

## The Power of Pandas

### Before Pandas:
```python
# Reading CSV manually - 50+ lines of code
# Filtering data - loops and conditions
# Grouping - complex dictionary logic
# Plotting - connecting to other libraries
```

### With Pandas:
```python
df = pd.read_csv('data.csv')
df[df['type'] == 'reel'].groupby('key')['downloads'].mean().plot()
```

**One line does it all!**

---

## Questions to Think About

As we begin, consider:

- What makes some tunes more popular than others?
- Do certain keys sound "better" to listeners?
- How has Irish music evolved over time?
- Can we predict a tune's popularity?
- What cultural factors influence tune types?

**Data can help answer these questions!**
