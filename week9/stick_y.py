import tkinter as tk

root = tk.Tk()
root.title("Sticky Parameter Demo")
root.geometry("400x400")

# Configure grid to have weight (so cells can expand)
for i in range(3):
    root.grid_rowconfigure(i, weight=1, minsize=100)
    root.grid_columnconfigure(i, weight=1, minsize=100)

# Different sticky examples
tk.Button(root, text="No sticky\n(centered)").grid(row=0, column=0)

tk.Button(root, text="sticky='w'\n(left)").grid(row=0, column=1, sticky='w')

tk.Button(root, text="sticky='e'\n(right)").grid(row=0, column=2, sticky='e')

tk.Button(root, text="sticky='n'\n(top)").grid(row=1, column=0, sticky='n')

tk.Button(root, text="sticky='s'\n(bottom)").grid(row=1, column=1, sticky='s')

tk.Button(root, text="sticky='ew'\n(stretch horizontal)").grid(row=1, column=2, sticky='ew')

tk.Button(root, text="sticky='ns'\n(stretch\nvertical)").grid(row=2, column=0, sticky='ns')

tk.Button(root, text="sticky='nsew'\n(fill entire cell)").grid(row=2, column=1, sticky='nsew')

tk.Button(root, text="sticky='nw'\n(top-left corner)").grid(row=2, column=2, sticky='nw')

root.mainloop()