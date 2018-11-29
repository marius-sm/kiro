import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
from scipy.spatial import cKDTree


points = []

nb_pts_distrib = 0
pts_distrib = []

with open('instances/nodesPIM.csv') as csvfile:
	readcsv = csv.reader(csvfile, delimiter=';')
	lineCount = -1
	nb_pts_distrib = 0
	for row in readcsv:
		lineCount = lineCount + 1
		if(lineCount >= 1):
			points.append([float(row[0]), float(row[1])])
			if(row[2] == 'distribution'):
				nb_pts_distrib += 1
				pts_distrib.append([float(row[0]), float(row[1])])


matriceDistances = np.zeros((len(points),len(points)))
listedist = []
#parser distance
with open('instances/distancesPIM.csv') as csvfile:
    readcsv = csv.reader(csvfile, delimiter=';')

    for row in readcsv:
        listedist.append(row[0])
    for i in range(lineCount):
        for j in range(lineCount):
            matriceDistances[i,j] = listedist[lineCount*i+j]

voronoi_kdtree = cKDTree(pts_distrib)

test_point_dist, test_point_regions = voronoi_kdtree.query(points, k=1)

groups = [[] for k in range(nb_pts_distrib)]
groups_bis = [[] for k in range(nb_pts_distrib)]

for i in range(len(points)):
	indice_pt = i
	indice_groupe = test_point_regions[i]
	groups[test_point_regions[i]].append((points[i][0], points[i][1], indice_pt, indice_groupe))
	groups_bis[test_point_regions[i]].append((points[i][0], points[i][1]))


matrices = []

for n in range(nb_pts_distrib):
	mat = [[0 for k in range(len(groups[n]))] for l in range(len(groups[n]))]
	for i in range(len(groups[n])):
		for j in range(len(groups[n])):
			dist = matriceDistances[groups[n][i][2]][groups[n][j][2]]
			mat[i][j] = dist
	matrices.append(mat)




clusters = groups_bis


#### clusters[i] est une liste de 2-uplets  (les coordonnees des points du cluster)
#### matrices[i] est la matrice de distances du cluster i
