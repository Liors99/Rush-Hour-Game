#Lior Somin
#Student Number: 30050532 
#25 November 2017
#Assignment 4, GUI version

import sys
import pygame
import math
from pygame.locals import *
from Car import*

#The main function of the game that sets up all the cars and enters the main loop of the game.
def main():
	all_cars={}
	car_num=0
	InputFile=open(sys.argv[1],"r")

	#Adding a car to the dictionary of the cars and assigning the key added the correct properties. (the properties are used in the Car.py module)
	for line in InputFile:
		car_num+=1
		new_line=(line.rstrip("\n")).split(",")
		all_cars[car_num]=Car(car_num,new_line[0],new_line[1],new_line[2],new_line[3])
		all_cars[car_num].width=(all_cars[car_num].coordinates[2]-all_cars[car_num].coordinates[0])
		all_cars[car_num].height=(all_cars[car_num].coordinates[3]-all_cars[car_num].coordinates[1])

	return all_cars

#A function that checks if 2 cars overlap or if a car is out of the boundries of the game. It takes in the car being moved and all the other cars as a parameter.
def check_move(all_cars,selected_car):
	for car_num in range(1,len(all_cars)+1):
		if car_num!=selected_car:
			if not(all_cars[car_num].coordinates[0]>=all_cars[selected_car].coordinates[2]) and \
			   not(all_cars[car_num].coordinates[1]>=all_cars[selected_car].coordinates[3]) and \
			   not(all_cars[selected_car].coordinates[0]>=all_cars[car_num].coordinates[2]) and \
			   not(all_cars[selected_car].coordinates[1]>=all_cars[car_num].coordinates[3]):
				return False

	#Checking if the selected car is out of boundries using its coordinates.
	if all_cars[selected_car].coordinates[0]<0 or \
	all_cars[selected_car].coordinates[1]<0 or \
	all_cars[selected_car].coordinates[2]>6 or \
	all_cars[selected_car].coordinates[3]>6:
		return False

#Setting up colours
WHITE=(255,255,255)
RED=(255,0,0)
BLACK=(0,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)

pygame.init()
DISPLAYSURF=pygame.display.set_mode((610,700))

#Intializing varibales and fonts
active = False
player_win=False
font_win=pygame.font.SysFont("monospace", 100)
font_steps=pygame.font.SysFont("monospace", 50)
win_text=font_win.render("YOU WON!",1,GREEN)
steps=0

#Acquiring all the cars dictionary from the main function.
all_cars=main()


