import array
import random

width = int(input("Inserte ancho: "))
height = int(input("Inserte altura: "))
if width%2 == 0:
	width = width + 1
if height%2 == 0:
	height = height + 1
	
maxval = 255

#Creates a raster depending of the size given
image = array.array('B', [255, 255, 255] * width * height)

#Creates a raster with a different color each time we compile it
#image = array.array('B', [random.randrange(0,255) ,random.randrange(0,255) ,random.randrange(0,255)] * width * height) 

#Creates a raster with a different color for each pixel
# def randomImage(height,width):
# 	for y in range(height):
# 	 	for x in range(width):
# 	 		index = 3 * (y * width + x)
# 	 		image[index] = random.randrange(0,255)             # red channel
# 	 		image[index + 1] = random.randrange(0,255)         # green channel
# 	 		image[index + 2] = random.randrange(0,255)         # blue channel 
# randomImage(height, width)

# Function to set a pixel by coordinates and color 
# def setPixel(x,y,r,g,b):
# 	index = 3 * (y * width + x)
# 	image[index] = r
# 	image[index + 1] = g
# 	image[index + 2] = b

#Function to set pixels with a center
def setPixel(x,y,r,g,b):
	cx = width/2
	cy = height/2
	x = int(cx) + x
	y = int(cy) - y
	index = 3 * (y * width + x)
	image[index] = r
	image[index + 1] = g
	image[index + 2] = b

def setCenter(x,y,r,g,b):
	index = 3 * (y * width + x)
	image[index] = r
	image[index + 1] = g
	image[index + 2] = b



#Function to draw a line (NAIVE SOLUTION)
	#Line Equation
	#y = m*x + b
#Improvements
	#1. Check x1 < x2
	#2. larger axis, |y2 - y1| > |x2 - x1|
	#3. Make it work in all octancts
def drawLineNaive(x1, y1, x2, y2):
	#Assuming x2 y higher than x1
	m = (y2-y1)/(x2-x1)
	b = y1 - (m*x1)
	for x in range(x1, x2):
		y = int(m * x + b)
		setPixel(x, y, 0, 0, 0)
		#lista.append(str(x) + " " + str(y))
#We call the fucntion
#drawLineNaive(2, 2, 5, 10)


#Function to draw a line (DDA)
	#General Techniqe in CG
	#Applied toline drawing, circle drawing,
	#	shadow, illumination, etc.
	#
	#
	#Origin of the algorithm
	# y = m * x + b 		Initialize
	# y = m * (x+1) + b     Next y value
	# Analysing whats happens with the next y
	# y = m * x  + m + b
	# y = m * x + b + m
	# y = (m * x +  b) + m
	# y = y + m    <---------
	#
	#
	#Improvements	
def drawLineDda(x1, y1, x2, y2):
	m = (y2-y1)/(x2-x1)
	b = y1 - (m*x1)
	y = m * x1 + b
	setPixel(x1, y1, 0, 0, 0)
	for x in range(x1+1, x2):
		y = int(y + m) 
		setPixel(x, y, 0, 0, 0)
		#lista.append(str(x) + " " + str(y))
	setPixel(x2, y2, 0, 0, 0)

#We call the fucntion
#drawLineDda(1, 1, 8, 8)


def changeOct(x1, y1, x2 , y2):
	flag = []
	while 1:		
		if x1 > x2:
			x1, x2 = x2, x1
			flag.append("x")
			
		if y1 > y2:
			y1, y2 = y2, y1
			flag.append("y")

		else:
			break
		
	dx = x2 - x1
	dy = y2 - y1

	if dx == 0 or dy == 0:
		drawVertHori(x1, y1, x2, y2)
	else:
		m = dy / dx
		print(m)

		if 0 <= m <= 1:
			if x2 > x1:
				octa = 1
			else:
				octa = 5

		elif m>1:
			if y2 > y1:
				octa = 2
			else:
				octa = 6

		elif m<-1:
			if y1 < y2:
				octa = 3
			else:
				octa = 7

		elif 0 >= m >= -1:
			if x2 < x1:
				octa = 4
			else:
				octa = 8

		drawLineBresenhams(x1, y1, x2, y2, octa, flag)

def drawVertHori(x1, y1, x2, y2):
	dx = abs(x2 - x1)
	dy = abs(y2 - y1)
	if dx > dy:
		for x in range(dx+1):
			setPixel(x1, y1, 0, 0, 0)
			x1 = x1 + 1
	else:
		for y in range(dy+1):
			setPixel(x1, y1, 0, 0, 0)
			y1 = y1 + 1

	cx = width/2
	cy = height/2
	setCenter(int(cx), int(cy), 0, 0, 255)	

#Function to draw a line (Bresenham Middle Point)
	#Is a generalitations of bresenhams, it uses DDA and the idea
	#is to use only integer operations.
	#the decition is binary 
	# decision is made using the distance between:
 	#    next pixel and the middle point.
 	#    two distances: d1 and d2
 	#    d1 from the upper option and middle point
 	#    d2 from the lower option and middle point.
 	#    d2 == d1?   choose the lower, deltaY = 0
 	#    d2  > d1     choose the upper, 
 	#    d2  < d1     choose the lower.
 	#    (d1 - d2) >= 0, lower option
 	#    (d1 - d2) < 0, upper option
 	#    just need to check the sign of (d1-d2)
 	#    using 'improvements' he reach:  C*(d1-d2)
 	#         ->>>  result is:   just integer operation, and does not 
	#                            change the sign. 


