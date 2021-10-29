import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def myFunc(value):
    print(value)
    
    array[1][2]=value

    im.set_array(array)
    canvas.draw()                        

i = 0

def test():
    global i
    print('test')
    myFunc(i)
    i+=1
    root.after(300, test)

root = tk.Tk()
root.title("Something")

array = ([[1,2,3,4],
          [3,9,1,5],
          [8,4,1,7],
          [2,4,9,1]])

figure, ax = plt.subplots()
im = ax.imshow(array)

canvas = FigureCanvasTkAgg(figure, root)                
canvas.get_tk_widget().pack()                           

test()
root.mainloop()
