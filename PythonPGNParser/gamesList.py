import CSVMaker

# https://spin.atomicobj ect.com/2016/04/19/vim-commands-cheat-sheet/

# This function uses readlines() to read in one line at a time then builds
# a map of data from each game and returns a list of all games and associated
# pgn header info (aka tags) plus moves.
def gamesList(fileName):
    fileName = fileName
    inputfile = open(fileName, "r")

    # use the readlines() function to read one line at a time
    if inputfile.mode == 'r':
        lines = inputfile.readlines()

        # Initialize a gamesList that includes a dictionary of Header items and add Moves to it
        # addMoves is used to initialize addMoves bool which is used as a switch to signal when we can record moves
        # Initialize the headerMap with all fields so it can be converted to a flat file
        gamesList = []
        moves = ''
        addMoves = False
        headerMap = CSVMaker.initializeGameMap()

        # Read in a line at a time and detect new games based "["
        for line in lines:
            if line[0:1] == "[":

                # We run this if condition after we finish reading in the moves
                # Record moves and append all data to gamesList, then empty moves string and reinitialize GameMap
                if addMoves:
                    addMoves = False
                    headerMap["Moves"] = moves
                    gamesList.append(headerMap)
                    moves = ''
                    headerMap = CSVMaker.initializeGameMap()

                # To build headerMap, isolate the info between the brackets and assign the 1st word to 'key'
                # then find the first " position and isolate the data between the double quotes and store to 'value'
                keyValue = line[1:-2]
                key = keyValue.split()[0]
                valueIndex = keyValue.find("\"")
                value = keyValue[valueIndex+1:-1]
                headerMap[key] = value

            # When we come across the first move we flip the addMoves switch and begin recording moves
            # Append the lines until we come across another "[" which tells us we are in a new game
            # The rstrip() removes trailing new lines
            elif line[0:2] == "1.":
                addMoves = True
            if addMoves:
                moves += str(line.rstrip())
        # Last game info
        headerMap["Moves"] = moves
        gamesList.append(headerMap)

        return gamesList

    inputfile.close()

if __name__ == "__main__":
    # pgnFileName = sys.argv[1]
    pgnFileName = "k10.pgn"
    thisGame = gamesList(pgnFileName)
    for s in thisGame:
        print(s)