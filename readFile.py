import numpy as np 

def verifyFile(t):
    """checks that the elements of the input array t with the time values (in s) 
    to be used in the model are correct 
    and returns the array t with the sorted values 
    """
    #scroll all elements contained in the array t
    for elem in t:
       #verify that each element is a float value
       if isinstance(elem, float):
          #verify that each element is positive
          if elem >= 0:
             # return the array t with sorted values 
             return np.sort(t)
          else:
             #raise an error if an element is not positive 
             raise ValueError('The time values must be positive')
       else:
          #raise an error if an element is not float
          raise TypeError('The time values must be floats')
