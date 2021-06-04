from configparser import ConfigParser
import logging
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import json


# This code goes through Pages 1-33 of all chess masters and grabs the Names, # of games, and URLs for each master
# and adds them to a dictionary called mastersList then dumps this data into a json file
# Example: <a class="post-preview-title" href="https://www.chess.com/games/adolf-anderssen">Adolf Anderssen</a>

# Config
file = 'config.ini'
config = ConfigParser()
config.read(file)
chromeDriver = config['drivers']['chromeDriver']
mastersListStage1 = config['jsons']['mastersListStage1']
urlOGs = config['urls']['urlOGs']
urlWithPages = config['urls']['urlWithPages']
driver = webdriver.Chrome(chromeDriver)

# Create and configure logger
logger =  logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('ChessMastersList.log')
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

mastersList = {}
urlAndGames = []

# Go to url and grab (and cleanse) name, url, and number of games, create dictionary object
def gatherMastersData(url):
    count = 0
    driver.get(url)
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    for match in soup.find_all('article', class_="post-preview-component"):
        getName1 = str.rstrip(match.h2.a.text)
        getName = str.lstrip(getName1)
        getHREF = match.h2.a.get('href')
        getGames1 = str.rstrip(match.div.text)
        getGames = str.lstrip(getGames1)
        spaceLoc = getGames.index(" ")
        numOfGames = getGames[:spaceLoc]
        numOfGames = int(numOfGames.replace(',', ''))
        urlAndGames = [getHREF, numOfGames]
        mastersList[getName] = urlAndGames
        count += 1
    return count # this count is how many masters per page, so when count is 0 we know to stop

def createMastersList():
    gatherMastersData(urlOGs)
    for pageNum in range(1, 99):
        url = urlWithPages.format(pageNum)
        count = gatherMastersData(url)
        if count == 0: # Once a page with no masters exists then break out of the loop
            break
    logger.info("Successfully gathered all masters")
    logger.info(mastersList)

    a_file = open(mastersListStage1, "w")
    json.dump(mastersList, a_file)
    a_file.close()

if __name__ == "__main__":
    createMastersList()