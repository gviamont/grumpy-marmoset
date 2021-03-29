#!/usr/bin/env python3

import csv
import sys

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
    'Moves'
]

# Initialize the GameMap with empty data in order to populate the csv with null data
# when values are not included for each key in the pgn file, which is usually the case
def initializeGameMap():
    gamesListMap = {}
    for f in fieldNames:
        gamesListMap[f] = ''
    return gamesListMap

if __name__ == "__main__":
    import gamesList
    pgnFileName = sys.argv[1]
    gamesList = gamesList.gamesList(pgnFileName)
    with open('PGNGames.csv', 'w', newline='') as f:
        theWriter = csv.DictWriter(f, fieldnames=fieldNames)
        theWriter.writeheader()
        for s in gamesList:
            theWriter.writerow(s)
    print("Success")

