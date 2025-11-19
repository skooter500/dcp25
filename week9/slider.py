import tkinter as tk

root = tk.Tk()
root.geometry("400x300")

value_label = tk.Label(root, text="Value: 50")
value_label.pack(pady=20)

def update_label(val):
    value_label.config(text=f"Value: {int(val)}")

# Horizontal slider
scale1 = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL,
command=update_label, length=300)

scale1.set(50)

scale1.pack(pady=10)

# Vertical slider
scale2 = tk.Scale(root, from_=0, to=100, orient=tk.VERTICAL, length=150)
scale2.pack(pady=10)

root.mainloop()