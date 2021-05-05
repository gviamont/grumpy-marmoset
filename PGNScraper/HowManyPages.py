from selenium import webdriver
from configparser import ConfigParser

# This code performs a divide and conquer algorithm to load masters pages until the 'no games' text
# appears on the page. The first page that displays the text is labeled pageNum.
# e.g. as of this writing Kasparov has 96 pages of game results so his pageNum is 97

file = 'config.ini'
config = ConfigParser()
config.read(file)
chromedriver = config['getpgns']['chromedriver']
driver = webdriver.Chrome(chromedriver)
min = int(config['howmanypages']['min'])
max = int(config['howmanypages']['max'])

def getPageNum(masterURL, pageNum, min, max):
    text = "Your search did not match any games. Please try a new search."
    url = masterURL + str(pageNum)
    driver.get(url)
    if driver.page_source.__contains__(text):
        return min, pageNum # If no games on page then we are too high, same min, lower max
    else:
        return pageNum, max # If games on page, then too low, new min, same max

# Divide and conquer
def howManyPages(masterURL,min,max):
    num = (min + max) // 2
    while max - min != 1:
        min, max = getPageNum(masterURL, num, min, max)
        num = (min + max) // 2
        print(min, max)
    return max

if __name__ == "__main__":
    masterURL = 'https://www.chess.com/games/search?fromSearchShort=1&p1=Garry%20Kasparov&page='
    pageNum = howManyPages(masterURL,min,max)
    print("No games on page number {}".format(pageNum))
