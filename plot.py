import matplotlib.pyplot as plt
from configparser import ConfigParser
import numpy as np

#load the array with 'odeint' results from the text file 'results.txt'
N = np.loadtxt('results.txt', dtype=float)

#read the configuration file 'config.ini' and get the value corresponding to 'filename'
parser = ConfigParser()
parser.read('config.ini')
filename = parser.get('config', 'filename')
# put the time values from the text file 'filename' into an array t
t = np.loadtxt(filename, unpack = 'True')

# plot the number N of remaining nuclei after a time t vs time t (in s)
plt.plot(t,N,'r-',linewidth=2)

# set x and y labels
plt.xlabel('time t')
plt.ylabel('N(t)')

# put the grid
plt.grid()
