import csv
import numpy as np

# parser node

listeCoord = []

with open('instances/nodesN.csv') as csvfile:
    readcsv = csv.reader(csvfile, delimiter=';')
    nbNoeud = -1

    for row in readcsv:
        nbNoeud = nbNoeud + 1
        if(nbNoeud >= 1):
            listeCoord.append((float(row[0]), float(row[1]), row[2]))



#parser distance
with open('distancesG.csv') as csvfile:
    readcsv = csv.reader(csvfile, delimiter=';')
    matriceDistances = np.zeros((nbNoeud,nbNoeud))
    listedist = []
    for row in readcsv:
        listedist.append(row[0])
    for i in range(nbNoeud):
        for j in range(nbNoeud):
            matriceDistances[i,j] = listedist[nbNoeud*i+j]
            

def cout(b,matriceDistances):
    cout_boucle = 0
    cout_chaine = 0
    for boucle in b:
        for sous_boucle in boucle:
            if (len(sous_boucle) > 1):
                for i in range(len(sous_boucle)-1):
                    cout_chaine += matriceDistances[sous_boucle[i],sous_boucle[i+1]]
        for j in range(len(boucle)-1):
            cout_boucle += matriceDistances[boucle[j][0],boucle[j+1][0]]
        cout_boucle += matriceDistances[boucle[len(boucle)-1][0],boucle[0][0]]

    cout_reseau = cout_boucle + cout_chaine
    return cout_reseau           


Distributions = []
Antennes = []
for i in range(nbNoeud):
    if(listeCoord[i][2] == "distribution"):
        Distributions.append([listeCoord[i][0], listeCoord[i][1]])
    else:
        Antennes.append([listeCoord[i][0], listeCoord[i][1]])

