from compare_params import compareparams

#===========================
#UNIT TESTING 
#all the possible positive and negative combinations
#===========================

    
def test_coherency(): 
    """positive test that checks if the 'compareparams' function 
    returns 'coherent' when the expected parameters 'p0' 
    are within the uncertainty range 'stdevs' of the extracted ones (N0, k, b)
    """
    #define the variables for the input of 'compareparams' function 
    p0 = (100, 1e-11, 0.)
    N0 = 100.5
    k = 1.2e-11
    b = - 2
    stdevs = np.array([0.5,0.4,3]) 
    #check if the 'compareparams' function returns 'coherent' using the parameters defined above
    assert compareparams(p0, N0, k, b, stdevs) ==  "coherent"
    
def test_not_coherency(): 
    """positive test that checks if the 'compareparams' function 
    returns 'not coherent' when the expected parameters 'p0' 
    are not within the uncertainty range 'stdevs' of the extracted ones (N0, k, b)
    """
    #define the variables for the input of 'compareparams' function 
    p0 = (100, 1e-11, 0.)
    N0 = 100.5
    k = 1.2e-11
    b = - 2
    stdevs = np.array([0.2,0.4,3]) 
    #check if the 'compareparams' function returns 'not coherent' using the parameters defined above
    assert compareparams(p0, N0, k, b, stdevs) ==  "not coherent"   
