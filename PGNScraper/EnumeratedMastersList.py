import json
import URLConverter
from configparser import ConfigParser
import HowManyPages

# This code opens the JSON file and creates a dictionary named 'data'
# Extra code is to print enumerated list of all the masters for debugging

## May be interesting to build this out with a class instead of a dictionary
## Specify the config file on the command line
## Specify the json file location on the command line

file = 'config.ini'
config = ConfigParser()
config.read(file)
mastersListLoc = config['enumeratedmasterslist']['mastersListLoc']
min = int(config['howmanypages']['min'])
max = int(config['howmanypages']['max'])

def getMasterURLs():
    # Opens the mastersList.json file and loads it into a dictionary called 'data'
    with open(mastersListLoc, "r") as json_file:
        data = json.load(json_file)

    # Updates the urls using the URLConverter
    for key in data:
        data[key] = URLConverter.URLConverter(data[key])
    return data

def addHowManyPages(data, key, numOfPages):
    if key not in data:
        print("Master not in the list")
    else:
        data[key].extend(numOfPages) #I think append might be the more appropriate choice here
    return data

if __name__ == "__main__":
    data = getMasterURLs() #creates dictionary object with only Masters & URLs
    dataWithPages = {} #this will be new dictionary object that also includes pageNum
    for key in data:
        master = key
        url = data[key]
        pages = HowManyPages.howManyPages(url, min, max)
        newValueList = (url, pages)
        # dataWithPages.setdefault(master, []) # wasn't able to figure out how to create tuple value pair instead of list value pair
        dataWithPages[master] = newValueList
        # for newValue in newValueList:
        #     dataWithPages[master].append(newValue)
        print(master, pages)

    # This prints the results in a nice to view format
    for index, key in enumerate(dataWithPages):
        print(index, key, dataWithPages[key])

    b_file = open("/Users/mattmcclain/Desktop/mastersListWithPages.json", "w")
    json.dump(dataWithPages, b_file)
    b_file.close()