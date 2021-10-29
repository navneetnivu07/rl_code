import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def myFunc(value):
    array[1][2]=value
    im.set_array(array)

array = ([[1,2,3,4],
          [3,9,1,5],
          [8,4,1,7],
          [2,4,9,1]])

figure, ax = plt.subplots()
im = ax.imshow(array)                        
ax_slider = plt.axes([0.1, 0.1, 0.8, 0.03]) # [left, bottom, width, height]
slide = Slider(ax_slider, '', 0, 15, valinit=0)
slide.on_changed(myFunc)

plt.show()