def drawLineBresenhams(x1, y1, x2, y2, octa, flag):
	#Saving the coordinates
	coorx = []
	coory = []
	
	dx = abs(x2 - x1)
	dy = abs(y2 - y1) 

	coorx.append(x1)
	coory.append(y1)

	if dx >= dy:
		p = 2*dy - dx
		#update up
		up = 2*dy - 2*dx
		#update rigth
		ur = 2*dy
		y = y1

		if x1 >= 0 or x2 >= 0 :
			for x in range(x1+1, x2):
				if p < 0:
					p += ur
				else:
					p += up
					y = y + 1

				if octa == 1:
					coorx.append(x)
					coory.append(y)
				elif octa == 4:
					setPixel(-x, y, 0, 0, 0)	
					lista.append(str(-x) + " | " + str(y))
				elif octa == 5:
					xp = -x
					yp = -y
					coorx.append(xp)
					coory.append(yp)
				elif octa == 8:
					setPixel(x, -y, 0, 0, 0)	
					lista.append(str(x) + " | " + str(-y))

		else:
			for x in range(abs(x1)+1, abs(x2)):
				if p < 0:
					p += ur
				else:
					p += up
					y = y + 1

				if octa == 1:
					coorx.append(x)
					coory.append(y)
				elif octa == 4:
					setPixel(-x, y, 0, 0, 0)	
					lista.append(str(-x) + " | " + str(y))
				elif octa == 5:
					xp = -x
					xy = -y
					coorx.append(xp)
					coory.append(yp)
				elif octa == 8:
					setPixel(x, -y, 0, 0, 0)	
					lista.append(str(x) + " | " + str(-y))

	else:
		p = 2*dx - dy
		#update up
		up = 2*dx
		#update rigth
		ur = 2*dx - 2*dy
		x = x1

		if y1 >= 0 or y2 >= 0 :
			for y in range(y1+1, y2):
				if p < 0:
					p += up
				else:
					p += ur
					x = x + 1
				if octa == 2:
					coorx.append(x)
					coory.append(y)
				elif octa == 3:
					setPixel(-x, y, 0, 0, 0)
					lista.append(str(-x) + " | " + str(y))
				elif octa == 6:
					setPixel(-x, -y, 0, 0, 0)
					lista.append(str(-x) + " | " + str(-y))
				elif octa == 7:
					setPixel(x, -y, 0, 0, 0)
					lista.append(str(x) + " | " + str(-y))
		else:
			for y in range(abs(y1)+1, abs(y2)):
				if p < 0:
					p += up
				else:
					p += ur
					x = x + 1
				if octa == 2:
					coorx.append(x)
					coory.append(y)
				elif octa == 3:
					setPixel(-x, y, 0, 0, 0)
					lista.append(str(-x) + " | " + str(y))
				elif octa == 6:
					setPixel(-x, -y, 0, 0, 0)
					lista.append(str(-x) + " | " + str(-y))
				elif octa == 7:
					setPixel(x, -y, 0, 0, 0)
					lista.append(str(x) + " | " + str(-y))


	coorx.append(x2)
	coory.append(y2)

	for i in coorx:
		print(i)

	showLine(coorx, coory, flag)
	coorx = []
	coory = []

def showLine(coorx, coory, flag):
	yprime = []
	xprime = []

	for f in flag:
		print(f)

	for f in reversed(flag):
		if f == "y":
			yprime = coory[::-1]
		elif f == "x":
			xprime = coorx[::-1]
	flag = []		

	if xprime and yprime:
		for l in range(len(coorx)):
			setPixel(xprime[l], yprime[l],0,0,0)
	elif xprime:
		for l in range(len(coorx)):
			setPixel(xprime[l], coory[l],0,0,0)
	elif yprime:
		for l in range(len(coorx)):
			setPixel(coorx[l], yprime[l],0,0,0)
	elif len(xprime) == 0 and len(yprime) == 0:
		for l in range(len(coorx)):
			setPixel(coorx[l], coory[l],0,0,0)

	cx = width/2
	cy = height/2
	setCenter(int(cx), int(cy), 0, 0, 255)	

x1 = int(input('Ingrese (X1): '))
y1 = int(input('Ingrese (Y1): '))
x2 = int(input('Ingrese (X2): '))
y2 = int(input('Ingrese (Y2): '))

changeOct(x1,y1,x2,y2)

#PPM HEADER AND DRAWER
ppm_header = 'P6 ' + str(width) + ' ' + str(height) + ' ' + str(maxval) + '\n'

print(ppm_header)
with open('cgppm.ppm', 'wb') as f:
	#The bytearray() method returns a bytearray object which is an array of the given bytes.
	#bytearray(source, encode)
	f.write(bytearray(ppm_header, 'ascii'))
	image.tofile(f)