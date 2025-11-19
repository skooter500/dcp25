import tkinter as tk
root = tk.Tk()
root.geometry("300x250")

# Pack from top (default)
tk.Label(root, text="Top", bg="red").pack(side=tk.TOP, fill=tk.X)
tk.Label(root, text="Bottom", bg="blue").pack(side=tk.BOTTOM, fill=tk.X)
# Pack from left and right
tk.Label(root, text="Left", bg="green").pack(side=tk.LEFT, fill=tk.Y)
tk.Label(root, text="Right", bg="yellow").pack(side=tk.RIGHT, fill=tk.Y)
# Center (fills remaining space)
tk.Label(root, text="Center", bg="purple").pack(fill=tk.BOTH, expand=True)

root.mainloop()