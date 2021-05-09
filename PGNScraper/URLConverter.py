# This code converts old URLs scraped from the website for use in crawler, for example
# From: https://www.chess.com/games/adolf-anderssen
# To: https://www.chess.com/games/search?fromSearchShort=1&p1=Adolf%20Anderssen&page=1

## Research url encoding/decoding
## Spit another error if URL doesn't work

URLStart = "https://www.chess.com/games/search?fromSearchShort=1&p1="
sep = "%20"
URLEnd = "&page="

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