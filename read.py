import csv
import numpy as np

# parser node

with open('nodesG.csv') as csvfile:
    readcsv = csv.reader(csvfile, delimiter=';')
    lineCount = -1
    listeCoord = []
    for row in readcsv:
        lineCount = lineCount + 1
        if(lineCount >= 1):
            listeCoord.append(row)

#parser distance

with open('distancesG.csv') as csvfile:
    readcsv = csv.reader(csvfile, delimiter=';')
    matriceDistances = np.zeros((lineCount,lineCount))
    listedist = []
    for row in readcsv:
        listedist.append(row[0])
    print(listedist)
    for i in range(lineCount):
        for j in range(lineCount):
            matriceDistances[i,j] = listedist[1+lineCount*i+j]