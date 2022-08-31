def verifyN0 (N0):
    """ verify the initial condition
        of the differential states 
    """
    # verify that the initial number of radioactive nuclei is an integer
    if isinstance(N0, int):
        if N0 > 0:
           return N0
        else:
           raise ValueError('The initial number of radioactive nuclei must be greater than 0')
    else:
        raise TypeError('The initial number of radioactive nuclei must be an integer')
   
