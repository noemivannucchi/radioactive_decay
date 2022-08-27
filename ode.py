from scipy.integrate import odeint

# solve ODEs
N = odeint(model,N0,t,args=(k,))