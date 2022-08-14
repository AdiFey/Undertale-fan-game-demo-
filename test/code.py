import pygame
import sys
pygame.init()

W = 800
H = 600

sc = pygame.display.set_mode((W, H))
pygame.display.set_caption('Undertale fan-game (demo)')

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

FPS = 60
clock = pygame.time.Clock()

x = W // 2
y = H // 2
speed = 5

flLeft = flRight = flUp = flDown = None

while True:
	clock.tick(FPS)

	if flLeft:
		x -= speed
	elif flRight:
		x += speed
	elif flUp:
		y -= speed
	elif flDown:
		y += speed

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				flLeft = True
			elif event.key == pygame.K_RIGHT:
				flRight = True
			elif event.key == pygame.K_UP:
				flUp = True
			elif event.key == pygame.K_DOWN:
				flDown = True
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				flLeft = False
			elif event.key == pygame.K_RIGHT:
				flRight = False
			elif event.key == pygame.K_UP:
				flUp = False
			elif event.key == pygame.K_DOWN:
				flDown = False

	sc.fill(BLACK)
	pygame.draw.rect(sc, RED, (x, y, 20, 20))
	pygame.display.update()