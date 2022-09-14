import numpy as np
from inter_extra_function import interextra

#===========================
#UNIT TESTING 
#all the possible positive and negative combinations
#===========================
    
def test_extrapolation(): 
    """positive test that checks if the 'interextra' function 
    returns the dictionary referred to the 'extrapolation' case 
    when the parameter 'x' is not within the minimum and the maximum values of the array 't'
    """
    #define the variables for the input of 'interextra' function 
    x = 2e11
    N0 = 100.5
    k = 1.2e-11
    b = - 2
    t = np.array([0.5,1e3,2e5]) 
    #check if the 'interextra' function returns the dictionary referred to the 'extrapolation' case 
    assert interextra(x, N0, k, b, t) ==  {'Case': 'Extrapolation', 'x': 2e11, 'N': 7.117154305585958}
    
def test_interpolation(): 
    """positive test that checks if the 'interextra' function 
    returns the dictionary referred to the 'interpolation' case 
    when the parameter 'x' is within the minimum and the maximum values of the array 't'
    """
    #define the variables for the input of 'interextra' function
    x = 2e11
    N0 = 100.5
    k = 1.2e-11
    b = - 2
    t = np.array([0.5,1e3,3e11]) 
    #check if the 'interextra' function returns the dictionary referred to the 'interpolation' case 
    assert interextra(x, N0, k, b, t) ==  {'Case': 'Interpolation', 'x': 2e11, 'N': 7.117154305585958}    
    
    
#docstring fatti bene
#github sti due files
#readme
#    foglio riassunto modifiche (dom mat magari)