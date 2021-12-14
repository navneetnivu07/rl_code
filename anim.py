
# importing the modules
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt

for i in range(1,11): 
    # generating 2-D 10x10 matrix of random numbers
    # from 1 to 100
    data = np.random.randint(low=1,
                            high=100,
                            size=(10, 10))
    data[i,i] = data[i,i] + i
    
    # setting the parameter values
    annot = True
    
    # plotting the heatmap
    hm = sn.heatmap(data=data,
                    annot=annot)
    
    # displaying the plotted heatmap
    plt.show()