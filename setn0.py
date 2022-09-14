def verifyN0 (N0):
    """
    Parameters
    ----------
    N0 : int
         it represents the initial number of radioactive nuclei
         and it is the initial condition of the differential states.

    Description
    ----------
    This function checks that the input value 'N0' is an integer greater than 0
    and it returns the same value.       

    Raises
    ------
    ValueError
        raised if 'N0' is not greater than 0.
    TypeError
        raised if 'N0' is not an integer.

    Returns
    -------
    N0 : int
         it represents the initial number of radioactive nuclei
         and it is the initial condition of the differential states.

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
   
