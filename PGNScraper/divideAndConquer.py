from selenium import webdriver
import time
from configparser import ConfigParser

# This code will run through all masters pages until the page returns the text
# calls out that there are no more games.

# The first page that returns this is called pageNum, so the function howManyPages returns total page numbers
# ie Kasparove has games on pages 1 - 97, so howManyPages returns 97 because pageNum = 98
# Players who have no data will return 0 because page 1 will show the following text

## Update this to be a function that gets a URL and returns the number of pages
## Wait until last operation is done before moving on instead of 1 sec

file = 'config.ini'
config = ConfigParser()
config.read(file)
chromedriver = config['getpgns']['chromedriver']
driver = webdriver.Chrome(chromedriver)

def runIt(masterURL, pageNum, min, max):
    text = "Your search did not match any games. Please try a new search."
    url = masterURL + str(pageNum)
    driver.get(url)
    time.sleep(1)
    if driver.page_source.__contains__(text):
        return min, pageNum # If no games on page then we are too high, same min, lower max
    else:
        return pageNum, max # If games on page, then too low, new min, same max

def howManyPages(masterURL,min,max):
    num = (min + max) // 2
    while max - min != 1:
        min, max = runIt(masterURL, num, min, max)
        num = (min + max) // 2
        print(min, max)
    print("Yes, the pageNum is", max)
    return max

if __name__ == "__main__":
    min = 0
    max = 100
    masterURL = 'https://www.chess.com/games/search?fromSearchShort=1&p1=Garry%20Kasparov&page='
    pageNum = howManyPages(masterURL,min,max)
    print("No games on page number {}".format(pageNum))
