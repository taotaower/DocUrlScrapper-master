import urllib2
import re
import time
from bs4 import BeautifulSoup
import urllib





files = []

f = open('COL.txt')

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



n = open('choiceOfLaw.txt','a')

for url in files:
    url = 'https://www.lawinsider.com' + url + '\n'
    n.write(url)

n.close()


