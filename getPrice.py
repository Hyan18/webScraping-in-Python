import bs4, requests

def getEbayPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#prcIsum')
    return elems[0].text


price = getEbayPrice('https://www.ebay.co.uk/itm/Automate-the-Boring-Stuff-With-Python-Practical-Programming-for-Total-Begin/382762277817')
print('The price is ' + price)
