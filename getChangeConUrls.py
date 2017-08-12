import urllib2
import re
import time
from bs4 import BeautifulSoup
import urllib


"""
The way to use this file:

For get all the urls of document that includes party name 'choiceOfLaw'

1:
  Run function 'outPutUrls' the input argument is 'https://www.lawinsider.com/clause/choice-of-law'

  in this function, you need to change two name of the output files

------- 'morechoiceOfLaw.txt' store the url that will direct to aimed urls ----
        f = open("moreChoiceOfLaw.txt", "a")
        for url in urls:
            link = url + '\n'
            f.write(link)
        f.close()

------- 'COL.txt' aimed urls ----


        f = open("COL.txt","a")

        for c in contracts:
            contract = c + '\n'
            f.write(contract)
        f.close()

2.
        Run function 'getAllUrls()'

        you also need to change the file name of the file that the function will open,

        and the result file's name

        those two files' name you need to change are same as you use in function 'outPutUrls'




------- 'morechoiceOfLaw.txt' store the url that will direct to aimed urls ----

    files = []

    f = open('moreChoiceOfLaw.txt')

    while 1:
        file = f.readline()
        if file:

------- 'COL.txt' aimed urls   the output result we need----

    contracts = []
    f = open('COL.txt')

    while 1:
        file = f.readline()
        if file:
            lists = file.split(' ')


s
"""



def getAllUrls():

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

#outPutUrls('https://www.lawinsider.com/clause/choice-of-law')

getAllUrls()
