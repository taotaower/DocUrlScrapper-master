
'''
import random


def generateRan():
    files = []

    f = open('urls.txt')
    num = 0
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

    hundred = random.sample(files, 100)

    f = open("hundredUrls.txt", "a")

    for file in hundred:
        file = file + '\n'

        f.write(file)

    f.close()

    print hundred
    #print files

'''