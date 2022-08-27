# set the type of nuclei
def setnuclei ():
    nuclei = input('Select the type of radioactive nuclei among "Uranium238", "Plutonium239" or "Radium226"')
    if nuclei == 'Uranium238':
        k = 5e-18
    if nuclei == 'Plutonium239':
        k = 9e-13
    if nuclei == 'Radium226':
        k = 1e-11
    return k