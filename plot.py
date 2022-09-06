import matplotlib.pyplot as plt
from readFile import verifyFile
from ode import N, t

# plot the number N of remaining nuclei after a time t vs time t (in s)
plt.plot(verifyFile(t),N,'r-',linewidth=2)

# set x and y labels
plt.xlabel('time t')
plt.ylabel('N(t)')

# put the grid
plt.grid()
