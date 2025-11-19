import tkinter as tk

root = tk.Tk()
root.geometry("400x300")

label = tk.Label(root, text="Click or press keys", font=("Arial", 14))
label.pack(pady=50)

def on_click(event):
    label.config(text=f"Clicked at ({event.x}, {event.y})")

def on_key(event):
    label.config(text=f"Key pressed: {event.char}")

def on_enter(event):
    label.config(bg="lightblue")

def on_leave(event):
    label.config(bg="white")

label.bind("<Button-1>", on_click)      # Left click
root.bind("<Key>", on_key)              # Any key
label.bind("<Enter>", on_enter)         # Mouse enter
label.bind("<Leave>", on_leave)         # Mouse leave

root.mainloop()