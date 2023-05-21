    


# The following code implements canvas in tkinter:

import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width = 200, height = 100)
canvas.pack()

canvas.create_line(0, 0, 200, 100)
canvas.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

canvas.create_rectangle(50, 25, 150, 75, fill="blue")

root.mainloop()
    