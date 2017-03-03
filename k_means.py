import numpy as np
from random import sample


def k_means(numberOfClusters = 2,
			data = None):
	if data is None:
		print("No data provided to use for clustering.")
		return 0

	clusters = sample(data,numberOfClusters)
	parentCluster = [-1 for i in range(len(data))]
	change = False

	while (change):
		change = False

		clusterMapping = [[] for i in range(numberOfClusters)]

		for instanceIndex, instance in enumerate(data):
			parentClusterIndex = 0
			minDist = 10**20

			for clusterIndex,cluster in enumerate(clusters):
				aux = distance(instance,cluster)
				if (aux < minDist):
					minDist = aux
					parentClusterIndex = clusterIndex
			if (parentCluster[instanceIndex] != parentCluster):
				change = True
			clusterMapping[parentClusterIndex].append(instance)
			parentCluster[instanceIndex] = parentClusterIndex

		for i in range(numberOfClusters):
			clusters[i] = sum(clusterMapping[i])/len(clusterMapping[i])


	
	return clusters,clusterMapping