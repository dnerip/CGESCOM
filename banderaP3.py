#Creando una imagen en PPM
#es una forma basica para crear imagenes pero ineficiente, a su vez muy sencillo

#PLAIN PPM FORMAT
#BANDERA DE MEXICO
#P3
#3 3 255 <----- ancho y alto de la imagen (3x3) asi como valor de color (hasta 65536)
#0 255 0 255 255 255 255 0 0 
#0 255 0 100 50 0 255 0 0 
#0 255 0 255 255 255 255 0 0 

#FULL HD PPM RESOLUCTION IMAGE
print("P3")
print("1920 1080 255")

# #Funcion para pintar lineas
# def paint(r, g, b , n):
# 	for i in range(int(n)):
# 		print(str(r)+ " " + str(g)+ " " + str(b)+ " ")
		

# for i in range(int(1080/3)):
# 	paint(0, 255, 0, 1920/3)
# 	paint(255, 255, 255, 1920/3)
# 	paint(255, 0, 0, 1920/3)

# for i in range(int(1080/3)):
# 	paint(0, 255, 0, 1920/3)
# 	paint(100, 50, 0, 1920/3)
# 	paint(255, 0, 0, 1920/3)

# for i in range(int(1080/3)):
# 	paint(0, 255, 0, 1920/3)
# 	paint(255, 255, 255, 1920/3)
# 	paint(255, 0, 0, 1920/3)


#Para el tipo P6 se necesita manejar unsigned char en la funicon de pintar

raster= [1920, 1080, 255]

def setPixel(x, y , r, g, b):
	if x >= 1920 and y>=1080:
		return
	