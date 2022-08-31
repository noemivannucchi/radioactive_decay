import numpy as np 

def verifyFile(t):
    """ Verify the array t with the time values (in s) to be used in the model 
    """
    for elem in t:
       if isinstance(elem, float):
          if elem >= 0:
             return np.sort(t)
          else:
             raise ValueError('The time values must be positive')
       else:
          raise TypeError('The time values must be floats')
