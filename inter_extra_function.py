import numpy as np

def interextra(x, N0, k, b, t):
    """

    Parameters
    ----------
    x : float
        it represents the time value (in s) at which interpolation/extrapolation is performed
    N0 : float
        parameter extracted from the fit. It represents the initial number of decaying nuclei.
    k : float
        parameter extracted from the fit. It represents the decay constant.
    b : float
        parameter extracted from the fit. It represents a shift in the exponential fitting function.
    t : numpy.array
        array with the time values for ODE integration

    Description
    ----------
    This function calculate the number of remaining nuclei N at the selected time x.
    It is based on an interpolation/extrapolation from the fitting function N0 * np.exp(-k * x) + b
    using the parameters extracted from the fit N0, k, b.
  
    Returns
    -------
    This function checks if the input time 'x' is whitin the minimum and the maximum time values of the array 't',
    thus distinguishing the case of interpolation and extrapolation, 
    and returns a dictionary 'd' containing the number of remaining nuclei N at the selected time x.
    
    """
    # define the decreasing exponential function 'N', which is the same as the fitting function
    N = N0 * np.exp(-k * x) + b
    # convert the input array into a list 'l'
    l = t.tolist()
    # check if the input 'x' is whitin the minimum and the maximum time values of the array 't'
    if min(l) <= x <= max(l):
        # if 'x' is within the minimum and the maximum values of the array 't',
        # it is the interpolation case and it is printed the resulting 
        # number of remaining nuclei N at the time x
        print (f"Interpolation: if t = {x}, N = {N}" )
        #define a dictionary 'd' for the interpolation case. It contains the string 'Interpolation', 
        #the number of calculated remaining nuclei N and the selected time x
        d = dict(); 
        d['Case'] = "Interpolation"
        d['x']   = x
        d['N']   = N
        return d         
    else:
        # otherwise, it is the extrapolation case and it is printed the resulting
        # number of remaining nuclei N at a future time x
        print (f"Extrapolation: if t = {x}, N = {N}" )
        #define a dictionary 'd' for the extrapolation case. It contains the string 'Extrapolation', 
        #the number of calculated remaining nuclei N and the selected time x
        d = dict(); 
        d['Case'] = "Extrapolation"
        d['x']   = x
        d['N']   = N
        return d
