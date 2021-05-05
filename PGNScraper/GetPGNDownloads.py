from selenium import webdriver
import time
from configparser import ConfigParser

# This code crawls through a masters pages and downloads the pgns a page at a time

## Update the range to include how many pages that master has from HowManyPages.py. Great candidate for config file.
## Update the url as an input from URLs returned in URLConverter

# Config
file = 'config.ini'
config = ConfigParser()
config.read(file)
outputDir = config['getpgns']['outputDir']
chromedriver = config['getpgns']['chromedriver']

# Loads the chromedriver location then updates the Chrome download output directory
chromeOptions = webdriver.ChromeOptions()
prefs = {"profile.default_content_settings.popups": 0,
             "download.default_directory": outputDir,
             "directory_upgrade": True}
chromeOptions.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(executable_path=chromedriver, options=chromeOptions)

# Takes each masterURL and 'how many pages' each has then visits each page, checks the check-all box
# then downloads them into the directory in the config.ini
def downloadPGNs(masterURL, howManyPages):
    for pageNum in range(1, howManyPages+1):
        url = masterURL + str(pageNum)
        driver.get(url)
        time.sleep(2)
        driver.find_element_by_class_name("master-games-check-all").click()
        # time.sleep(2)
        driver.find_element_by_class_name("master-games-download-button").click()
        # time.sleep(4)

if __name__ == "__main__":
    masterURL = "https://www.chess.com/games/search?fromSearchShort=1&p1=Garry%20Kasparov&page="
    howManyPages = 2
    downloadPGNs(masterURL, howManyPages)
