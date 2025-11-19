import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Treeview Table")

# Create Treeview widget
columns = ('Name', 'Age', 'City')
tree = ttk.Treeview(root, columns=columns, show='headings', height=8)

# Define headings
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)

# Add data
data = [
    ("Alice", 25, "Dublin"),
    ("Bob", 30, "Cork"),
    ("Charlie", 35, "Galway"),
    ("Diana", 28, "Limerick")
]

for row in data:
    tree.insert('', tk.END, values=row)

# Add scrollbar
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)

tree.grid(row=0, column=0, sticky='nsew')
scrollbar.grid(row=0, column=1, sticky='ns')

root.mainloop()