from inter_extra_function import interextra
from configparser import ConfigParser
import numpy as np

parser = ConfigParser()

# read the configuration file 'config.ini' and get the value corresponding to 'filename'
parser.read('config.ini')
filename = parser.get('config', 'filename')
# put the time values from the text file 'filename' into an array t
t = np.loadtxt(filename, unpack = 'True')


#load the array with the parameters extracted from the fit from the text file 'par_from_fit.txt'
params = np.loadtxt('par_from_fit.txt', dtype=float)
# extract the parameters from the array 'params'
N0, k, b = params


#read the configuration file 'configfit.ini'
#This configuration file allows you to set the 'x' value of the fitting function y = N0 * exp(-k * x) + b
#in order to make an interpolation or extrapolation of the corresponding y value.
# - x represents a time value (in s)
# - N0, k, b are the parameters extracted from the fit
# As an example, this file contains a time value for extrapolation in the case of "Radium226".
parser.read('configx.ini')

#get the value corresponding to 'x' from the file "configx.ini" and convert it into a float
x_string = parser.get('configx', 'x')
x = float(x_string)


#Do the interpolation/extrapolation to extract the number of remaining nuclei at a time x,
#set in 'configx.ini' file, using the fitting function N0 * np.exp(-k * x) + b
#and the parameters extracted from the fit N0, k, b.
#As an example, here it is an extrapolation with x = 2e11 s
interextra(x, N0, k, b, t)


