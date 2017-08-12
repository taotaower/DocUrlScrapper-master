from scraper import extractAllProvision,cleanSubProvisions
import xlsxwriter

#provs = cleanSubProvisions(extractAllProvision('https://www.lawinsider.com/contracts/50EkUcDbOfMwYQ3lvmZj5j/tandem-diabetes-care/delaware/2013-11-04'))
#workbook = xlsxwriter.Workbook('data.xlsx')
#worksheet = workbook.add_worksheet()
#row = 0
#for p in provs:
#    col = 0
#    for i in p:
#        worksheet.write(row, col, i)
#        col+=1
#    row += 1



files = []

f = open('chaOfCon.txt')

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

num = 0

for file in files:
    file = 'https://www.lawinsider.com' + file

    filename = 'excel/' + str(num) + '-excel.xlsx'
    num +=1

    try:

        provs = cleanSubProvisions(extractAllProvision(file))
        workbook = xlsxwriter.Workbook(filename)
        worksheet = workbook.add_worksheet()
        row = 0
        for p in provs:
            col = 0
            for i in p:
                worksheet.write(row, col, i)
                col += 1
            row += 1

    except:
        print num
        print file

