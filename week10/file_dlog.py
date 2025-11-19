import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.geometry("300x200")

def open_file():
    filename = filedialog.askopenfilename(
        title="Select a file",
        filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
    )
    if filename:
        print(f"Selected: {filename}")

def save_file():
    filename = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
    )
    if filename:
        print(f"Save as: {filename}")

tk.Button(root, text="Open File", command=open_file).pack(pady=20)
tk.Button(root, text="Save File", command=save_file).pack(pady=20)

root.mainloop()