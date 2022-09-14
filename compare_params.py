def compareparams(p0, N0, k, b, stdevs):
    """
    Parameters
    ----------
    p0 : tuple
         p0 = (N0_i, k_i, b_i) contains the initial parameters for the fitting function near those expected.
    N0 : float
        parameter extracted from the fit. It represents the initial number of decaying nuclei.
    k : float
        parameter extracted from the fit. It represents the decay constant.
    b : float
        parameter extracted from the fit. It represents a shift in the exponential fitting function.
    stdevs : numpy.array
        it contains the standard deviations related to the parameters (N0, k, b) extracted from the fit
   
    Description
    ----------
    This function checks that the parameters extracted from the fit 
    are consistent with those expected within the uncertainty given by the standard deviation
    
    Returns
    -------
    If the expected parameters are within the uncertainty range of the extracted ones, 
    it is printed that the extracted parameters are coherent with the expected ones.
    Otherwise, it is printed that more points are needed to better estimate the parameters N0, k, b.

    """
    # check if the expected parameters contained in the tuple 'p0' 
    # are within the uncertainty range of the extracted ones from the fit (N0, k, b)
    if N0 - stdevs[0] < p0[0] < N0 + stdevs[0] \
       and k - stdevs[1] < p0[1] < k + stdevs[1] \
           and b - stdevs[2] < p0[2] < b + stdevs[2]:
               # if the expected parameters are within the uncertainty range of the extracted ones,
               # print that the extracted parameters are coherent with the expected ones
               print ("The parameters extracted from the fit are coherent with the expected ones")
    else:
        # otherwise, print that more points are needed to better estimate the parameters N0, k, b
        print ("The parameters extracted from the fit are not all coherent with the expected ones. \
               Therefore, more points are needed to better estimate the parameters N0, k, b ")           