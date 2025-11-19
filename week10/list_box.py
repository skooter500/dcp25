import tkinter as tk

root = tk.Tk()
root.geometry("300x300")

tk.Label(root, text="Select items:").pack(pady=5)

# Create listbox
listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, height=8)
listbox.pack(padx=20, pady=10)

# Add items
items = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig"]
for item in items:
    listbox.insert(tk.END, item)

def get_selected():
    selected = [listbox.get(i) for i in listbox.curselection()]
    print(f"Selected: {selected}")

tk.Button(root, text="Get Selection", command=get_selected).pack(pady=5)

root.mainloop()