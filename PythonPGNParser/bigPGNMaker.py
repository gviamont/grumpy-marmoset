import os
import gamesList
from pathlib import Path

# filesList takes a directory as an input and returns list of all pgn filenames in that directory
def filesList(dirName):
    ## Add os function to get full path
    ## add check if file or directory, can use recursion to hit filesList again, use extend
    ## base case is in directory with no sub directories
    filesInDirectory = os.listdir(dirName)
    for entry in filesInDirectory:
        if entry[-3:] != 'pgn':
            filesInDirectory.remove(entry)
    return filesInDirectory

# appendFiles takes the list of files from filesList() and creates one list of all lines from all files
def appendFiles(listOfFiles, dirName):
    eachLine = []
    for eachFile in listOfFiles:
        inputfile = open(dirName + eachFile, "r")
        if inputfile.mode == 'r':
            eachLine.extend(inputfile.readlines())
        inputfile.close()
    return eachLine

# # Not sure where we were going with this
# def getAllPGNLines(dirName):
#     listOfFiles = filesList(dirName)
#     listOfFilesWithPaths = []
#     for f in listOfFiles:
#         listOfFilesWithPaths.append(dirName + f)
#     return appendFiles(listOfFilesWithPaths)

if __name__ == '__main__':
    ## Add sys.argv
    dirName = '/Users/mattmcclain/Desktop/pgnfiles/'
    listOfFiles = filesList(dirName)
    # print(listOfFiles)
    allLines = appendFiles(listOfFiles, dirName)
    # print(lines)
    # bigPGNMaker(allLines) # No longer needed due to gamesListDir()
    bigGamesList = gamesList.gamesListDir(allLines)
    # print(bigGamesList)

