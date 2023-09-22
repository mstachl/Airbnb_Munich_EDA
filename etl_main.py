from etl_util import getAirbnbUrls, extractAll


if __name__ == "__main__":
    urls = getAirbnbUrls()
    extractAll(urls)