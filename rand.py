import random



def generateRan():
    files = []

    f = open('choiceOfLow.txt')

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

    hundred = random.sample(files, 1000)

    f = open("samCOL.txt", "a")

    for file in hundred:
        file = file + '\n'

        f.write(file)

    f.close()
    #print files


generateRan()