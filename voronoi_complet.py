import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
from scipy.spatial import cKDTree
import random
import math
import copy
import tsp

listeCoord = []
listeCoordX = []
listeCoordY = []
points = []

nb_pts_distrib = 0
pts_distrib = []
pts_distribX = []
pts_distribY = []

with open('instances/nodesG.csv') as csvfile:
	readcsv = csv.reader(csvfile, delimiter=';')
	lineCount = -1
	nb_pts_distrib = 0
	for row in readcsv:
		lineCount = lineCount + 1
		if(lineCount >= 1):
			listeCoord.append((float(row[0]), float(row[1]), row[2]))
			points.append([float(row[0]), float(row[1])])
			listeCoordX.append(float(row[0]))
			listeCoordY.append(float(row[1]))
			if(row[2] == 'distribution'):
				nb_pts_distrib += 1
				pts_distrib.append([float(row[0]), float(row[1])])
				pts_distribX.append(float(row[0]))
				pts_distribY.append(float(row[1]))


matriceDistances = np.zeros((len(points),len(points)))
listedist = []
#parser distance
with open('instances/distancesG.csv') as csvfile:
    readcsv = csv.reader(csvfile, delimiter=';')

    for row in readcsv:
        listedist.append(row[0])
    for i in range(lineCount):
        for j in range(lineCount):
            matriceDistances[i,j] = listedist[lineCount*i+j]

voronoi_kdtree = cKDTree(pts_distrib)

test_point_dist, test_point_regions = voronoi_kdtree.query(points, k=1)

groupsX = [[] for k in range(nb_pts_distrib)]
groupsY = [[] for k in range(nb_pts_distrib)]

groups = [[] for k in range(nb_pts_distrib)]
groups_bis = [[] for k in range(nb_pts_distrib)]

for i in range(len(points)):
	indice_pt = i
	indice_groupe = test_point_regions[i]
	groupsX[test_point_regions[i]].append(points[i][0])
	groupsY[test_point_regions[i]].append(points[i][1])
	groups[test_point_regions[i]].append((points[i][0], points[i][1], indice_pt, indice_groupe))
	groups_bis[test_point_regions[i]].append((points[i][0], points[i][1]))


matrices = []

print(len(points))

for n in range(nb_pts_distrib):
	mat = [[0 for k in range(len(groups[n]))] for l in range(len(groups[n]))]
	for i in range(len(groups[n])):
		for j in range(len(groups[n])):
			dist = matriceDistances[groups[n][i][2]][groups[n][j][2]]
			mat[i][j] = dist
	matrices.append(mat)

cout = 0

taille_circuit = 5

boucles = []
chaines = []

for i in range(nb_pts_distrib):
	boucle = []
	r = np.random.random()
	g = np.random.random()
	b = np.random.random()
	plt.scatter(groupsX[i], groupsY[i], s=5, c=(r,g,b))
	print(len(groupsX[i]))


	matrice_reduite = np.zeros((taille_circuit, taille_circuit))
	for k in range(taille_circuit):
		for l in range(taille_circuit):
			matrice_reduite[k][l] = matrices[i][k][l]

	r = range(len(matrice_reduite))
	dist = {(i, j): matrice_reduite[i][j] for i in r for j in r}
	t = tsp.tsp(groups_bis[i][0:taille_circuit], dist)
	print(t)

	boucle = t[1]
	for n in range(len(boucle)):
		boucle[n] = groups[i][boucle[n]][2]
	boucles.append(boucle)

	cout += t[0]

	print([groups_bis[i][0][0], groups_bis[i][0][1]])

	#plt.plot([groups_bis[i][0][0], groups_bis[i][1][0]], [groups_bis[i][0][1], groups_bis[i][1][1]])
	for n in range(taille_circuit-1):
		plt.plot([groups_bis[i][n][0], groups_bis[i][n+1][0]], [groups_bis[i][n][1], groups_bis[i][n+1][1]], c='b')
	plt.plot([groups_bis[i][taille_circuit-1][0], groups_bis[i][0][0]], [groups_bis[i][taille_circuit-1][1], groups_bis[i][0][1]], c='b')

	print(len(matrice_reduite))
	for n in range(taille_circuit, len(groupsX[i])):
		min_dist = 10000000
		min_m = 0
		for m in range(0,taille_circuit):
			dist = matrices[i][n][m]
			if dist<min_dist:
				min_dist = dist
				min_m = m
		cout += min_dist
		plt.plot([groups_bis[i][n][0], groups_bis[i][min_m][0]], [groups_bis[i][n][1], groups_bis[i][min_m][1]], c='r')
		chaines.append([groups[i][min_m][2],groups[i][n][2]])

plt.scatter(pts_distribX, pts_distribY, c=(0,0,0), s=20)

with open('G.txt', 'w') as f:
	for b in boucles:
		f.write('b ');
		for e in b:
			f.write(str(e) + ' ')
		f.write("\n")
	for c in chaines:
		f.write('c ');
		for e in c:
			f.write(str(e) + ' ')
		f.write("\n")



plt.show()
