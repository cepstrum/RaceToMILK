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
globalSpeed = 0 #speed everything falls at, increase to make things faster

gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('RaceToMILK')

clock = pygame.time.Clock()

carImg = pygame.image.load('racecar.png')
enemyCarImgBlue = pygame.image.load('racecarBlue.png')


def car(x,y):
	gameDisplay.blit(carImg,(x,y))

def enemyBlue(x,y):
	gameDisplay.blit(enemyCarImgBlue,(x,y))

def things(thingx, thingy, thingw, thingh, color):
	pygame.draw.rect(gameDisplay, color, [thingx,thingy,thingw,thingh])
def text_objects(text,font):
	textSurface = font.render(text, True, black)
	return textSurface, textSurface.get_rect()

def message_display(text):
	largeText = pygame.font.Font('freesansbold.ttf', 115)
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

	heroCarX_change = 0

	enemyBlueX = random.randrange(0, display_width - 74) #img is 74x74
	enemyBlueY = -600
	enemyBlue_speed = 7 + globalSpeed

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
		enemyBlueY += enemyBlue_speed

		if heroCarX > display_width - car_width or heroCarX < 0:
			crash()

		if enemyBlueY > display_height:
			enemyBlueY = 0 - 74
		if thing_starty > display_height:
			thing_starty = 0 - thing_height
			thing_startx = random.randrange(0,display_width)

		if heroCarY <= thing_starty + thing_height:
			print('step 1')
			if heroCarX > thing_startx and heroCarX < (thing_startx + thing_width) or (heroCarX + car_width) > thing_startx and (heroCarX + car_width) < (thing_startx + thing_width):
				print ('heroCarX crossover')
				crash()






		pygame.display.update()

		clock.tick(60)
game_loop()
pygame.quit()
quit()