from PIL import Image
from k_means import k_means

if __name__ == '__main__':
	print("Coloque el nombre de la imagen a comprimir:")
	imageName = input()

	#imageName = "stardewValley.png"

	# Se carga la imagen y se obtienen los valores de sus pixeles
	#  (requiere pillow en python3, PIL en python2)
	image = Image.open(imageName)
	pixels = image.load()

	# Se obtiene el tamaño de la imagen
	width,height = image.size

	# Se obtiene el nombre y la extension de la imagen
	name,extension = imageName.split(".")

	# Se inicializa una lista de pixeles
	pixelList = [[(0,0,0) for i in range(height)] for j in range(width)]

	# Se aplana la matriz de pixeles en la lista
	for i in range(width):
		for j in range(height):
			pixelList[i][j] = pixels[i,j] 

	flattenedPixels = [i for sublist in pixelList for i in sublist]

	# Se corre k_means para cada K y se cambian los pixeles
	#  luego se guarda la imagen. 
	# (No se cambia la lista aplanada de pixeles).
	for i in [2, 4, 8, 16, 32, 64, 128]:
		clusters,mapping = k_means(i,flattenedPixels,compression=True)
		for w in range(width):
			for h in range(height):
				pixels[w,h] = clusters[mapping[w*height+h]]
		image.save("ImagenesComprimidas/"+name + "K" + str(i) + "." + extension)		
