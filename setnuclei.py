def setnuclei ():
    """ set the type of radioactive nuclei and the relative decay constant k
    """
    #ask the user to choose the type of nuclei from a list
    nuclei = input('Select the type of radioactive nuclei among "Uranium238", "Plutonium239" or "Radium226": ')
    
    #set the decay constant k corresponding to the selected nucleus
    if nuclei == 'Uranium238':
        k = 5e-18
    if nuclei == 'Plutonium239':
        k = 9e-13
    if nuclei == 'Radium226':
        k = 1e-11
    return k
