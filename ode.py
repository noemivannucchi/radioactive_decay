from scipy.integrate import odeint
import numpy as np
from model import model
from readFile import verifyFile
from setn0 import verifyN0
from setnuclei import verifynuclei

# insert the initial condition to solve ODE
N0 = 100

#choose the type of nuclei among "Uranium238", "Plutonium239" or "Radium226"
nuclei = 'Radium226'

# ask the user to insert the name of a text file with time values
filename = input('Insert the filename with the times: ')
    
# put the time values from the text file into an array t
t = np.loadtxt(filename, unpack = 'True')

# solve ODE
N = odeint(model,verifyN0(N0),verifyFile(t),args=(verifynuclei(nuclei),))
