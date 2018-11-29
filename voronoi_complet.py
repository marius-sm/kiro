import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
from scipy.spatial import cKDTree

listeCoord = []
listeCoordX = []
listeCoordY = []
points = []

nb_pts_distrib = 0
pts_distrib = []
pts_distribX = []
pts_distribY = []

with open('instances/nodesPIM.csv') as csvfile:
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

voronoi_kdtree = cKDTree(pts_distrib)

test_point_dist, test_point_regions = voronoi_kdtree.query(points, k=1)

groupsX = [[] for k in range(nb_pts_distrib)]
groupsY = [[] for k in range(nb_pts_distrib)]

for i in range(len(points)):
	groupsX[test_point_regions[i]].append(points[i][0])
	groupsY[test_point_regions[i]].append(points[i][1])

for i in range(nb_pts_distrib):
	r = np.random.random()
	g = np.random.random()
	b = np.random.random()
	plt.scatter(groupsX[i], groupsY[i], s=5, c=(r,g,b))
	print(len(groupsX[i]))

plt.scatter(pts_distribX, pts_distribY, c=(0,0,0), s=20)

plt.show()
