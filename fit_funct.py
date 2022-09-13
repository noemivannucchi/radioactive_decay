import numpy as np

def fitfunct(x, N0, k, b):
    """
    This is the definition of the function for the fit.
    It represents a decreasing exponential functon.
    
    The input values are: 
        - x which is the variable of the function
        - N0, k which are float positive constants
        - b which is a float constant
    
    This function returns a decreasing exponential function
    which depends on the variable x
    using the input parameters
    """
    return N0 * np.exp(-k * x) + b