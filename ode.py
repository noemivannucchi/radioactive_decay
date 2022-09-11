from scipy.integrate import odeint
import numpy as np
from model import model
from readFile import verifyFile
from setn0 import verifyN0
from setnuclei import verifynuclei
from configparser import ConfigParser

#read the configuration file 'config.ini'
#in the configuration file you can choose:
    #the type of nuclei among "Uranium238", "Plutonium239" or "Radium226"
    #the initial number of nuclei N0
    #the name of a text file with time values
parser = ConfigParser()
parser.read('config.ini')

#get the value corresponding to 'N0' from the file "config.ini" and convert it into an integer
N0_string = parser.get('config', 'N0')
N0 = int(N0_string)

#get the value corresponding to 'nuclei' from the file "config.ini"
nuclei = parser.get('config', 'nuclei')

#get the value corresponding to 'filename' from the file "config.ini"
filename = parser.get('config', 'filename')
    
# put the time values from the text file 'filename' into an array t
# type(t) = numpy.ndarray
t = np.loadtxt(filename, unpack = 'True')

# solve ODE 
# type(N) = numpy.ndarray
N = odeint(model,verifyN0(N0),verifyFile(t),args=(verifynuclei(nuclei),))

#save the array with 'odeint' results in a text file 'results.txt'
np.savetxt('results.txt', N, fmt='%d')
