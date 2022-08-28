import matplotlib.pyplot as plt
from readFile import readFile
from ode import N

# plot results
plt.plot(t,N,'r-',linewidth=2)

# set x and y labels
plt.xlabel('time t')
plt.ylabel('N(t)')

# put the grid
plt.grid()
