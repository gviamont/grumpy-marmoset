from configparser import ConfigParser
from selenium import webdriver
import json

# This code converts old URLs scraped from the website for use in crawler, for example
# From: https://www.chess.com/games/adolf-anderssen
# To: https://www.chess.com/games/search?fromSearchShort=1&p1=Adolf%20Anderssen&page=1

## Research url encoding/decoding
## Add error logging

file = 'config.ini'
config = ConfigParser()
config.read(file)
chromedriver = config['drivers']['chromedriver']
driver = webdriver.Chrome(chromedriver)
mastersListStage1 = config['jsons']['mastersListStage1']
mastersListStage2 = config['jsons']['mastersListStage2']

URLStart = "https://www.chess.com/games/search?fromSearchShort=1&p1="
sep = "%20"
URLEnd = "&page="

def getUpdatedURLs():
    # Opens the mastersListStage1.json file and loads it into a dictionary called 'data'
    text = "Your search did not match any games. Please try a new search."

    with open(mastersListStage1, "r") as json_file:
        data = json.load(json_file)

    # Updates the urls using the URLConverter
    for key in data:
        oldURL = data[key][0]
        data[key][0] = URLConverter(data[key][0])
        newURL = data[key][0]
        driver.get(newURL)
        if driver.page_source.__contains__(text) and data[key][1] != 0:
            print("This URL is not working:", newURL, "Old:", oldURL) # Add a logging statement here or maybe a new function to testURLs
    return data

def URLConverter(oldURL):
    # oldURL = "https://www.chess.com/games/david-anton-guijarro"

    name = oldURL[28:]
    splitName = name.split('-')
    nameLen = len(splitName)
    newURL = ''

    # There are 10 players whose names didn't run through this URLConverter correctly
    # so this is the manual correction of those urls
    if oldURL == 'https://www.chess.com/games/bogdan-daniel-deac': return 'https://www.chess.com/games/search?fromSearchShort=1&p1=Bogdan-Daniel%20Deac&page='
    elif oldURL == 'https://www.chess.com/games/david-wl-howell' : return 'https://www.chess.com/games/search?fromSearchShort=1&p1=David%20W%20L%20Howell&page='
    elif oldURL == 'https://www.chess.com/games/francois-philidor' : return 'https://www.chess.com/games/search?fromSearchShort=1&p1=Francois-Andre%20Danican%20Philidor&page='
    elif oldURL == 'https://www.chess.com/games/jan-krzysztof-duda' : return 'https://www.chess.com/games/search?fromSearchShort=1&p1=Jan-Krzysztof%20Duda&page='
    elif oldURL == 'https://www.chess.com/games/liviu-dieter-nisipeanu' : return 'https://www.chess.com/games/search?fromSearchShort=1&p1=Liviu-Dieter%20Nisipeanu&page='
    elif oldURL == 'https://www.chess.com/games/louis-charles-mahe-de-la-bourdonnais' : return 'https://www.chess.com/games/search?fromSearchShort=1&p1=Louis-Charles%20Mahe%20de%20La%20Bourdonnais&page='
    elif oldURL == 'https://www.chess.com/games/maxime-vachier-lagrave' : return 'https://www.chess.com/games/search?fromSearchShort=1&p1=Maxime%20Vachier-Lagrave&page='
    elif oldURL == 'https://www.chess.com/games/pierre-de-saint-amant' : return 'https://www.chess.com/games/search?fromSearchShort=1&p1=Pierre%20de%20Saint-Amant&page='
    elif oldURL == 'https://www.chess.com/games/sabina-francesca-foisor' : return 'https://www.chess.com/games/search?fromSearchShort=1&p1=Sabina-Francesca%20Foisor&page='
    elif oldURL == 'https://www.chess.com/games/zhu-jiner' : return 'https://www.chess.com/games/search?fromSearchShort=1&p1=Zhu%20Jin%27er&page='
    elif oldURL == 'https://www.chess.com/games/alexander-ilyin-genevsky' : return 'https://www.chess.com/games/search?fromSearchShort=1&p1=Alexander%20Ilyin-Genevsky&page='
    elif oldURL == 'https://www.chess.com/games/donaldson-a-elena' : return 'https://www.chess.com/games/search?fromSearchShort=1&p1=Donaldson-A%20Elena&page='
    elif oldURL == 'https://www.chess.com/games/efim-bogoljubow' : return 'https://www.chess.com/games/search?fromSearchShort=1&p1=Efim%20Bogoljubov&page='
    elif oldURL == 'https://www.chess.com/games/harry-pillsbury' : return 'https://www.chess.com/games/search?fromSearchShort=1&p1=Harry%20Nelson%20Pillsbury&page='
    elif oldURL == 'https://www.chess.com/games/jan-timman' : return 'https://www.chess.com/games/search?fromSearchShort=1&p1=Jan%20H%20Timman&page='
    elif oldURL == 'https://www.chess.com/games/matthew-sadler' : return 'https://www.chess.com/games/search?fromSearchShort=1&p1=Matthew%20D%20Sadler&page='
    elif oldURL == 'https://www.chess.com/games/sultan-khan-mir' : return 'https://www.chess.com/games/search?fromSearchShort=1&p1=Mir%20Sultan%20Khan&page='
    elif oldURL == 'https://www.chess.com/games/nigel-short' : return 'https://www.chess.com/games/search?fromSearchShort=1&p1=Nigel%20D%20Short&page='
    elif oldURL == 'https://www.chess.com/games/abasov-nijat-azad' : return 'https://www.chess.com/games/search?fromSearchShort=1&p1=Nijat%20Abasov&page='
    elif oldURL == 'https://www.chess.com/games/maghsoodloo-parham' : return 'https://www.chess.com/games/search?fromSearchShort=1&p1=Parham%20Maghsoodloo&page='
    elif oldURL == 'https://www.chess.com/games/sam-shankland' : return 'https://www.chess.com/games/search?fromSearchShort=1&p1=Samuel%20Shankland&page='
    elif oldURL == 'https://www.chess.com/games/vidit-santosh-gujrathi' : return 'https://www.chess.com/games/search?fromSearchShort=1&p1=Santosh%20Gujrathi%20Vidit&page='
    elif oldURL == 'https://www.chess.com/games/hoang-thanh-trang' : return 'https://www.chess.com/games/search?fromSearchShort=1&p1=Thanh%20Trang%20Hoang&page='

    # Here is the URLConverter logic which is based on the old URL that is passed in due to the
    # ChessMastersList.py scraper logic which pulls the href out of each page for each player
    elif nameLen == 1:
        newURL = URLStart + splitName[0] + URLEnd
    elif nameLen == 2:
        newURL = URLStart + splitName[0] + sep + splitName [1] + URLEnd
    elif nameLen == 3:
        newURL = URLStart + splitName[0] + sep + splitName[1] + sep + splitName[2] + URLEnd
    elif nameLen == 4:
        newURL = URLStart + splitName[0] + sep + splitName[1] + sep + splitName[2] + sep + splitName[3] + URLEnd
    else:
        print("At lease one in the list has too many forking names")
    return newURL

if __name__ == "__main__":
    data = getUpdatedURLs()  # creates dictionary object with updated URLs

    a_file = open(mastersListStage2, "w")
    json.dump(data, a_file)
    a_file.close()

    print("Success")

    # This prints the results in a nice to view format
    # for index, key in enumerate(data):
    #     print(index, key, data[key][0],data[key][1])
