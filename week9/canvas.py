import tkinter as tk

root = tk.Tk()
root.geometry("500x400")

canvas = tk.Canvas(root, width=450, height=350, bg="white")
canvas.pack(pady=10)

# Draw shapes
canvas.create_line(50, 50, 400, 50, fill="blue", width=3)
canvas.create_rectangle(50, 100, 150, 200, fill="red", outline="black")
canvas.create_oval(200, 100, 300, 200, fill="green")
canvas.create_polygon(350, 100, 400, 150, 350, 200, fill="yellow")

# Draw text
canvas.create_text(225, 250, text="Canvas Graphics", 
                  font=("Arial", 20, "bold"))

root.mainloop()