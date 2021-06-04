from configparser import ConfigParser
import logging
from selenium import webdriver
import time
import json


# This code crawls through a masters pages and downloads the pgns a page at a time

# Config
file = 'config.ini'
config = ConfigParser()
config.read(file)
outputDir = config['outputdirectories']['PGNOutputDir']
chromeDriver = config['drivers']['chromeDriver']
mastersListStage3 = config['jsons']['mastersListStage3']

# Loads the chromeDriver location then updates the Chrome download output directory
chromeOptions = webdriver.ChromeOptions()
prefs = {"profile.default_content_settings.popups": 0,
             "download.default_directory": outputDir,
             "directory_upgrade": True}
chromeOptions.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(executable_path=chromeDriver, options=chromeOptions)

# Create and configure logger
logger =  logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('GetPGNDownloads.log')
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

text = "Your search did not match any games. Please try a new search."

# Takes each masterURL and then visits each page, checks the check-all box
# then downloads them into the directory in the config.ini
def downloadAllPGNs(masterURL):
    for pageNum in range(1, 999):
        url = masterURL + str(pageNum)
        driver.get(url)
        time.sleep(2)
        if driver.page_source.__contains__(text):
            break
        else:
            driver.find_element_by_class_name("master-games-check-all").click()
            driver.find_element_by_class_name("master-games-download-button").click()

if __name__ == "__main__":
    masterURL = "https://www.chess.com/games/search?fromSearchShort=1&p1=alexander%20mcdonnell&page="
    downloadAllPGNs(masterURL)
    #
    # with open(mastersListStage3, "r") as json_file:
    #     data = json.load(json_file)
    # logger.info("json file loaded")
    # logger.info(data)
    #
    # numOfMasters = len(data)
    # print("Total number of Masters is", numOfMasters)
    # logger.info("Total number of Masters is", numOfMasters) # Number of Masters
    #
    # x = 0
    # for key in data:
    #     if x < 1:
    #         masterURL = data[key][0]
    #         howManyPages = data[key][2]
    #         logger.info(key, howManyPages)
    #         downloadAllPGNs(masterURL, howManyPages)
    #         x += 1
    #     else:
    #         break
