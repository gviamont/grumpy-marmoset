import glob

# Takes a directory path as an input and returns list of all pgn filenames
# in that directory and subdirectories
def dirFilesList(dirName):
    allFiles = []
    allFilePaths = glob.glob(dirName + "/**/*.pgn", recursive=True)
    for t in allFilePaths:
        allFiles.append(t)
    return allFiles


# Takes the list of files from dirFilesList() and creates
# one new list of all lines from all files, like one big pgn file but in a list
def dirLineList(listOfFiles):
    eachLine = []
    for eachFile in listOfFiles:
        inputfile = open(eachFile, "r")
        if inputfile.mode == 'r':
            eachLine.extend(inputfile.readlines())
        inputfile.close()
    return eachLine


# pgnToList takes a single file and uses the readlines() function to
# read one line at a time into a list
def pgnLineList(fileName):
    eachLine = []
    inputfile = open(fileName, "r")
    if inputfile.mode == 'r':
        eachLine = inputfile.readlines()
    inputfile.close()
    return eachLine