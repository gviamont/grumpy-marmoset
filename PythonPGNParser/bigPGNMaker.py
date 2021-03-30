import os
from pathlib import Path

# filesList takes a directory as an input and returns list of all pgn filenames in that directory
def filesList(dirName):
    filesInDirectory = os.listdir(dirName)
    for entry in filesInDirectory:
        if entry[-3:] != 'pgn':
            filesInDirectory.remove(entry)
    return filesInDirectory

# appendFiles takes the list of files from filesList() and creates a bigPGNFile.pgn file
def appendFiles(listOfFiles, dirName):
    clearOutput = open("bigPGNFile.pgn", "r+")
    clearOutput.truncate(0) # Since we are appending to this file, this clears it first
    clearOutput.close()
    dataFolder = Path(dirName)
    outputFile = open("bigPGNFile.pgn", "a")
    for eachFile in listOfFiles:
        fileToOpen = dataFolder / eachFile
        inputFile = open(fileToOpen, "r")
        if inputFile.mode == 'r':
            lines = inputFile.readlines()
            for l in lines:
                outputFile.write(l)
        outputFile.write('\n\n')
        inputFile.close()
    outputFile.close()

if __name__ == '__main__':
    dirName = '/Users/mattmcclain/Desktop/pgnfiles/'
    listOfFiles = filesList(dirName)
    print(listOfFiles)
    appendFiles(listOfFiles, dirName)

