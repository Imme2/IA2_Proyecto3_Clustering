from k_means import k_means
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
    f = open("iris.data","r")
    lines = f.readlines()
    f.close()
    points = [[float(x_i) for x_i in point.strip("\n\r").split(",")] for point in lines if len(point) > 2]
    print(points)
    points = normalizar(points)
    multiplier = 0
    for i in [2, 3, 4, 5]:
        clusters,mapping = k_means(i,points)
        print("Iris-Setosa: ",mapping[0:50],Counter(mapping[0:50]),"\n")
        print("Iris-Versicolor: ",mapping[50:100],Counter(mapping[50:100]),"\n")
        print("Iris-Virginica: ",mapping[100:150],Counter(mapping[100:150]),"\n")
