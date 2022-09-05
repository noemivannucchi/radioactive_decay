def model(N,t,k):    
    """returns derivative values at requested N and t values 
    as dNdt = model(N,t,k). The model represents an exponential decay
    with a decay constant k. 
    N is the number of remaining nuclei after a time t.
    """
    #verify that k is a float value and it is greater than 0 and N is positive
    if isinstance(k, float):
          if N >= 0:
             if k > 0:
               #define the ordinary differential equation (ODE) of the model
               dNdt = -k * N
               #return derivative values at requested N and t values
               return dNdt
             #raise an error if k is not a float value and it is not greater than 0 and N is not positive
             else:
               raise ValueError('k value must be greater than 0')
          else:
             raise ValueError('N value must be positive')
    else:
        raise TypeError('k value must be float')
