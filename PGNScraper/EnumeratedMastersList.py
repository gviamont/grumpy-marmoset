import json
import URLConverter
from configparser import ConfigParser
import HowManyPages

# This code opens the JSON file and creates a dictionary named 'data'
# Extra code is to spit out an enumerated list of all the masters for debugging

## Maybe convert this into a function that simply returns the dictionary from the JSON file
## Maybe call HowManyPages.py function to add number of pages to each dictionary.
## Best way to add multiple values to a dictionary?
## mastersList = {"master" : [URL, numOfPages]} or maybe
## mastersList = {"master" : (URL, numOfPages)}
## May be a good reason to build this out with a class

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
        data[key].extend(numOfPages)
    return data

if __name__ == "__main__":
    data = getMasterURLs()
    dataWithPages = {}
    for key in data:
        master = key
        url = data[key]
        pages = HowManyPages.howManyPages(url, min, max)
        newValueList = [url, pages]
        dataWithPages.setdefault(master, [])
        for newValue in newValueList:
            dataWithPages[master].append(newValue)
        print(master, pages)

    for index, key in enumerate(dataWithPages):
        print(index, key, dataWithPages[key])

    b_file = open("/Users/mattmcclain/Desktop/mastersListWithPages.json", "w")
    json.dump(dataWithPages, b_file)
    b_file.close()