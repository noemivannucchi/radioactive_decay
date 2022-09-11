def verifyN0 (N0):
    """ 
    The input 'N0' represents the initial number of radioactive nuclei
    and it is the initial condition of the differential states.
    
    This function checks that the input value 'N0' is an integer greater than 0
    and it returns the same value.
    
    If 'N0' is not an integer, it returns a TypeError, 
    while if 'N0' is not greater than 0, it returns a ValueError
    
    """
    #verify that the initial number of radioactive nuclei N0 is an integer
    if isinstance(N0, int):
        #verify that the initial number of radioactive nuclei N0 is greater than 0
        if N0 > 0:
           #return the input value, which will be the initial condition for the differential equation
           return N0
        else:
           #raise an error if the input is not greater than 0
           raise ValueError('The initial number of radioactive nuclei must be greater than 0')
    else:
        #raise an error if the input is not an integer
        raise TypeError('The initial number of radioactive nuclei must be an integer')
   
