import matplotlib.pyplot as plt
from configparser import ConfigParser
import numpy as np
import scipy.optimize
from fit_funct import fitfunct

#load the array with 'odeint' results from the text file 'results.txt'
N = np.loadtxt('results.txt', dtype=float)

#read the configuration file 'config.ini' and get the value corresponding to 'filename'
parser = ConfigParser()
parser.read('config.ini')
filename = parser.get('config', 'filename')
# put the time values from the text file 'filename' into an array t
t = np.loadtxt(filename, unpack = 'True')


# start with parameters (N0,k,b) near those we expect for "Radium226" as an example
p0 = (100, 1e-11, 0.) 
# perform the fit using the function 'fitfunct'
params, cov = scipy.optimize.curve_fit(fitfunct, t, N, p0)
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