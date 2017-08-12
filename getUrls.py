import urllib2
import re
import time
from bs4 import BeautifulSoup
import urllib


def getUrls(url):

    # Reading the url and get html content
    # fp = urllib.request.urlopen(url)
    # htmlBytes = fp.read()
    htmlBytes = urllib.urlopen(url).read()
    html = htmlBytes.decode("utf8")
    soup = BeautifulSoup(html, 'lxml')

    links = soup.find_all('a',href=re.compile(r"^/contracts/"))
    urls = []
    nextLink = soup.find('a',href=re.compile(r"^/contracts/tagged/delaware"))
    nextUrl = 'https://www.lawinsider.com' + nextLink.get('href')
    for link in links:
        if link == nextLink:
            continue
        l = link.get('href')
        url = 'https://www.lawinsider.com' + l
        urls.append(url)

    return urls, nextUrl



def outPutUrls(url):
    num = 0
    nextUrl = url
    while num < 10000:
        print num
        urls, nextUrl = getUrls(nextUrl)
        num += len(urls)
        f = open("urls.txt", "a")
        for url in urls:
            link = url + '\n'
            f.write(link)
        f.close()




outPutUrls('https://www.lawinsider.com/contracts/tagged/delaware')



