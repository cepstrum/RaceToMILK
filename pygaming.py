import pygame
import time
import random

pygame.init()


display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

car_width = 74
global_speed = 0 #speed everything falls at, increase to make things faster
speed_counter = 0


gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('RaceToMILK')

clock = pygame.time.Clock()

carImg = pygame.image.load('racecar.png')
enemyCarImgYellow = pygame.image.load('racecarYellow.png')
enemyCarImgGreen = pygame.image.load('racecarGreen.png')
enemyCarImgBlue = pygame.image.load('racecarBlue.png')
billImg = pygame.image.load('bill.png')


def car(x,y):
	gameDisplay.blit(carImg,(x,y))

def enemyBlue(x,y):
	gameDisplay.blit(enemyCarImgBlue,(x,y))

def enemyYellow(x,y):
	gameDisplay.blit(enemyCarImgYellow,(x,y))

def enemyGreen(x,y):
	gameDisplay.blit(enemyCarImgGreen,(x,y))

def bill(x,y):
	gameDisplay.blit(billImg,(x,y))

def things(thingx, thingy, thingw, thingh, color):
	pygame.draw.rect(gameDisplay, color, [thingx,thingy,thingw,thingh])

def text_objects(text,font):
	textSurface = font.render(text, True, black)
	return textSurface, textSurface.get_rect()

def message_display(text):
	largeText = pygame.font.Font('freesansbold.ttf', 95)
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = ((display_width/2),(display_height/2))
	gameDisplay.blit(TextSurf, TextRect)

	pygame.display.update()

	time.sleep(2)

	game_loop()


def crash():
	message_display('You Crashed')

def game_loop():
	heroCarX = (display_width * 0.45)
	heroCarY = (display_height - 74) #car is 74x74
	global global_speed
	global speed_counter

	heroCarX_change = 0
	
	
	

	if random.randrange(0,11) == 10:
		billY = -200
	else:
		billY = -2000

	bill_left_or_right = random.randrange(0,2)
	if bill_left_or_right == 0:
		billX = 0
	else:
		billX = display_width

	bill_speedY = 3 + global_speed
	bill_speedX = 3 + global_speed

	enemyBlueX = random.randrange(0, display_width - 74) #img is 74x74
	enemyBlueY = -600
	enemyBlue_speed = 7 + global_speed

	enemyGreenX = random.randrange(0,display_width -74)
	enemyGreenY = -3100
	enemyGreen_speed = 10 + global_speed

	enemyYellowX = random.randrange(0,display_width -74)
	enemyYellowY = -6100
	enemyYellow_speed = 13 + global_speed

	thing_startx = random.randrange(0, display_width)
	thing_starty = -600
	thing_speed = 7
	thing_width = 100
	thing_height = 100

	gameExit = False
	hero_LR_Speed = 7 #speed of movement left or right
	while not gameExit:

		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					heroCarX_change = -hero_LR_Speed
				if event.key == pygame.K_RIGHT:
					heroCarX_change = hero_LR_Speed

			
			

		heroCarX += heroCarX_change

		gameDisplay.fill(white)

		#things(thingx, thingy, thingw, thingh, color):
		things(thing_startx,thing_starty,thing_width,thing_height,black)
		thing_starty += thing_speed

		car(heroCarX,heroCarY)
		enemyBlue(enemyBlueX,enemyBlueY)
		enemyGreen(enemyGreenX,enemyGreenY)
		enemyYellow(enemyYellowX,enemyYellowY)

		
		bill(billX,billY)

		
		billY += bill_speedY
		if bill_left_or_right == 0 and billY > -141:
			billX += bill_speedX
		if bill_left_or_right == 1 and billY > -141:
			billX -= bill_speedX
		if billY > display_height:
			bill_left_or_right = random.randrange(0,2)
			if bill_left_or_right == 0:
				billX = 0
			else:
				billX = display_width

			if random.randrange(0,11) == 10:
				billY = -200
			else:
				billY = -2000
			
			


		enemyBlueY += enemyBlue_speed
		enemyGreenY += enemyGreen_speed
		enemyYellowY += enemyYellow_speed
		

		if heroCarX > display_width - car_width or heroCarX < 0:
			crash()

		if enemyBlueY > display_height:
			enemyBlueY = 0 - 74
			enemyBlueX = random.randrange(0,display_width)
			speed_counter += 1
		if enemyGreenY > display_height:
			enemyGreenY = -3100
			enemyGreenX = random.randrange(0,display_width)
			speed_counter += 1
		if enemyYellowY > display_height:
			enemyYellowY = -6100
			enemyYellowX = random.randrange(0,display_width)
			speed_counter += 1

		if thing_starty > display_height:
			thing_starty = 0 - thing_height
			thing_startx = random.randrange(0,display_width)
#bill.png is 55x142
		if heroCarY <= thing_starty + thing_height:
			if heroCarX > thing_startx and heroCarX < (thing_startx + thing_width) or (heroCarX + car_width) > thing_startx and (heroCarX + car_width) < (thing_startx + thing_width):
				print ('heroCarX crossover')

		#if speed_counter == 10:
			#global_speed += 1
			speed_counter = 0


		pygame.display.update()

		clock.tick(60)
game_loop()
pygame.quit()
quit()