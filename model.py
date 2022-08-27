# function that returns dN/dt
def model(N,t,k):
    dNdt = -k * N
    return dNdt