#NOTE: the pygame version of this game is scaled by 100 comparted to the text version, so this is why the coordinates of the car are multiplied by factor of 100 everywhere.
while True:

	for event in pygame.event.get():

		#Going through all the cars and enabling the user to press on car and drag it across.
		for car_num in range(1,len(all_cars)+1):

			if event.type == QUIT:
				pygame.quit()
				sys.exit()
				
			if player_win==False:
				#When the user presses on a car, it will record its intital position (on the original grid), and enable the drag of the car object.	
				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 1:
						if car_draw[car_num].collidepoint(event.pos):
							selected_car=car_num
							active=True #A variable that allows the object to be dragged across.
							mouse_x, mouse_y = event.pos
							inital_x=all_cars[selected_car].coordinates[0]
							inital_y=all_cars[selected_car].coordinates[1]
							#Depending on the orientation of the car, change the offest in the x and y accordingly.
							if all_cars[selected_car].oreintation=="h":
								offset_x = all_cars[selected_car].coordinates[0] - mouse_x/100
								offset_y=0
							else:
								offset_y = all_cars[selected_car].coordinates[1] - mouse_y/100
								offset_x=0
							steps+=1

				#Once the user stops holding down left mouse button, disable the drag.
				elif event.type == pygame.MOUSEBUTTONUP:
					if event.button == 1:
						active=False

				#Makes the object follow the mouse.
				elif event.type == pygame.MOUSEMOTION:
					if active==True:
						mouse_x, mouse_y = event.pos
						#According to the orientation of the car, change the position of the car (on the original grid) using the mouse position and the offset.
						if all_cars[selected_car].oreintation=="h":
							all_cars[selected_car].coordinates[0]  = mouse_x/100 + offset_x
							all_cars[selected_car].coordinates[2]=all_cars[selected_car].coordinates[0]+all_cars[selected_car].width
						elif all_cars[selected_car].oreintation=="v":
							all_cars[selected_car].coordinates[1]  = mouse_y/100 + offset_y
							all_cars[selected_car].coordinates[3]=all_cars[selected_car].coordinates[1]+all_cars[selected_car].height

						#Keep track of the last direction that the car movement(down and right being positive, while left and up being negative)
						if all_cars[selected_car].coordinates[0]>inital_x or all_cars[selected_car].coordinates[1]>inital_y:
							direction=("positive")
						elif all_cars[selected_car].coordinates[0]<inital_x or all_cars[selected_car].coordinates[1]<inital_y:
							direction=("negative")

						#Check for the move the move of the selected car.
						if check_move(all_cars,selected_car)==False:
							#If the movement results in a movement that is out of boundries or overlap of other cars, disable the dragging of the car and round up the coordiantes to resolve the issue.
							active=False
							#If the last direction of the car was negative, then round up all the ccordinates of the car and round down if the movement was positive.
							if direction=="negative":
								all_cars[selected_car].coordinates[0]=int(math.ceil(all_cars[selected_car].coordinates[0]))
								all_cars[selected_car].coordinates[2]=int(math.ceil(all_cars[selected_car].coordinates[2]))
								all_cars[selected_car].coordinates[1]=int(math.ceil(all_cars[selected_car].coordinates[1]))
								all_cars[selected_car].coordinates[3]=int(math.ceil(all_cars[selected_car].coordinates[3]))
				
							elif direction=="positive":
								all_cars[selected_car].coordinates[0]=int(math.floor(all_cars[selected_car].coordinates[0]))
								all_cars[selected_car].coordinates[2]=int(math.floor(all_cars[selected_car].coordinates[2]))
								all_cars[selected_car].coordinates[1]=int(math.floor(all_cars[selected_car].coordinates[1]))
								all_cars[selected_car].coordinates[3]=int(math.floor(all_cars[selected_car].coordinates[3]))


	DISPLAYSURF.fill(WHITE)
	if player_win==False:
		car_draw={}
		#Drawing all the cars in the game, and assigning every car drawn to a new dictionary so that it will be possible to tell on what car the user pressed.
		for car_num in range(1,len(all_cars)+1):
			#Make the car colour black if it is not the desired car to be moved to the finish line and red if it is. Also, scale the car by a factor of 100 and add 10px border around every car.
			if car_num!=1:
				car_draw[car_num]=pygame.draw.rect(DISPLAYSURF,BLACK,(all_cars[car_num].coordinates[0]*100+10,all_cars[car_num].coordinates[1]*100+10,all_cars[car_num].width*100-10,all_cars[car_num].height*100-10))
			else:
				car_draw[car_num]=pygame.draw.rect(DISPLAYSURF,RED,(all_cars[car_num].coordinates[0]*100+10,all_cars[car_num].coordinates[1]*100+10,all_cars[car_num].width*100-10,all_cars[car_num].height*100-10))

		#Draw a line that seperates the main grid in the game from the move counter
		pygame.draw.rect(DISPLAYSURF,BLACK,(0,610,610,5))

	#Check for the winning condition of the game.
	if all_cars[1].coordinates[2]>=6:
		player_win=True
		DISPLAYSURF.blit(win_text,(65,240))

	#Displaying the total number of moves the user has taken
	steps_text=font_steps.render("Move count: "+str(steps),1,BLUE)
	DISPLAYSURF.blit(steps_text,(0,620))

	pygame.display.update()

pygame.quit()