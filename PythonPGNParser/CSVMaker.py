#!/usr/bin/env python3

import csv
import sys
import gamesList
import bigPGNMaker

# This list of tags can be updated when running into new tags in pgn files
# Most of these tags sourced from http://www.saremba.de/chessgml/standards/pgn/pgn-complete.htm#c9.9.2
fieldNames = [
    'Event',
    'Site',
    'Date',
    'Round',
    'White',
    'Black',
    'Result',
    'WhiteTitle',
    'BlackTitle',
    'WhiteElo',
    'BlackElo',
    'WhiteUSCF',
    'BlackUSCF',
    'WhiteNA',
    'BlackNA',
    'WhiteType',
    'BlackType',
    'EventDate',
    'EventSponsor',
    'Section',
    'Stage',
    'Board',
    'Opening',
    'Variation',
    'SubVariation',
    'ECO',
    'NIC',
    'Time',
    'UTCTime',
    'UTCDate',
    'TimeControl',
    'SetUp',
    'FEN',
    'Termination',
    'Annotator',
    'Mode',
    'PlyCount',
    # The ones below not included in http://www.saremba.de/chessgml/standards/pgn/pgn-complete.htm#c9.9.2
    'WhiteFideId',
    'BlackFideId',
    'EventType',
    'EventRounds',
    'EventCountry',
    'Source',
    'SourceDate',
    'WhiteTeamCountry',
    'BlackTeamCountry',
    'Remark',
    'EventCategory',
    'Source_', # This is our convention to add special keys to the map
    'Moves_'
]

# Initialize the GameMap with empty data in order to populate the csv with null data
# when values are not included for each key in the pgn file, which is usually the case
def initializeGameMap():
    gamesListMap = {}
    for f in fieldNames:
        gamesListMap[f] = ''
    return gamesListMap

# Creates a csv file from a single pgn file
def fileCSVMaker(pgnFileName):
    fileGamesList = gamesList.gamesList(pgnFileName)
    with open('singlePGNfile.csv', 'w', newline='') as f:
        theWriter = csv.DictWriter(f, fieldnames=fieldNames)
        theWriter.writeheader()
        for s in fileGamesList:
            theWriter.writerow(s)
    print("Successfully created singlePGNfile.csv from file %s"%pgnFileName)

# Creates a csv file from a directory w/ lots of files
def dirCSVMaker(pgnDirName):
    listOfFiles = bigPGNMaker.filesListWithSubDirs(pgnDirName)
    allLines = bigPGNMaker.appendFiles(listOfFiles)
    bigGamesList = gamesList.gamesListDir(allLines)
    with open('dirPGNGames.csv', 'w', newline='') as foo:
        theWriter = csv.DictWriter(foo, fieldnames=fieldNames)
        theWriter.writeheader()
        for b in bigGamesList:
            theWriter.writerow(b)
    print("Successfully created dirPGNGames.csv from dir %s"%pgnDirName)

if __name__ == "__main__":
    if len(sys.argv) != 2: # In case the commandline filename entered incorrectly
        print("usage: CSVMaker.py <pgn filename or pgn file directory>")
        sys.exit(1) # Normally returns 0 for success

    # Added logic here to check if entry is a file or directory
    if len(sys.argv) == 2:
        cmndEntry = sys.argv[1]
        if cmndEntry[0:1] == "/":
            pgnDirName = cmndEntry
            dirCSVMaker(pgnDirName)
        else:
            pgnFileName = cmndEntry
            fileCSVMaker(pgnFileName)
