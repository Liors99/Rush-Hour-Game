#Lior Somin
#Student Number: 30050532 
#25 November 2017
#Assignment 4, text version

import sys
from Car import*

#The main function of the game that sets up all the cars and enters the main loop of the game.
def main():

	#Creating a dictionary that will contain all the cars that are in the game.
	all_cars={}
	car_num=1
	InputFile=open(sys.argv[1],"r")

	#Adding a car to the dictionary of the cars and assigning the key added the correct properties. (the properties are used in the Car.py module)
	for line in InputFile:
		new_line=(line.rstrip("\n")).split(",")
		all_cars[car_num]=Car(car_num,new_line[0],new_line[1],new_line[2],new_line[3])
		car_num+=1

	#The main loop of the game that will keep on running as long as the player didn't win the game.
	while all_cars[1].coordinates[2]<6:
		draw_grid(all_cars)	
		move_car(all_cars)
	#Checks for the the winning codition of the game.
	if all_cars[1].coordinates[2]>=6:
		draw_grid(all_cars)
		print("You won!")


#A function that deals with the movement of a car. It takes the all_cars dictionary as a parameter.
def move_car(all_cars):

	#Asking for the user's input and validating that the user has entered a correct input for the car he wants to move.
	valid_car=False
	while valid_car==False:
		choose_car=input("what car do you want to move? ")
		try:
			int(choose_car)
		except ValueError:
			print("Invalid input!")
		else:
			choose_car=int(choose_car)
			if choose_car>len(all_cars) or choose_car<1:
				print("Car does not exist")
			else:
				valid_car=True

	#Asking for the user's input and validating that the user has entered a correct input for the distance he wants to move the car selected.
	valid_distance=False
	while valid_distance==False:
		distance_move=input("what distance do you want to move it? ")
		try:
			int(distance_move)
		except ValueError:
			print("Invalid input!")
		else:
			distance_move=int(distance_move)
			if distance_move!=0:
				valid_distance=True
	
	#Checking if the user can move to the desired destination by moving the car a step by step untill the car reaches that distance, the step could be negative or positive depending on the direction. 
	allow_move=True
	if distance_move<0:
		step=-1
	elif distance_move>0:
		step=1
	#Moving the car a step by step and counting the total number of steps took using the unit_distance variable.
	for unit_distance in range(step,distance_move+step,step):
		if allow_move==True:
			all_cars[choose_car].moveCar(step)
			#Check if the move is possible.
			if check_move(all_cars,choose_car)==False:
				#If the move that the user made is not possible, move the car back to its original position and stop checking every step.
				all_cars[choose_car].moveCar(-1*unit_distance)
				allow_move=False


#A function that checks if 2 cars overlap or if a car is out of the boundries of the game. It takes in the car being moved and all the other cars as a parameter.
def check_move(all_cars,selected_car):

	#Going through all the cars in the game (except the one selected) and checking if the car selected overlaps with any other car.
	for car_num in range(1,len(all_cars)+1):
		if car_num!=selected_car:
			if not(all_cars[car_num].coordinates[0]>=all_cars[selected_car].coordinates[2]) and \
			   not(all_cars[car_num].coordinates[1]>=all_cars[selected_car].coordinates[3]) and \
			   not(all_cars[selected_car].coordinates[0]>=all_cars[car_num].coordinates[2]) and \
			   not(all_cars[selected_car].coordinates[1]>=all_cars[car_num].coordinates[3]):
				print("%d and %d overlap" %(selected_car,car_num))
				return False

	#Checking if the selected car is out of boundries using its coordinates.
	if all_cars[selected_car].coordinates[0]<0 or \
	all_cars[selected_car].coordinates[1]<0 or \
	all_cars[selected_car].coordinates[2]>6 or \
	all_cars[selected_car].coordinates[3]>6:
		print("Movement out of boundaries")
		return False


#A function that draws the grid, taking in all the cars dictionary as a parameter.
def draw_grid(all_cars):

	#print an empty line so the grid will be seperated from the rest of the text.
	print()
	grid=[]

	#Drawing an empty grid using the "·" character, and making the entire grid into a list. where every row would coorespond to the y value in the grid and every entry in the row itself, would coorespond to the x coordiante of the grid.
	for j in range(6):
		row=""
		for i in range(6):
			row+="·"
		new_row=list(row)
		grid.append(new_row)

	#Plotting the cars based on their orientation and position on the grid, and replacing every empry space in the grid with that car number.
	for car_num in range(1,len(all_cars)+1,1):
		for space in range(all_cars[car_num].length):
			if all_cars[car_num].oreintation=="h":
				grid[all_cars[car_num].coordinates[1]][all_cars[car_num].coordinates[0]+space]=str(car_num)
			elif all_cars[car_num].oreintation=="v":
				grid[all_cars[car_num].coordinates[1]+space][all_cars[car_num].coordinates[0]]=str(car_num)

	#Spacing out the grid by going through every entery in the line.
	for row in grid:
		counter=0
		for element in row:
			try:
				int(row[counter])
			#If the entery cannot be converted into an integer(teh "·" character), then insert 5 space after that entery.
			except ValueError: 
				row[counter]=row[counter]+ 5*" "
			#If the entery is an integer, then insert 5 spaces if it is a single digit number, and insert 4 spaces if it is a 2 digit number after that entery.
			else:
				if int(row[counter])>9:
					row[counter]=row[counter]+ 4*" "
				else:
					row[counter]=row[counter]+ 5*" "
			counter+=1
		#Printing the row
		print ("".join(row))

	#print an empty line so the grid will be seperated from the rest of the text.
	print()



main()



