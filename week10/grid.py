import tkinter as tk

root = tk.Tk()
root.geometry("400x300")


tk.Label(root, text="Username:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
tk.Entry(root).grid(row=0, column=1, padx=10, pady=5)
tk.Label(root, text="Password:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
tk.Entry(root, show="*").grid(row=1, column=1, padx=10, pady=5)
tk.Button(root, text="Login").grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
