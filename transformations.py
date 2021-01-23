# ##############
# obj
# los vertices estan en un orden
# y el primer numero de las caras es la coordenada 
# con la que se une al siguiente inidcie de vertices
# ejemplo
# (1/1/1)(5/2/1)

# el 1 se unse con el 5

vertices = []

def readObj(nombreArchivo): 
	archivo = open(nombreArchivo,'r')
	contenido = archivo.readlines()
	return contenido

def readFile(contenido):
	cadenaAux = ""
	flag = 0
	for l in range(len(contenido)):
		for char in contenido[l]:
			if contenido[l][0] == "v" and contenido[l][1] == " ":
				if char != " " and char != "\n" and char != "\r":
			 		cadenaAux += char
			 		if cadenaAux == "v":
			 			cadenaAux = ""
			 		else:
			 			vertices.append(cadenaAux)
			 			cadenaAux = ""





nombreArchivo = input("Nombre de objeto 3D (formato .obj): \n----->")
cont = readObj(nombreArchivo)
readFile(cont)

for i in vertices:
	print(i)

print(vertices[0])
