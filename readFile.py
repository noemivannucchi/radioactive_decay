import numpy as np

def readFile():
    """ Reads from a text file the time values to be used in the model 
    and puts them into an array t
    """
    # ask the user to insert the name of a text file with time values
    filename = input('Insert the filename with the times: ')
    
    # put the time values from the text file into an array t
    t = np.loadtxt(filename, unpack = 'True')
    return t
