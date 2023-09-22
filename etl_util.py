import requests
from bs4 import BeautifulSoup

def getAirbnbUrls():
    urls = []
    baseAirbnbUrl = 'http://insideairbnb.com/get-the-data'
    response = requests.get(baseAirbnbUrl)

    # Obtain Airbnb's information
    soup = BeautifulSoup(response.text, 'lxml')
    # Find table containing Munich urls
    munichTable = soup.find('table', {'class': 'munich'})

    for row in munichTable.tbody.findAll('tr'):
        cells = row.findAll('td')
        if '.gz' not in str(cells[1]):
            urls.append(cells[1].findAll('a', href=True)[0].get('href'))
    print(urls)
    return urls
    

def extract(url: str, saveTo: str):
    print("Extract file from {}".format(url))
    response = requests.get(url)
    open(saveTo, 'wb').write(response.content)
    print("Safed to file {}".format(url, saveTo))

def extractAll(urls: []):
    for url in urls:
        filename_orig = url.split('/')[-1].split('.')
        saveTo = "imported/{}_downloaded{}".format(filename_orig[0], filename_orig[-1])
        extract(url, saveTo)
