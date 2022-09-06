def verifynuclei (nuclei):
    """checks that the string input value corresponds to one of the allowed types of radioactive nuclei
    and set the relative float decay constant k (in s^-1)
    """
    #verify that the input is a string
    if isinstance(nuclei,str):
       # check if the input is equal to 'Uranium238'
       if nuclei == 'Uranium238':
           #set the decay constant k (in s^-1) corresponding to the selected nucleus
           k = 5e-18 
           #return the float decay constant corresponding to the selected nucleus
           return k
       # check if the input is equal to 'Plutonium239'
       if nuclei == 'Plutonium239':
           #set the decay constant k (in s^-1) corresponding to the selected nucleus
           k = 9e-13
           #return the float decay constant corresponding to the selected nucleus
           return k
       # check if the input is equal to 'Radium226'
       if nuclei == 'Radium226':
           #set the decay constant k (in s^-1) corresponding to the selected nucleus
           k = 1e-11
           #return the float decay constant corresponding to the selected nucleus
           return k
       else:
            #raise an error if the input is not equal to one of the three allowed nuclei
            raise ValueError('Select the type of radioactive nuclei among "Uranium238", "Plutonium239" or "Radium226"')
    else:
        # raise an error if the input is not a string
        raise TypeError('The type of radioactive nuclei must be a string')
        
