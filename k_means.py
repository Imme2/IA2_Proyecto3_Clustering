import numpy as np
from random import sample
from math import sqrt

'''
	For our 3 color tuples
	Doesn't use decimals in order to output valid colors.
'''
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

'''
	Funcion que obtiene el centro de un cluster
	 (puede devolver numeros no enteros).
'''
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


'''
	Funcion simple que calcula la distancia (al cuadrado)
'''
def distance(A,B):
	return sum((A[i]-B[i])**2 for i in range(min(len(A),len(B))))


'''
	Algoritmo de K-medias: implementa k-medias.

	@numberOfClusters: numero de clusters a usar.
	@data: data a agrupar.
	@compression: un booleano que indica si se usan
			 colores (estos requieren un promedio diferente) o no

	Retorna los valores de los clusters y un arreglo
	que contiene
'''
def k_means(numberOfClusters = 2,
			data = None,
			compression=False):
	if data is None:
		print("No data provided to use for clustering.")
		return 0

	# Se inician los clusters con un grupo al azar de
	#  la data.
	clusters = sample(data,numberOfClusters)
	# Se inicializan los valores.
	parentCluster = [-1 for i in range(len(data))]
	change = len(data)

	print(len(data), numberOfClusters)

	iteracion = 0

	# Se inicializa una cota para las imagenes en 3
	#  en otro caso se usa 1000.
	cota = 3 if compression else 1000


	# Se empiezan las iteraciones para colocar y mover
	#  los clusters.
	while (change > 0.01 * len(data) and iteracion < cota):
		iteracion += 1
		#print(iteracion)
		#print(change)
		change = 0

		clusterMapping = [[] for i in range(numberOfClusters)]

		# Para cada instancia se calcula a que cluster pertenece
		for instanceIndex, instance in enumerate(data):
			parentClusterIndex = 0
			minDist = 10**10

			# Se busca la menor distancia a un cluster
			for clusterIndex,cluster in enumerate(clusters):
				aux = distance(instance,cluster)
				if (aux < minDist):
					minDist = aux
					parentClusterIndex = clusterIndex

			# Si hay un cambio se cuenta ese cambio con el fin
			#  de saber cuando se ha convergido
			if (parentCluster[instanceIndex] != parentClusterIndex):
				change += 1

			# se actualiza el cluster (aun cuando sea el mismo)
			clusterMapping[parentClusterIndex].append(instance)
			parentCluster[instanceIndex] = parentClusterIndex

		# Para cada cluster, en cada iteracion se cambia su
		#  posicion
		for i in range(numberOfClusters):
			clusters[i] = getAverageColor(clusterMapping[i]) \
					if compression \
						else getCentre(clusterMapping[i])

	# Se retornan los clusters y el mapping una vez que se converge
	return clusters,parentCluster