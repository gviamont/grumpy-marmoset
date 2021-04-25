import glob

# Takes a directory path as an input and returns list of all pgn filenames
# in that directory and subdirectories
def filesListWithSubDirs(dirName):
    filesInSubDirectories = []
    allFilePaths = glob.glob(dirName + "/**/*.pgn", recursive=True)
    for t in allFilePaths:
        filesInSubDirectories.append(t)
    return filesInSubDirectories


# appendFiles takes the list of files from filesListWithSubDirs() and creates
# one new list of all lines from all files, like one big pgn file but in a list
def appendFiles(listOfFiles):
    eachLine = []
    for eachFile in listOfFiles:
        inputfile = open(eachFile, "r")
        if inputfile.mode == 'r':
            eachLine.extend(inputfile.readlines())
        inputfile.close()
    return eachLine

# pgnToList takes a single file and uses the readlines() function to read one line at a time into a list
def pgnLineList(fileName):
    inputfile = open(fileName, "r")
    if inputfile.mode == 'r':
        lines = inputfile.readlines()
    inputfile.close()
    return lines

if __name__ == '__main__':
    dirName = '/Users/mattmcclain/Desktop/newpgnfiles/'
    listOfFiles = filesListWithSubDirs(dirName)
    print(listOfFiles)
    allLines = appendFiles(listOfFiles, dirName)
    print(lines)
    bigGamesList = gamesList.gamesListDir(allLines)
    print(bigGamesList)