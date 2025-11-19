import tkinter as tk

def on_click():
    label.config(text=f"Hello " + entry.get() )

root = tk.Tk()
root.geometry("400x300")
# Simple label
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

button = tk.Button(root, text="Click Me!", command=on_click)
button.pack()

# Text entry
entry = tk.Entry(root, width=30)
entry.pack()

## Multi Line Text 
text = tk.Text(root, height=15, width=50)
text.pack(side=tk.LEFT, pady=10, padx=10)
scrollbar = tk.Scrollbar(root, command=text.yview)
scrollbar.pack(side=tk.LEFT, fill=tk.Y)
text.config(yscrollcommand=scrollbar.set)
# Insert some text
text.insert(1.0,
"Type your text here...\n")


root.mainloop()