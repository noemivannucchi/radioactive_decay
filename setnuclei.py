def verifynuclei (nuclei):
    """
    The input 'nuclei' is a string that represents the name
    of the radioactive decaying nuclei 
    
    This function checks that the input value corresponds to one of the allowed types of radioactive nuclei
    among "Uranium238", "Plutonium239" or "Radium226"
    and return the relative float decay constant k (in s^-1)
    
    If the input 'nuclei' does not correspond to one of the allowed types, it raises a ValueError,
    while if the input is not a string, it raises a TypeError
    
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
