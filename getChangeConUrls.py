import urllib2
import re
import time
from bs4 import BeautifulSoup
import urllib



files = []

f = open('moreChoiceOfLaw.txt')

while 1:
    file = f.readline()
    if file:
        lists = file.split(' ')

        lists = filter(lambda x: x != '\n', lists)
        lists = map(lambda x: x.replace('\n', ''), lists)
        #num += 1
        files.append(lists[0])

    else:
        break
f.close()


contracts = []
f = open('COL.txt')

while 1:
    file = f.readline()
    if file:
        lists = file.split(' ')

        lists = filter(lambda x: x != '\n', lists)
        lists = map(lambda x: x.replace('\n', ''), lists)
        #num += 1
        contracts.append(lists[0])

    else:
        break
f.close()



num= 0
for file in files:
    htmlBytes = urllib.urlopen(file).read()
    html = htmlBytes.decode("utf8")
    soup = BeautifulSoup(html, 'lxml')

    links = soup.find_all('a',href=re.compile(r"^/contracts/"))
    discard = soup.find_all('a',href=re.compile(r"^/contracts/tagged/"))
    for link in discard:
        link.extract()
    f = open("COL.txt", "a")
    for link in links:
        num +=1
        print num
        l = link.get('href')
        if l in contracts:
            print 'already in here'
        else:
            l = l + '\n'
            f.write(l)
    f.close()







def getUrls(url):

    # Reading the url and get html content
    # fp = urllib.request.urlopen(url)
    # htmlBytes = fp.read()


    htmlBytes = urllib.urlopen(url).read()
    html = htmlBytes.decode("utf8")
    soup = BeautifulSoup(html, 'lxml')
    cons = []
    contracts = soup.find_all('a',href=re.compile(r"^/contracts/"))

    links = soup.find_all('a',href=re.compile(r"^/clause/choice-of-law/_"))

    urls = []
    nextLink = soup.find('a',href=re.compile(r"^/clause/choice-of-law\?cursor"))

    nextUrl = 'https://www.lawinsider.com' + nextLink.get('href')
    for con in contracts:
        c = con.get('href')
        cons.append(c)

    for link in links:
        if link == nextLink:
            continue
        l = link.get('href')
        url = 'https://www.lawinsider.com' + l
        urls.append(url)

    return urls, nextUrl, cons


def outPutUrls(url):
    num = 0
    nextUrl = url
    while nextUrl:
        print num
        print nextUrl
        urls, nextUrl, contracts = getUrls(nextUrl)
        num += len(urls)

        f = open("moreChoiceOfLaw.txt", "a")
        for url in urls:
            link = url + '\n'
            f.write(link)
        f.close()

        f = open("COL.txt","a")

        for c in contracts:
            contract = c + '\n'
            f.write(contract)
        f.close()

outPutUrls('https://www.lawinsider.com/clause/choice-of-law')

'''

'''