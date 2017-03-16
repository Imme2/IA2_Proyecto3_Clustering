from PIL import Image
from k_means import k_means

if __name__ == '__main__':
	print("Coloque el nombre de la imagen a comprimir:")
	imageName = input()

	#imageName = "stardewValley.png"
	image = Image.open(imageName)

	pixels = image.load()

	width,height = image.size

	name,extension = imageName.split(".")

	pixelList = [[(0,0,0) for i in range(height)] for j in range(width)]

	for i in range(width):
		for j in range(height):
			pixelList[i][j] = pixels[i,j] 

	flattenedPixels = [i for sublist in pixelList for i in sublist]

	multiplier = 0
	for i in [2, 4, 8, 16, 32, 64, 128]:
		clusters,mapping = k_means(i,flattenedPixels,compression=True)
		for w in range(width):
			for h in range(height):
				pixels[w,h] = clusters[mapping[w*height+h]]
		image.save("ImagenesComprimidas/"+name + "K" + str(i) + "." + extension)		
