def model(N,t,k):    
    """
    The input N is the number of remaining nuclei after a time t (in s), 
    while the input k is the decay constant (in s^-1)
    
    This model represents an exponential decay with a decay constant k (in s^-1)
    
    This function checks that k is a float value greater than 0 and that N is positive
    Then it returns derivative values at requested N and t values as dNdt = model(N,t,k)
   
    If N is not positive or k is not greater than 0, it raises a ValueError,
    while if k is not a float value, it raises  TypeError
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
