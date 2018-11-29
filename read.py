import csv
import numpy as np

# parser node

listeCoord = []

with open('instances/nodesN.csv') as csvfile:
    readcsv = csv.reader(csvfile, delimiter=';')
    lineCount = -1

    for row in readcsv:
        lineCount = lineCount + 1
        if(lineCount >= 1):
            listeCoord.append((float(row[0]), float(row[1]), row[2]))



#parser distance
with open('distancesG.csv') as csvfile:
    readcsv = csv.reader(csvfile, delimiter=';')
    matriceDistances = np.zeros((lineCount,lineCount))
    listedist = []
    for row in readcsv:
        listedist.append(row[0])
    for i in range(lineCount):
        for j in range(lineCount):
            matriceDistances[i,j] = listedist[lineCount*i+j]
            

def cout(b,c,matriceDistances):
    cout_boucle = 0
    cout_chaine = 0
    for boucle in b:
        for i in range(len(boucle)-1):
            cout_boucle += matriceDistances[boucle[i],boucle[i+1]]
        cout_boucle += matriceDistances[boucle[len(boucle)-1],boucle[0]]
    for chaine in c:
        for j in range(len(chaine)-1):
            cout_chaine += matriceDistances[chaine[j],chaine[j+1]]
    cout_reseau = cout_boucle + cout_chaine
    return cout_reseau            
