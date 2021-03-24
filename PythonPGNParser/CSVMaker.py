#!/usr/bin/env python3

import csv

# Tags soured from http://www.saremba.de/chessgml/standards/pgn/pgn-complete.htm#c9.9.2
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
    'EventCategory'
]

def initializeGameMap():
    gamesListMap = {}
    for f in fieldNames:
        gamesListMap[f] = ''
    return gamesListMap

def main():
    import gamesList
    whichFile = input("Which PGN file do you want to run?\n")
    gamesList = gamesList.gamesList(whichFile)
    with open('PGNGames.csv', 'w', newline='') as f:
        theWriter = csv.DictWriter(f, fieldnames=fieldNames)
        theWriter.writeheader()
        for s in gamesList:
            theWriter.writerow(s[0])
    print("Success")

if __name__ == "__main__":
    main()

