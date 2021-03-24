import CSVMaker

def gamesList(fileName):
    fileName = fileName
    inputfile = open(fileName, "r")
    if inputfile.mode == 'r':  # check to make sure that the file was opened
        lines = inputfile.readlines() # use the readlines() function to read one line at a time
        gameNum = 1 #game counter
        moves = '' #initialize moves string
        addMoves = False #initialize addMoves bool which is used as a switch to signal when we can record moves
        gamesList = [] # creating a list of tuples consisting of ({headerMap}, moves)
        # Initialize the headerMap with all fields so it can be converted to a flat file
        headerMap = CSVMaker.initializeGameMap()
        for line in lines:
            if line[0:1] == "[": #new game detected when we find first open [
                if addMoves: #after recording moves, need to flip the switch and print moves
                    addMoves = False #Flip switch now that we are in a new game
                    gameInfo = (headerMap, moves) # creating a tuple for each game
                    gamesList.append(gameInfo) #adding the gameInfo from this game to a list of games
                    moves = "" #empty moves string for next game
                    gameNum += 1
                    headerMap = CSVMaker.initializeGameMap()
                keyValue = line[1:-2] # grab info between brackets
                key = keyValue.split()[0] #assign 1st word to key
                valueIndex = keyValue.find("\"") #find first " position
                value = keyValue[valueIndex+1:-1] #grab value info between "s and store to value
                headerMap[key] = value
            elif line[0:2] == "1.": #when we come across a 1. we know to start recording moves
                addMoves = True #flip switch on to record moves
            if addMoves: #if the switch is on then append lines to moves string
                moves += str(line.rstrip()) #Append the moves together into a single string, removing trailing newlines
        gameInfo = (headerMap, moves) #last game
        gamesList.append(gameInfo) #last game

        return gamesList

    inputfile.close() # close the file when done

def main():
    thisGame = gamesList("KasparovFirst10Pages.pgn")
    for s in thisGame:
        print(s)
    print(CSVMaker.fieldNames)

if __name__ == "__main__":
    main()