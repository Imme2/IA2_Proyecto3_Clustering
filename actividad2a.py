from k_means import k_means,distance
from math import sqrt
from collections import Counter

# Extraida del segundo proyecto
# Funcion que normaliza la data, asume que el ultimo es la
#  clase y por lo tanto no lo normaliza
def normalizar(data):
    # the last one is assumed to be the result
    for i in range(len(data[0])):
        mean = sum(instancia[i] for instancia in data) / len(data)
        stddev = sqrt(sum((instancia[i] - mean) **2 for instancia in data) / len(data))
        for j in range(len(data)):
            data[j][i] = (data[j][i] - mean)/stddev
    return data

if __name__ == '__main__':

    # Leemos la data
    f = open("iris.data","r")
    lines = f.readlines()
    f.close()
    points = [[float(x_i) for x_i in point.strip("\n\r").split(",")] for point in lines if len(point) > 2]
    
    # Normalizamos
    points = normalizar(points)

    # para cada K se corre k_means y se 
    # guardan los resultados en un archivo
    for i in [2, 3, 4, 5]:
        clusters,mapping = k_means(i,points,False)
        
        resultsFile = open("Resultados/resultados_K="+str(i)+".csv","w")
        resultsFile.write("clase,cluster,cantidad_en_cluster\n")
        contador_setosa = Counter(mapping[0:50])
        contador_versicolor = Counter(mapping[50:100])
        contador_virginica = Counter(mapping[100:150])
        for j in range(i):
            resultsFile.write("Iris-Setosa,"+str(j)+","+str(contador_setosa[j])+"\n")
        for j in range(i):
            resultsFile.write("Iris-Versicolor,"+str(j)+","+str(contador_versicolor[j])+"\n")
        for j in range(i):
            resultsFile.write("Iris-Virginica,"+str(j)+","+str(contador_virginica[j])+"\n")
        
        resultsFile.close()
        
        # Se guardan las distancias entre clusters e instancias
        resultsFile = open("Resultados/distancias_K="+str(i)+".csv","w")
        resultsFile.write("cluster_id,instancia_id,distancia\n")
        for clust in range(len(clusters)) :
            for instancia in range(len(points)) :
                dist = distance(points[instancia], clusters[clust])
                resultsFile.write(str(clust)+","+str(instancia)+","+str(dist)+"\n")
        resultsFile.close()
