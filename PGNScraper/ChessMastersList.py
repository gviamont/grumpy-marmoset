from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests
import json

# This code goes through Pages 1-33 of all chess masters and grabs the Names and HREFs for each master
# and adds them to a dictionary called mastersList then dumps this data into a json file
# Example: <a class="post-preview-title" href="https://www.chess.com/games/adolf-anderssen">Adolf Anderssen</a>

## One and done, not sure if anything needs to be worked further, unless a dictionary isn't the
## best way to handle this data
if __name__ == "__main__":
    mastersList = {}
    driver = webdriver.Chrome('/Users/mattmcclain/Downloads/chromedriver4')
    for pageNum in range(1, 34):
        url = "https://www.chess.com/games?page={}".format(pageNum)
        driver.get(url)
        time.sleep(4)
        source = requests.get(url).text
        soup = BeautifulSoup(source, 'lxml')
        for match in soup.find_all('a', class_="post-preview-title"):
            getName1 = str.rstrip(match.text)
            getName = str.lstrip(getName1)
            getHREF = match.get('href')
            mastersList[getName] = getHREF
    print(mastersList)
    a_file = open("/Users/mattmcclain/Desktop/mastersList.json", "w")
    json.dump(mastersList, a_file)
    a_file.close()
