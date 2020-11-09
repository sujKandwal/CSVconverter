import csv
import os
import pandas

#Gets the CSV file via Pandas and detects the header of the columns
col_list = ["No.", 'PosX', "PosY", "PosZ", "Rx", "Ry", "Rz", "DWNx", "DWNy", "DWNz", "Lx", "Ly", "Lz"]
allCols = pandas.read_csv("rmc.csv", usecols = col_list)
#Each variable is assigned to the corresponding column list
number = allCols["No."]
posx = allCols["PosX"]
posy =  allCols["PosY"]
posz = allCols["PosZ"]
rx = allCols["Rx"]
ry = allCols["Ry"]
rz = allCols["Rz"]
dwnx = allCols["DWNx"]
dwny = allCols["DWNy"]
dwnz = allCols["DWNz"]
lx = allCols["Lx"]
ly = allCols["Ly"]
lz = allCols["Lz"]
groupSize = input("Enter your group size: ")
groupSize = int(groupSize)
def grouping(startInd, size, lisx, lisy, lisz):
    a = []
    b = []
    c = []
    group = []
    end = startInd + size
    while(startInd < end):
        a.append(lisx[startInd])
        b.append(lisy[startInd])
        c.append(lisz[startInd])
        startInd+=1
    group.append(a)
    group.append(b)
    group.append(c)
    return group
groups = int((len(number)//groupSize) + 1)
multiplier = 0
startMul = 0
counter = 0
for part in range(groups):
    counter+=1
    pathname = "Section" + (str(counter))
    adder = counter*groupSize
    if (adder > len(number)):
        diff =  adder - len(number)
        groupSize -= diff
        grouppos = grouping(startMul,groupSize, posx, posy, posz)
        groupr = grouping(startMul,groupSize, rx, ry, rz)
        groupdwn = grouping(startMul,groupSize, dwnx, dwny, dwnz)
        groupl = grouping(startMul,groupSize, lx, ly, lz)
        os.mkdir(pathname)
        os.chdir(pathname)
        textFilCenter = "Center" + str(counter) + ".txt"
        textFilDown = "Down" + str(counter) + ".txt"
        textFilRight = "Right" + str(counter) + ".txt"
        textFilLeft = "Left" + str(counter) + ".txt"
        zerogrouppos = grouppos[0]
        onegrouppos = grouppos[1]
        twogrouppos = grouppos[2]
        zerogroupr = groupr[0]
        onegroupr = groupr[1]
        twogroupr = groupr[2]
        zerogroupdwn = groupdwn[0]
        onegroupdwn = groupdwn[1]
        twogroupdwn = groupdwn[2]
        zerogroupl = groupl[0]
        onegroupl = groupl[1]
        twogroupl = groupl[2]
        with open(textFilCenter, 'w') as f:
            writer = csv.writer(f, delimiter = '\t')
            writer.writerows(zip(zerogrouppos,onegrouppos,twogrouppos))
        with open(textFilDown, 'w') as f:
            writer = csv.writer(f, delimiter = '\t')
            writer.writerows(zip(zerogroupr,onegroupr,twogroupr))
        with open(textFilRight, 'w') as f:
            writer = csv.writer(f, delimiter = '\t')
            writer.writerows(zip(zerogroupdwn,onegroupdwn,twogroupdwn))
        with open(textFilLeft, 'w') as f:
            writer = csv.writer(f, delimiter = '\t')
            writer.writerows(("X", "Y", "Z"))
            writer.writerows(zip(zerogroupl,onegroupl,twogroupl))
        os.chdir("/Users/sujaykandwal/Documents/CSVConverter")
    else:
        grouppos = grouping(startMul,groupSize, posx, posy, posz)
        groupr = grouping(startMul,groupSize, rx, ry, rz)
        groupdwn = grouping(startMul,groupSize, dwnx, dwny, dwnz)
        groupl = grouping(startMul,groupSize, lx, ly, lz)
        startMul+=37
        os.mkdir(pathname)
        os.chdir(pathname)
        textFilCenter = "Center" + str(counter) + ".txt"
        textFilDown = "Down" + str(counter) + ".txt"
        textFilRight = "Right" + str(counter) + ".txt"
        textFilLeft = "Left" + str(counter) + ".txt"
        zerogrouppos = grouppos[0]
        onegrouppos = grouppos[1]
        twogrouppos = grouppos[2]
        zerogroupr = groupr[0]
        onegroupr = groupr[1]
        twogroupr = groupr[2]
        zerogroupdwn = groupdwn[0]
        onegroupdwn = groupdwn[1]
        twogroupdwn = groupdwn[2]
        zerogroupl = groupl[0]
        onegroupl = groupl[1]
        twogroupl = groupl[2]
        with open(textFilCenter, 'w') as f:
            writer = csv.writer(f, delimiter = '\t')
            writer.writerows(zip(zerogrouppos,onegrouppos,twogrouppos))
        with open(textFilDown, 'w') as f:
            writer = csv.writer(f, delimiter = '\t')
            writer.writerows(zip(zerogroupr,onegroupr,twogroupr))
        with open(textFilRight, 'w') as f:
            writer = csv.writer(f, delimiter = '\t')
            writer.writerows(zip(zerogroupdwn,onegroupdwn,twogroupdwn))
        with open(textFilLeft, 'w') as f:
            writer = csv.writer(f, delimiter = '\t')
            writer.writerows(zip(zerogroupl,onegroupl,twogroupl))
        os.chdir("/Users/sujaykandwal/Documents/CSVConverter")