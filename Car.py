#Lior Somin
#Student Number: 30050532 
#25 November 2017
#Assignment 4, class for both versions

class Car:
	coordinates=[0,0,0,0]
	oreintation=""
	number=""
	width=""
	height=""

	#Whenever a car is created, the user has to specify the car number, orientation, the length and the initial x and y coordinates.
	def __init__(self,car_num,car_orientation,car_length,y,x):
		self.oreintation=car_orientation
		min_x=int(x)
		min_y=int(y)
		self.length=int(car_length)
		self.number=str(car_num)
		#Create another set of coordinates with regards to the orientation and length of the car, the maximum x and y of the car.
		if self.oreintation=="h":
			max_x=min_x+self.length
			max_y=min_y+1
		elif self.oreintation=="v":
			max_x=min_x+1
			max_y=min_y+self.length
		#Update the coordinates of the car with the new coordinates.
		self.coordinates=[min_x,min_y,max_x,max_y]

	#A method that deals with the movement of the car, it takes in the number of units that the car moves by.
	def moveCar(self,unit):
		#Change the coordinates according to the orientation of the car and the number of units being moved. (does not change the either the x or the y according to the orientation).
		if self.oreintation=="h":
			self.coordinates[0]+=int(unit)
			self.coordinates[2]+=int(unit)
		elif self.oreintation=="v":
			self.coordinates[1]+=int(unit)
			self.coordinates[3]+=int(unit)