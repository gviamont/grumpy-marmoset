#!/usr/bin/env python3

import csv
import sys
import gamesList
import bigPGNMaker
import os

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

# Creates a csv file from the parsed list output from gamesList
def CSVMaker(allLines, outputLoc):
    bigGamesList = gamesList.gamesList(allLines)
    with open(outputLoc + 'bigPGN.csv', 'w', newline='') as f:
        theWriter = csv.DictWriter(f, fieldnames=fieldNames)
        theWriter.writeheader()
        for s in bigGamesList:
            theWriter.writerow(s)
    print("Successfully created CSV file")

if __name__ == "__main__":
    if len(sys.argv) != 3: # In case the commandline filename entered incorrectly
        print("usage: CSVMaker.py <pgn filename or pgn file directory> <file output location>")
        sys.exit(1) # Normally returns 0 for success

    # Added logic here to check if entry in argv[1] is a file or directory
    # Also added command line input for output location in argv[2]
    elif len(sys.argv) == 3:
        cmndEntry = sys.argv[1]
        outputLoc = sys.argv[2]
        isFile = os.path.isfile(cmndEntry)
        if isFile:
            pgnFileName = cmndEntry
            allLines = bigPGNMaker.pgnLineList(pgnFileName)
            CSVMaker(allLines, outputLoc)
        else:
            pgnDirName = cmndEntry
            listOfFiles = bigPGNMaker.dirFilesList(pgnDirName)
            allLines = bigPGNMaker.dirLineList(listOfFiles)
            CSVMaker(allLines, outputLoc)

