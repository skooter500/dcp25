import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
tk.Label(root, text="Select country:").pack(pady=20)
# Create combobox
countries = ["USA", "UK", "Canada", "Australia", "India"]
combo = ttk.Combobox(root, values=countries, state="readonly")
combo.pack(pady=10)
combo.current(0) # Set default selection

def on_select(event):
    print(f"Selected: {combo.get()}")

combo.bind("<<ComboboxSelected>>", on_select)

root.mainloop()