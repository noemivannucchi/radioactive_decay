from scipy.integrate import odeint
from model import model
from readFile import readFile
from setn0 import setN0
from setnuclei import setnuclei

# solve ODEs
N = odeint(model,setN0(),readFile(),args=(setnuclei(),))
