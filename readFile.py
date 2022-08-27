# time points
def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        t = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return t
