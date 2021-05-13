import csv

def calc_point(r, num):
    point = 0
    if line[r][num] == 'ハイ':
        point = 4

    if line[r][num] == 'どちらかといえばハイ':
        point = 3

    if line[r][num] == 'どちらかといえばイイエ':
        point = 1

    if line[r][num] == 'イイエ':
        point = 0
        
    return point

with open ( 'FFS理論簡易分析.csv', 'r' ) as f :
    reader = csv.reader(f)
    line = [row for row in reader]
    num = 16
    ffsA = 0
    ffsB = 0
    ffsC = 0
    ffsD = 0
    ffsE = 0
    ffsS = 0
    listA = [4, 8, 12, 15, 17]
    listB = [5, 19, 21, 27, 30]
    listC = [6, 11, 16, 18, 29]
    listD = [14, 20, 22, 23, 26]
    listE = [2, 7, 10, 24, 25]
    listS = [1, 3, 9, 13, 28]

    for r in range(1, 3):
        num = 16
        ffsA, ffsB, ffsC, ffsD, ffsE, ffsS = 0, 0, 0, 0, 0, 0
        for c in range(30):
            print(line[r][num])

            if c+1 in listA:
                ffsA += calc_point(r, num)

            if c+1 in listB:
                ffsB += calc_point(r,num)

            if c+1 in listC:
                ffsC += calc_point(r,num)    

            if c+1 in listD:
                ffsD += calc_point(r,num)

            if c+1 in listE:
                ffsE += calc_point(r,num)

            if c+1 in listS:
                ffsS += calc_point(r,num)
            num += 3
        print(line[r][4] + 'のポイントはA:{0}，B:{1}，C:{2}，D:{3}，E:{4}，S:{5}です'.format(ffsA, ffsB, ffsC, ffsD, ffsE, ffsS))

    print('finish')