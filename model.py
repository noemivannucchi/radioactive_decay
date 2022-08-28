def model(N,t,k):
    """returns derivative values at requested N and t values 
    as dNdt = model(N,t,k). The model represents an exponential decay
    with a decay constant k.
    """
    #define the ordinary differential equation (ODE) of the model
    dNdt = -k * N
    return dNdt
