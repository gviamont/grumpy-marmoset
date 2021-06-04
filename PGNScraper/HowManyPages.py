from configparser import ConfigParser
import logging
from selenium import webdriver
import json


# This code performs a divide and conquer algorithm to load masters pages until the 'no games' text
# appears on the page. The first page that displays the text is labeled pageNum.
# e.g. as of this writing Kasparov has 96 pages of game results so his pageNum is 97

# Config
file = 'config.ini'
config = ConfigParser()
config.read(file)
chromeDriver = config['drivers']['chromeDriver']
driver = webdriver.Chrome(chromeDriver)
min = int(config['howmanypages']['min'])
max = int(config['howmanypages']['max'])
firstPageCheck = int(config['howmanypages']['firstCheck'])
mastersListStage2 = config['jsons']['mastersListStage2']
mastersListStage3 = config['jsons']['mastersListStage3']

# Create and configure logger
logger =  logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('HowManyPages.log')
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

text = "Your search did not match any games. Please try a new search."

# Creates a new dictionary object that adds # of pages.
def howManyPages():
    with open(mastersListStage2, "r") as json_file:
        data = json.load(json_file)

    dataWithPages = {}  # this will be new dictionary object that also includes pageNum
    for key in data:
        master = key
        url = data[key][0]
        games = data[key][1]
        pages = firstCheck(url, 0, firstPageCheck)
        print(master, "has", pages, "pages")
        newValueList = [url, games, pages]
        dataWithPages[master] = newValueList
        logger.info(master, games, pages)
    return dataWithPages

def firstCheck(url, min, pageCheck):
    divConq = False
    multConq = False
    finalMax = 0
    newurl = url + str(pageCheck)
    driver.get(newurl)
    if driver.page_source.__contains__(text):
        divConq = True
    else:
        multConq = True
    if multConq == True:
        max = multiplyAndConquer(pageCheck)
        min = max // 2
        print("mult max", max)
        firstCheck(url, min, max)
    elif divConq == True:
        finalMax = divideAndConquer(url, min, pageCheck)
        print("final max", finalMax)
    print("final2 max", finalMax)
    return finalMax

# Divide and conquer
def divideAndConquer(masterURL,min,max):
    num = (min + max) // 2
    while max - min != 1:
        min, max = getPageNum(masterURL, num, min, max)
        num = (min + max) // 2
    return max

def multiplyAndConquer(min):
    num = min * 2
    return num

# Updates min and max based on if the 'no games' text is found
def getPageNum(masterURL, pageNum, min, max):
    url = masterURL + str(pageNum)
    driver.get(url)
    if driver.page_source.__contains__(text):
        return min, pageNum # If no games on page then we are too high, same min, lower max
    else:
        return pageNum, max # If games on page, then too low, new min, same max


if __name__ == "__main__":
    data = howManyPages()  # creates dictionary object with updated URLs

    a_file = open(mastersListStage3, "w")
    json.dump(data, a_file)
    a_file.close()

    # This prints the results in a nice to view format
    for index, key in enumerate(data):
        logger.info(index, key, data[key][0], data[key][1], data[key][2])

