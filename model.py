def model(N,t,k):
    """returns derivative values at requested N and t values 
    as dNdt = model(N,t,k). The model represents an exponential decay
    with a decay constant k.
    """
    #define the ordinary differential equation (ODE) of the model
    if isinstance(k, float):
          if N >= 0:
             if k > 0:
               dNdt = -k * N
               return dNdt
             else:
               raise ValueError('k value must be greater than 0')
          else:
             raise ValueError('N value must be positive')
    else:
        raise TypeError('k value must be float')
