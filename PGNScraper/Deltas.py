import json
import ast

if __name__ == "__main__":
    ChessMastersList = '/Users/mattmcclain/Coding/grumpy-marmoset/PGNScraper/ChessMastersList.log'
    with open(ChessMastersList) as f:
        lastEntry = f.readlines()[-1]
    firstChar = lastEntry.index('{')
    data2 = lastEntry[firstChar:]
    data = str.lstrip(str.rstrip(data2))
    dataStr = "'" + data + "'"
    print(newdata)

