import tkinter as tk
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import pandas as pd
import sqlite3
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


albums_df = pd.read_csv("data/album.csv")
albums_by_artist = albums_df['artist'].value_counts()
print(albums_by_artist.head())

# artists = 

'''
conn = sqlite3.connect('data/tunes.db')
cursor = conn.cursor()

# Create table
cursor.execute('select count(*) as count, artist from albums group by artist')

albums_by_artist = cursor.fetchall()

print(albums_df.head())
'''
def on_click():
    ax1.set_title(entry.get())
    canvas.draw()


root = tk.Tk()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

x = ["Arsenal", "Leixlip Utd", "Manchester", "Barcelona"]
y1 = [3, 24, 17, 22]

categories = ["Car", "Bus", "Bike", "Walk"]
values = [10, 8, 8, 1]
d

ax1.plot(albums_by_artist.index.tolist(), albums_by_artist.values.tolist(), color='red')
ax1.set_title('First Plot')
ax2.bar(categories, values, color='blue')
ax2.set_title('Second Plot')

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()

label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

button = tk.Button(root, text="Click Me!", command=on_click)
button.pack()

# Text entry
entry = tk.Entry(root, width=30)
entry.pack()


canvas.get_tk_widget().pack()



root.mainloop()