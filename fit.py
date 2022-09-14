import matplotlib.pyplot as plt
from configparser import ConfigParser
import numpy as np
import scipy.optimize
from fit_funct import fitfunct
from compare_params import compareparams

#load the array with 'odeint' results from the text file 'results.txt'
N = np.loadtxt('results.txt', dtype=float)

#read the configuration file 'config.ini' and get the value corresponding to 'filename'
parser = ConfigParser()
parser.read('config.ini')
filename = parser.get('config', 'filename')
# put the time values from the text file 'filename' into an array t
t = np.loadtxt(filename, unpack = 'True')


#read the configuration file 'configfit.ini'
#in the configuration file you can set the initial parameters for the fitting function 'fitfunct':
    #N0 which is the initial number of nuclei
    #k which is the decay constant (in s^-1) related to the chosen nuclei
    #b which is a constant that has to be close to 0 in this model
parser.read('configfit.ini')

#get the value corresponding to 'N0', 'k' and 'b' from the file "configfit.ini" and convert it into an integer
#and two floats, respectively
N0_string = parser.get('configfit', 'N0')
N0_i = int(N0_string)
k_string = parser.get('configfit', 'k')
k_i = float(k_string)
b_string = parser.get('configfit', 'b')
b_i = float(b_string)


# start with parameters (N0_i,k_i,b_i) near those we expect for "Radium226" as an example
#they are taken from the configuration file 'configfit.ini'
p0 = (N0_i, k_i, b_i) 
# perform the fit using the function 'fitfunct'
params, cov = scipy.optimize.curve_fit(fitfunct, t, N, p0)
# save the array 'params' with the parameters from the fit in a text file 'par_from_fit.txt'
np.savetxt('par_from_fit.txt', params)
# extract the parameters from the fit
N0, k, b = params

# determine quality of the fit by calculating R squared
squaredDiffs = np.square(N - fitfunct(t, N0, k, b))
squaredDiffsFromMean = np.square(N - np.mean(N))
rSquared = 1 - np.sum(squaredDiffs) / np.sum(squaredDiffsFromMean)
print(f"R² = {rSquared}")

# plot the fit curve on the initial data
plt.plot(t, N, '.', label="data")
plt.plot(t, fitfunct(t, N0, k, b), '--', label="fit")

# Get the standard deviations of the parameters (square roots of the diagonal of the covariance)
stdevs = np.sqrt(np.diag(cov))

#print the parameters extracted from the fit with their standard deviation
print (f"N0 = {N0} +/- {stdevs[0]}" )
print (f"k = {k} +/- {stdevs[1]}" )
print (f"b = {b} +/- {stdevs[2]}" )

#check that the parameters extracted from the fit are coherent with the expected ones
compareparams(p0,N0,k,b,stdevs)
