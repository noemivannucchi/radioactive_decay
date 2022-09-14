import numpy as np 

def verifyFile(t):
    """
    Parameters
    ----------
    t : numpy.aray
        it contains the time values (in s) to be used in the model

    Description
    ----------
    This function checks the type and the values of the elements 
    of the input array 't'. Then, it removes duplicated values from the input array 't' and 
    it creates a new array 'newt' with non duplicated values.
    Finally, it returns the array 'newt' with sorted values.
    
    Raises
    ------
    ValueError
        raised if the input array 't' is empty or 
        if the elements of the array 'newt' are not positive
    TypeError
        raised if the elements of the array 'newt' are not floats or not a number

    Returns
    -------
    it returns the array 'newt' with sorted and non duplicated values.

    """
    
    #verify that the array is not empty
    if len(t) == 0:
        raise ValueError('The input array is empty')
    
    #convert the input array into a list1
    list1 = t.tolist()
    #remove duplicated values from the list1 
    list2 = list(set(list1))
    #convert the list2 into an other array 'newt'
    newt = np.array(list2)   
    
    #scroll all elements contained in the array t
    for elem in newt:
      #verify that each element is a float value
      if not isinstance(elem, float):
         #raise an error if an element is not float
         raise TypeError('The time values must be floats')
      #verify that each element is positive
      if elem < 0:   
         #raise an error if an element is not positive 
         raise ValueError('The time values must be positive')
      #verify that all the elements are numbers
      if np.isnan(elem):  
         #raise an error if an element is not positive 
         raise TypeError('One element is not a number')
             
    # return the array t with sorted values 
    return np.sort(newt)
