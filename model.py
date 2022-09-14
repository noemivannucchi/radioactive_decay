def model(N,t,k):  
    """
    Parameters
    ----------
    N : float
        it represents the number of remaining nuclei after a time t 
    t : float
        it represents a time value (in s)
    k : float
        it represents the positive decay constant (in s^-1)

    Description
    ----------
    This model represents an exponential decay with a decay constant k (in s^-1) and
    it is used to simulate the decay of radioactive nuclei.
 
    Raises
    ------
    ValueError
        raised if N is not positive or k is not greater than 0
    TypeError
        raised if k is not a float value

    Returns
    -------
    dNdt : float
        it returns derivative values at requested N and t values as dNdt = model(N,t,k)

    """
   
    #verify that k is a float value
    if isinstance(k, float):
          #verify that N is positive
          if N >= 0:
             #verify that k is greater than 0
             if k > 0:
               #define the ordinary differential equation (ODE) of the model
               dNdt = -k * N
               #return derivative values at requested N and t values
               return dNdt
             else:
               #raise an error if k is not positive
               raise ValueError('k value must be greater than 0')
          else:
             #raise an error if N is not positive 
             raise ValueError('N value must be positive')
    else:
        #raise an error if k is not a float value 
        raise TypeError('k value must be float')
