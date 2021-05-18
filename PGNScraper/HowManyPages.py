from configparser import ConfigParser
from selenium import webdriver
import json

# This code performs a divide and conquer algorithm to load masters pages until the 'no games' text
# appears on the page. The first page that displays the text is labeled pageNum.
# e.g. as of this writing Kasparov has 96 pages of game results so his pageNum is 97

file = 'config.ini'
config = ConfigParser()
config.read(file)
chromedriver = config['drivers']['chromedriver']
driver = webdriver.Chrome(chromedriver)
min = int(config['howmanypages']['min'])
max = int(config['howmanypages']['max'])
mastersListStage2 = config['jsons']['mastersListStage2']
mastersListStage3 = config['jsons']['mastersListStage3']

# Creates a new dictionary object that adds # of pages.
def howManyPages():
    with open(mastersListStage2, "r") as json_file:
        data = json.load(json_file)

    dataWithPages = {}  # this will be new dictionary object that also includes pageNum
    for key in data:
        master = key
        url = data[key][0]
        games = data[key][1]
        pages = divideAndConquer(url, min, max)
        newValueList = [url, games, pages]
        dataWithPages[master] = newValueList
        print(master, games, pages)
    return dataWithPages


# Divide and conquer
def divideAndConquer(masterURL,min,max):
    num = (min + max) // 2
    while max - min != 1:
        min, max = getPageNum(masterURL, num, min, max)
        num = (min + max) // 2
    return max

# Updates min and max based on if the 'no games' text is found
def getPageNum(masterURL, pageNum, min, max):
    text = "Your search did not match any games. Please try a new search."
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
        print(index, key, data[key][0], data[key][1], data[key][2])
