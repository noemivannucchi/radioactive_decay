def verifynuclei (nuclei):
    """
    Parameters
    ----------
    nuclei : string
             it represents the name of the radioactive decaying nuclei 

    Description
    ----------
    This function allows to set the decay constant k (in s^-1) 
    corresponding to the type of nuclei in input

    Raises
    ------
    ValueError
        raised if the input 'nuclei' does not correspond to one of the allowed types
        of radioactive nuclei among "Uranium238", "Plutonium239" or "Radium226"
    TypeError
        raised of the input is not a string

    Returns
    -------
    It returns the float decay constant k (in s^-1) corresponding to the type of nuclei in input.
    
    """
    
    #define a dictionary to store all the decay constants for each nucleus
    nuclei_dict = {
      "Uranium238": 5e-18,
      "Plutonium239": 9e-13,
      "Radium226": 1e-11
    } 
    
    #verify that the input is a string
    if isinstance(nuclei,str):
       # check if the input is equal to 'Uranium238'
       if nuclei == 'Uranium238':
           #return the float decay constant corresponding to the selected nucleus
           return nuclei_dict.get("Uranium238")
       # check if the input is equal to 'Plutonium239'
       if nuclei == 'Plutonium239':
           #return the float decay constant corresponding to the selected nucleus
           return nuclei_dict.get("Plutonium239")
       # check if the input is equal to 'Radium226'
       if nuclei == 'Radium226':
           #return the float decay constant corresponding to the selected nucleus
           return nuclei_dict.get("Radium226")
       else:
            #raise an error if the input is not equal to one of the three allowed nuclei
            raise ValueError('Select the type of radioactive nuclei among "Uranium238", "Plutonium239" or "Radium226"')
    else:
        # raise an error if the input is not a string
        raise TypeError('The type of radioactive nuclei must be a string')
