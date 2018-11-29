import csv
import numpy as np
import matplotlib.pyplot as plt

# parser node

listeCoord = []
listeCoordX = []
listeCoordY = []
listeCoordBis = []

nb_pts_distrib = 0
pts_distrib = []

with open('instances/nodesG.csv') as csvfile:
	readcsv = csv.reader(csvfile, delimiter=';')
	lineCount = -1
	nb_pts_distrib = 0
	for row in readcsv:
		lineCount = lineCount + 1
		if(lineCount >= 1):
			listeCoord.append((float(row[0]), float(row[1]), row[2]))
			listeCoordBis.append([float(row[0]), float(row[1])])
			listeCoordX.append(float(row[0]))
			listeCoordY.append(float(row[1]))
			if(row[2] == 'distribution'):
				nb_pts_distrib += 1
				pts_distrib.append([float(row[0]), float(row[1])])

plt.scatter(listeCoordX, listeCoordY)
plt.show()


matriceDistances = np.zeros((lineCount,lineCount))
listedist = []

#parser distance
with open('instances/distancesPIM.csv') as csvfile:
    readcsv = csv.reader(csvfile, delimiter=';')

    for row in readcsv:
        listedist.append(row[0])
    for i in range(lineCount):
        for j in range(lineCount):
            matriceDistances[i,j] = listedist[lineCount*i+j]
