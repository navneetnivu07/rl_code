import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

i = 0

def test():
    global i
    array[1][2]=i
    im.set_array(array)
    # Loop over data dimensions and create text annotations.
    for i in range(4):
        for j in range(4):
            text = ax.text(j, i, array[i, j], ha="center", va="center", color="w")
    canvas.draw()
    i+=1
    root.after(300, test)

root = tk.Tk()
root.title("Something")

array = np.array([[1,2,3,4],
          [3,9,1,5],
          [8,4,1,7],
          [2,4,9,1]])

figure, ax = plt.subplots()
im = ax.imshow(array)

canvas = FigureCanvasTkAgg(figure, root)                
canvas.get_tk_widget().pack()                           

test()
root.mainloop()
