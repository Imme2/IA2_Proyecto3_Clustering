import numpy as np
from random import sample
from math import sqrt


# For our 3 color tuples
def getAverageColor(A):
	length = len(A)
	R = 0
	G = 0
	B = 0
	for color in A:
		R += color[0]
		G += color[1]
		B += color[2] 

	if (length != 0):
		R //= length
		G //= length
		B //= length

	return (R,G,B)

def getCentre(clusterSet):
	length = len(clusterSet)
	features = [0.0 for i in clusterSet[0]]
	for point in clusterSet :
		for dim in range(len(point)):
			features[dim]+=point[dim]
	if length != 0 :
		for dim in range(len(point)):
			features[dim]/=length
	return features

def distance(A,B):
	return sum((A[i]-B[i])**2 for i in range(min(len(A),len(B))))

def k_means(numberOfClusters = 2,
			data = None,
			compression=False):
	if data is None:
		print("No data provided to use for clustering.")
		return 0

	clusters = sample(data,numberOfClusters)
	parentCluster = [-1 for i in range(len(data))]
	change = len(data)

	print(len(data), numberOfClusters)

	iteracion = 0

	while (change > 0.01 * len(data) and iteracion < 1000):
		iteracion += 1
		#print(iteracion)
		#print(change)
		change = 0

		clusterMapping = [[] for i in range(numberOfClusters)]

		for instanceIndex, instance in enumerate(data):
			parentClusterIndex = 0
			minDist = 10**10

			for clusterIndex,cluster in enumerate(clusters):
				aux = distance(instance,cluster)
				if (aux < minDist):
					minDist = aux
					parentClusterIndex = clusterIndex
			if (parentCluster[instanceIndex] != parentClusterIndex):
				change += 1
			clusterMapping[parentClusterIndex].append(instance)
			parentCluster[instanceIndex] = parentClusterIndex

		for i in range(numberOfClusters):
			clusters[i] = getAverageColor(clusterMapping[i]) \
					if compression \
						else getCentre(clusterMapping[i])


	print("termine")
	return clusters,parentCluster