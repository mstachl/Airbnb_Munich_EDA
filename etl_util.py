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
    print("Found urls: {}".format(urls))
    return urls
    

def extract(url: str, saveTo: str):
    print("Extract file from {}".format(url))
    response = requests.get(url)
    open(saveTo, 'wb').write(response.content)
    print("Safed to file {}".format(saveTo))

def extractAll(urls: []):
    for url in urls:
        filename_orig = url.split('/')[-1]
        filename, extension = filename_orig.split('.')
        saveTo = "latest_download/{}_latest{}".format(filename, ".{}".format(extension))
        extract(url, saveTo)

if __name__ == '__main__':
    urls = getAirbnbUrls()
    extractAll(urls)
