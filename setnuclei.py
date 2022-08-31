def verifynuclei (nuclei):
    """ Verify the type of radioactive nuclei and set the relative decay constant k
    """
    #set the decay constant k corresponding to the selected nucleus
    if isinstance(nuclei,str):
       if nuclei == 'Uranium238':
           k = 5e-18
           return k
       if nuclei == 'Plutonium239':
           k = 9e-13
           return k
       if nuclei == 'Radium226':
           k = 1e-11
           return k
       else:
            raise ValueError('Select the type of radioactive nuclei among "Uranium238", "Plutonium239" or "Radium226"')
    else:
        raise TypeError('The type of radioactive nuclei must be a string')
        
