import numpy as np

def fitfunct(x, N0, k, b):
    """
    Parameters
    ----------
    x : float
        it is the variable of the function.
    N0 : float
        it is a float positive constant.
    k : float
        it is a float positive constant.
    b : float
        it is a float constant.
    
    Description
    ----------
    This is the definition of the function for the fit.
    It represents a decreasing exponential functon.
    
    Returns
    -------
    This function returns a decreasing exponential function
    which depends on the variable x
    using the input parameters.

    """
    #return a decreasing exponential function in the variable x with N0, k and b constants
    return N0 * np.exp(-k * x) + b
