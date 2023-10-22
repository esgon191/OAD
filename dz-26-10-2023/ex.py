import numpy as np 
import matplotlib.pyplot as plt 
  
# Define Data

x = np.arange(0, 15, 0.2)
data_1 = np.sin(x)
data_2 = np.cos(x) 
  
# Create Plot

fig, ax1 = plt.subplots() 
  
ax1.set_xlabel('X-axis') 
ax1.set_ylabel('Y1-axis', color = 'red') 
ax1.plot(x, data_1, color = 'red') 
ax1.tick_params(axis ='y', labelcolor = 'red') 
  
# Adding Twin Axes

ax2 = ax1.twinx() 
  
ax2.set_ylabel('Y2-axis', color = 'blue') 
ax2.plot(x, data_2, color = 'blue') 
ax2.tick_params(axis ='y', labelcolor = 'blue') 
 
# Show plot

plt.show()
