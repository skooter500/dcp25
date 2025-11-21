import tkinter as tk
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def on_click():
    label.config(text=f"Hello " + entry.get() )


root = tk.Tk()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

x = ["Arsenal", "Leixlip Utd", "Manchester", "Barcelona"]
y1 = [3, 24, 17, 22]

categories = ["Car", "Bus", "Bike", "Walk"]
values = [10, 8, 8, 1]


ax1.plot(x, y1, color='red')
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