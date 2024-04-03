
import pygame, random
from random import randint
from pathlib import Path

WIDTH = 1200
HEIGHT = 700
BLACK = (0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = (0, 255, 0)
RED = ( 255, 0, 0)
BLUE = (0,0,255)
PLOMO = (122,122,122)
BROWN = (50,20,30)


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tower")
clock = pygame.time.Clock()


def draw_text1(surface, text, size, x, y):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, WHITE)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)

def draw_text2(surface, text, size, x, y):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, BLACK)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)

def draw_text3(surface, text, size, x, y):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, PLOMO)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)

def draw_hp_bar1(surface, x, y, percentage):
	BAR_LENGHT = 100
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, GREEN, fill)
	pygame.draw.rect(surface, WHITE, border, 2)

def draw_hp_bar(surface, x, y, percentage):
	BAR_LENGHT = 50
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, GREEN, fill)
	pygame.draw.rect(surface, BLACK, border, 2)

def draw_mana_bar(surface, x, y, percentage):
	BAR_LENGHT = 100
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, BLUE, fill)
	pygame.draw.rect(surface, WHITE, border, 2)

def draw_hp_bar2(surface, x, y, percentage):
	BAR_LENGHT = 50
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, BROWN, fill)
	pygame.draw.rect(surface, BLACK, border, 2)

def draw_hp_bar3(surface, x, y, percentage):
	BAR_LENGHT = 100
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, BROWN, fill)
	pygame.draw.rect(surface, BLACK, border, 2)

def distance(a,b):
	#pitagoras distancia entre a y b
	dx = b.rect.centerx - a.rect.centerx
	dy = b.rect.centery - a.rect.centery
	return (dx**2 + dy**2)**(1/2)

def direction(a,b):
	#vector unitario desde a a b
	dx = b.rect.centerx - a.rect.centerx
	dy = b.rect.centery - a.rect.centery
	radio = (dx**2 + dy**2)**(1/2)
	return dx/radio, dy/radio

creep_asedio1=None
creep_asedio2=None

class Player1(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/slark.png").convert(),(50,65))
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.centerx = 50
		self.rect.centery = 275
		self.speed_x = 0
		self.hp = 500
		self.mana = 100
		self.armor = 2
		self.counter = True

	def update(self):
		self.hp += 1/15
		self.mana += 1/50
		if self.mana < 0:
			self.mana = 0
		if self.mana > 100:
			self.mana = 100
		if self.hp <= 0:
			self.hp = 0
		if self.hp == 0:
			self.kill()
			
		if self.hp > 500:
			self.hp = 500
		self.speed_x = 0
		self.speed_y = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_a]:
			self.speed_x = -5
		if keystate[pygame.K_d]:
			self.speed_x = 5
		self.rect.x += self.speed_x
		if keystate[pygame.K_w]:
			self.speed_y = -5
		if keystate[pygame.K_s]:
			self.speed_y = 5
		self.rect.y += self.speed_y
		if self.rect.right > WIDTH:
			self.rect.right = WIDTH
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.top < 0:
			self.rect.top = 0
		if self.rect.bottom > 700:
			self.rect.bottom = 700

class Player2(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/slark.png").convert(),(50,65))
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.centerx = 1125
		self.rect.centery = 440
		self.speed_x = 0
		self.hp = 500
		self.mana = 100
		self.armor = 2
		self.counter = True

	def update(self):
		self.hp += 1/15
		self.mana += 1/50
		if self.mana < 0:
			self.mana = 0
		if self.mana > 100:
			self.mana = 100
		if self.hp <= 0:
			self.hp = 0
		if self.hp == 0:
			self.kill()
			
		if self.hp > 500:
			self.hp = 500
		self.speed_x = 0
		self.speed_y = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_LEFT]:
			self.speed_x = -5
		if keystate[pygame.K_RIGHT]:
			self.speed_x = 5
		self.rect.x += self.speed_x
		if keystate[pygame.K_UP]:
			self.speed_y = -5
		if keystate[pygame.K_DOWN]:
			self.speed_y = 5
		self.rect.y += self.speed_y
		
		if self.rect.right > WIDTH:
			self.rect.right = WIDTH
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.top < 0:
			self.rect.top = 0
		if self.rect.bottom > 700:
			self.rect.bottom = 700

class Tower1(pygame.sprite.Sprite):
	def __init__(self,target):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/tower1.png").convert(),(100,125))
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = 0
		self.rect.y = 0
		self.hp = 2000
		self.armor = 12
		self.target = target
		self.counter = True

	def shoot(self):
		bullet1 = Bullet1(tower1.rect.x,tower1.rect.y, self.target)
		all_sprites.add(bullet1)
		bullets1.add(bullet1)

	def update(self):
		now = pygame.time.get_ticks()
		if self.hp < 0:
			self.hp = 0
		if self.hp == 0:
			self.kill()
		if self.hp > 2000:
			self.hp = 2000
		target_list = [creep_melee2a, creep_melee2b, creep_melee2c, creep_ranged2, player2, tower2]

		if creep_asedio2 is not None:
			target_list.append(creep_asedio2)
		
		target_list = [t for t in target_list if t.hp > 0]
		distance_list = [(distance(self,t),t) for t in target_list]
		if len(distance_list)==0:
			distance_list = [(0,self.target)]
		self.target = sorted(distance_list, key=lambda x: x[0])[0][1]
		if abs(self.target.rect.centerx - self.rect.centerx) < 300 and abs(self.target.rect.centery - self.rect.centery) < 300:
			if self.counter:
				self.counter = False
				self.shoot()
				
		if (now//100) % 10 == 0:
			self.counter = True 
		
class Tower2(pygame.sprite.Sprite):
	def __init__(self, target):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/tower2.png").convert(),(100,125))
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = 1100
		self.rect.y = 575
		self.hp = 2000
		self.armor = 12
		self.target = target
		self.counter = True

	def shoot(self):
		bullet2 = Bullet2(tower2.rect.x,tower2.rect.y, self.target)
		all_sprites.add(bullet2)
		bullets2.add(bullet2)

	def update(self):
		now = pygame.time.get_ticks()
		if self.hp < 0:
			self.hp = 0
		if self.hp == 0:
			self.kill()
		if self.hp > 2000:
			self.hp = 2000
		target_list = [creep_melee1a, creep_melee1b, creep_melee1c, creep_ranged1, player1, tower1]
		if creep_asedio1 is not None:
			target_list.append(creep_asedio1)
		
		target_list = [t for t in target_list if t.hp > 0]
		distance_list = [(distance(self,t),t) for t in target_list]
		if len(distance_list)==0:
			distance_list = [(0,self.target)]
		self.target = sorted(distance_list, key=lambda x: x[0])[0][1]
		if abs(self.target.rect.centerx - self.rect.centerx) < 300 and abs(self.target.rect.centery - self.rect.centery) < 300:
			if self.counter:
				self.counter = False
				self.shoot()
			
		if (now//100) % 10 == 0:
			self.counter = True 
		
class Bullet1(pygame.sprite.Sprite):	
	def __init__(self ,x , y, target):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/1.png").convert(),(25,25))
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.centery = y
		self.rect.centerx = x
		self.speed = 10
		self.target = target

	def update(self):

		if (self.target.rect.centerx - self.rect.centerx) == 0:
			if self.target.rect.centery > self.rect.centery:
				self.rect.centery += self.speed 
			elif self.rect.centery > self.target.rect.centery:
				self.rect.centery -= self.speed
			else:
				self.rect.centery += 0
		elif (self.target.rect.centerx - self.rect.centerx) != 0:
			x,y = direction(self, self.target)
			self.rect.centerx += self.speed*x
			self.rect.centery += self.speed*y
		
class Bullet2(pygame.sprite.Sprite):	
	def __init__(self ,x , y, target):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/1.png").convert(),(25,25))
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.centery = y
		self.rect.centerx = x
		self.speed = 10
		self.target = target

	def update(self):

		if (self.target.rect.centerx - self.rect.centerx) == 0:
			if self.target.rect.centery > self.rect.centery:
				self.rect.centery += self.speed 
			elif self.rect.centery > self.target.rect.centery:
				self.rect.centery -= self.speed
			else:
				self.rect.centery += 0
		elif (self.target.rect.centerx - self.rect.centerx) != 0:
			x,y = direction(self, self.target)
			self.rect.centerx += self.speed*x
			self.rect.centery += self.speed*y
		
class Creep_melee1(pygame.sprite.Sprite):		
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/creep_melee1.png").convert(),(25,50))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = 0
		self.rect.y = 50
		self.speed = 3
		self.hp = 550
		self.armor = 2
		self.target = None

	def update(self):
		target_list = [creep_melee2a, creep_melee2b, creep_melee2c, creep_ranged2, player2, tower2]

		if creep_asedio2 is not None:
			target_list.append(creep_asedio2)
		
		target_list = [t for t in target_list if t.hp > 0]
		distance_list = [(distance(self,t),t) for t in target_list]
		if len(distance_list)==0:
			distance_list = [(0,self.target)]
		self.target = sorted(distance_list, key=lambda x: x[0])[0][1]
		if (self.target.rect.centerx - self.rect.centerx) == 0:
			if self.target.rect.centery > self.rect.centery:
				self.rect.centery += self.speed 
			elif self.rect.centery > self.target.rect.centery:
				self.rect.centery -= self.speed
			else:
				self.rect.centery += 0
		elif (self.target.rect.centerx - self.rect.centerx) != 0:
			x,y = direction(self, self.target)
			self.rect.centerx += self.speed*x
			self.rect.centery += self.speed*y

		if self.hp < 0:
			self.hp = 0
		if self.hp == 0:
			self.kill()
		if self.hp > 550:
			self.hp = 550

class Creep_melee1a(Creep_melee1):
	def __init__(self):
		super().__init__()

class Creep_melee1b(Creep_melee1):
	def __init__(self):
		super().__init__()
		
class Creep_melee1c(Creep_melee1):
	def __init__(self):
		super().__init__()

class Creep_melee2(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/creep_melee2.png").convert(),(25,50))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = 1200
		self.rect.y = 650
		self.speed = 3
		self.hp = 550
		self.armor = 2
		self.target = None

	def update(self):
		target_list = [creep_melee1a, creep_melee1b, creep_melee1c, creep_ranged1, player1, tower1]
		if creep_asedio1 is not None:
			target_list.append(creep_asedio1)
		
		target_list = [t for t in target_list if t.hp > 0]
		distance_list = [(distance(self,t),t) for t in target_list]
		if len(distance_list)==0:
			distance_list = [(0,self.target)]
		self.target = sorted(distance_list, key=lambda x: x[0])[0][1]
		if (self.target.rect.centerx - self.rect.centerx) == 0:
			if self.target.rect.centery > self.rect.centery:
				self.rect.centery += self.speed 
			elif self.rect.centery > self.target.rect.centery:
				self.rect.centery -= self.speed
			else:
				self.rect.centery += 0
		elif (self.target.rect.centerx - self.rect.centerx) != 0:
			x,y = direction(self, self.target)
			self.rect.centerx += self.speed*x
			self.rect.centery += self.speed*y

		if self.hp < 0:
			self.hp = 0
		if self.hp == 0:
			self.kill()
		if self.hp > 550:
			self.hp = 550
		
class Creep_melee2a(Creep_melee2):
	def __init__(self):
		super().__init__()
		
class Creep_melee2b(Creep_melee2):
	def __init__(self):
		super().__init__()
		
class Creep_melee2c(Creep_melee2):
	def __init__(self):
		super().__init__()

class Creep_range1(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/creep_ranged1.png").convert(),(25,50))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = 0
		self.rect.y = 50
		self.speed = 3
		self.hp = 300
		self.armor = 0
		self.target = None

	def update(self):
		target_list = [creep_melee2a, creep_melee2b, creep_melee2c, creep_ranged2, player2, tower2]
		
		if creep_asedio2 is not None:
			target_list.append(creep_asedio2)
		
		target_list = [t for t in target_list if t.hp > 0]
		distance_list = [(distance(self,t),t) for t in target_list]
		if len(distance_list)==0:
			distance_list = [(0,self.target)]
		self.target = sorted(distance_list, key=lambda x: x[0])[0][1]
		if (self.target.rect.centerx - self.rect.centerx) == 0:
			if self.target.rect.centery > self.rect.centery:
				self.rect.centery += self.speed 
			elif self.rect.centery > self.target.rect.centery:
				self.rect.centery -= self.speed
			else:
				self.rect.centery += 0
		elif (self.target.rect.centerx - self.rect.centerx) != 0:
			x,y = direction(self, self.target)
			self.rect.centerx += self.speed*x
			self.rect.centery += self.speed*y
		
		if self.hp < 0:
			self.hp = 0
		if self.hp == 0:
			self.kill()
		if self.hp > 300:
			self.hp = 300

class Creep_range2(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/creep_ranged2.png").convert(),(25,50))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = 1200
		self.rect.y = 650
		self.speed = 3
		self.hp = 300
		self.armor = 0
		self.target = None

	def update(self):
		target_list = [creep_melee1a, creep_melee1b, creep_melee1c, creep_ranged1, player1, tower1]
		
		if creep_asedio1 is not None:
			target_list.append(creep_asedio1)
		
		target_list = [t for t in target_list if t.hp > 0]
		distance_list = [(distance(self,t),t) for t in target_list]
		if len(distance_list)==0:
			distance_list = [(0,self.target)]
		self.target = sorted(distance_list, key=lambda x: x[0])[0][1]
		if (self.target.rect.centerx - self.rect.centerx) == 0:
			if self.target.rect.centery > self.rect.centery:
				self.rect.centery += self.speed 
			elif self.rect.centery > self.target.rect.centery:
				self.rect.centery -= self.speed
			else:
				self.rect.centery += 0
		elif (self.target.rect.centerx - self.rect.centerx) != 0:
			x,y = direction(self, self.target)
			self.rect.centerx += self.speed*x
			self.rect.centery += self.speed*y

		if self.hp < 0:
			self.hp = 0
		if self.hp == 0:
			self.kill()
		if self.hp > 300:
			self.hp = 300

class Creep_asedio1(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/creep_asedio.png").convert(),(25,50))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = 0
		self.rect.y = 50
		self.speed = 3
		self.hp = 935
		self.armor = 0
		self.target = None

	def update(self):
		target_list = [creep_melee2a, creep_melee2b, creep_melee2c, creep_ranged2, creep_asedio2, player2, tower2]
		target_list = [t for t in target_list if t.hp > 0]
		distance_list = [(distance(self,t),t) for t in target_list]
		if len(distance_list)==0:
			distance_list = [(0,self.target)]
		self.target = sorted(distance_list, key=lambda x: x[0])[0][1]
		if (self.target.rect.centerx - self.rect.centerx) == 0:
			if self.target.rect.centery > self.rect.centery:
				self.rect.centery += self.speed 
			elif self.rect.centery > self.target.rect.centery:
				self.rect.centery -= self.speed
			else:
				self.rect.centery += 0
		elif (self.target.rect.centerx - self.rect.centerx) != 0:
			x,y = direction(self, self.target)
			self.rect.centerx += self.speed*x
			self.rect.centery += self.speed*y
		
		if self.hp < 0:
			self.hp = 0
		if self.hp == 0:
			self.kill()
		if self.hp > 935:
			self.hp = 935

class Creep_asedio2(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/creep_asedio2.png").convert(),(25,50))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = 1200
		self.rect.y = 650
		self.speed = 3
		self.hp = 935
		self.armor = 0
		self.target = None

	def update(self):
		target_list = [creep_melee1a, creep_melee1b, creep_melee1c, creep_ranged1, creep_asedio1, player1, tower1]
		target_list = [t for t in target_list if t.hp > 0]
		distance_list = [(distance(self,t),t) for t in target_list]
		if len(distance_list)==0:
			distance_list = [(0,self.target)]
		self.target = sorted(distance_list, key=lambda x: x[0])[0][1]
		if (self.target.rect.centerx - self.rect.centerx) == 0:
			if self.target.rect.centery > self.rect.centery:
				self.rect.centery += self.speed 
			elif self.rect.centery > self.target.rect.centery:
				self.rect.centery -= self.speed
			else:
				self.rect.centery += 0
		elif (self.target.rect.centerx - self.rect.centerx) != 0:
			x,y = direction(self, self.target)
			self.rect.centerx += self.speed*x
			self.rect.centery += self.speed*y
		
		if self.hp < 0:
			self.hp = 0
		if self.hp == 0:
			self.kill()
		if self.hp > 935:
			self.hp = 935

def show_go_screen():
	
	screen.fill(BLACK)
	draw_text1(screen, "Tower", 65, WIDTH // 2, HEIGHT // 4)
	draw_text1(screen, "Destruye la torre enemiga", 20, WIDTH // 2, HEIGHT // 2)
	draw_text1(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 3/4)
	
	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					waiting = False

def show_game_over_screen1():
	screen.fill(BLACK)
	draw_text1(screen, "Radiant victory", 60, WIDTH  // 2, HEIGHT * 1/4)
		#draw_text(screen, "score: "+str(score), 30, WIDTH // 2, HEIGHT // 2)
	draw_text1(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 4/5)
	
	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					waiting = False

def show_game_over_screen2():
	screen.fill(BLACK)
	draw_text1(screen, "Dire victory", 60, WIDTH  // 2, HEIGHT * 1/4)
		#draw_text(screen, "score: "+str(score), 30, WIDTH // 2, HEIGHT // 2)
	draw_text1(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 4/5)

	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					waiting = False

# Cargar imagen de fondo
background = pygame.transform.scale(pygame.image.load("img/fond.png").convert(),(1200,700))

wave = False
waveca = False
game_over1 = False
game_over2 = False
running = True
start = True
while running:
	if game_over1:

		show_game_over_screen1()
		game_over1 = False
		all_sprites = pygame.sprite.Group()
		team1p_list = pygame.sprite.Group()
		team2p_list = pygame.sprite.Group()
		team1cr_list = pygame.sprite.Group()
		team2cr_list = pygame.sprite.Group()
		team1cma_list = pygame.sprite.Group()
		team1cmb_list = pygame.sprite.Group()
		team1cmc_list = pygame.sprite.Group()
		team2cma_list = pygame.sprite.Group()
		team2cmb_list = pygame.sprite.Group()
		team2cmc_list = pygame.sprite.Group()
		team1ca_list = pygame.sprite.Group()
		team2ca_list = pygame.sprite.Group()
		bullets1 = pygame.sprite.Group()
		bullets2 = pygame.sprite.Group()
		
		player1 = Player1()
		player2 = Player2()
		all_sprites.add(player1, player2)
		team1p_list.add(player1)
		team2p_list.add(player2)
		tower1 = Tower1(any)
		tower2 = Tower2(any)
		all_sprites.add(tower1, tower2)
		
		creep_melee1a = Creep_melee1a()
		creep_melee1b = Creep_melee1b()
		creep_melee1c = Creep_melee1c()
		creep_melee2a = Creep_melee2a()
		creep_melee2b = Creep_melee2b()
		creep_melee2c = Creep_melee2c()
		team1cma_list.add(creep_melee1a)
		team1cmb_list.add(creep_melee1b)
		team1cmc_list.add(creep_melee1c)
		team2cma_list.add(creep_melee2a)
		team2cmb_list.add(creep_melee2b)
		team2cmc_list.add(creep_melee2c)

		all_sprites.add(creep_melee1a, creep_melee2a, creep_melee1b, creep_melee2b, creep_melee1c, creep_melee2c)
			
		creep_ranged1 = Creep_range1()
		creep_ranged2 = Creep_range2()
		team1cr_list.add(creep_ranged1)
		team2cr_list.add(creep_ranged2)
		all_sprites.add(creep_ranged1, creep_ranged2)
		start_time = pygame.time.get_ticks()
		
	if game_over2:

		show_game_over_screen2()
		game_over2 = False
		all_sprites = pygame.sprite.Group()
		team1p_list = pygame.sprite.Group()
		team2p_list = pygame.sprite.Group()
		team1cr_list = pygame.sprite.Group()
		team2cr_list = pygame.sprite.Group()
		team1cma_list = pygame.sprite.Group()
		team1cmb_list = pygame.sprite.Group()
		team1cmc_list = pygame.sprite.Group()
		team2cma_list = pygame.sprite.Group()
		team2cmb_list = pygame.sprite.Group()
		team2cmc_list = pygame.sprite.Group()
		team1ca_list = pygame.sprite.Group()
		team2ca_list = pygame.sprite.Group()
		bullets1 = pygame.sprite.Group()
		bullets2 = pygame.sprite.Group()
		
		player1 = Player1()
		player2 = Player2()
		team1p_list.add(player1)
		team2p_list.add(player2)
		all_sprites.add(player1, player2)
		
		tower1 = Tower1(any)
		tower2 = Tower2(any)
		all_sprites.add(tower1, tower2)
		
		creep_melee1a = Creep_melee1a()
		creep_melee1b = Creep_melee1b()
		creep_melee1c = Creep_melee1c()
		creep_melee2a = Creep_melee2a()
		creep_melee2b = Creep_melee2b()
		creep_melee2c = Creep_melee2c()
		team1cma_list.add(creep_melee1a)
		team1cmb_list.add(creep_melee1b)
		team1cmc_list.add(creep_melee1c)
		team2cma_list.add(creep_melee2a)
		team2cmb_list.add(creep_melee2b)
		team2cmc_list.add(creep_melee2c)

		all_sprites.add(creep_melee1a, creep_melee2a, creep_melee1b, creep_melee2b, creep_melee1c, creep_melee2c)
			
		creep_ranged1 = Creep_range1()
		creep_ranged2 = Creep_range2()
		team1cr_list.add(creep_ranged1)
		team2cr_list.add(creep_ranged2)
		all_sprites.add(creep_ranged1, creep_ranged2)
		start_time = pygame.time.get_ticks()
		
	if start:
		show_go_screen()
		start = False

		all_sprites = pygame.sprite.Group()
		team1p_list = pygame.sprite.Group()
		team2p_list = pygame.sprite.Group()
		team1cr_list = pygame.sprite.Group()
		team2cr_list = pygame.sprite.Group()
		team1cma_list = pygame.sprite.Group()
		team1cmb_list = pygame.sprite.Group()
		team1cmc_list = pygame.sprite.Group()
		team2cma_list = pygame.sprite.Group()
		team2cmb_list = pygame.sprite.Group()
		team2cmc_list = pygame.sprite.Group()
		team1ca_list = pygame.sprite.Group()
		team2ca_list = pygame.sprite.Group()
		bullets1 = pygame.sprite.Group()
		bullets2 = pygame.sprite.Group()
		
		player1 = Player1()
		player2 = Player2()
		team1p_list.add(player1)
		team2p_list.add(player2)
		all_sprites.add(player1, player2)
		
		tower1 = Tower1(any)
		tower2 = Tower2(any)
		all_sprites.add(tower1, tower2)
		
		creep_melee1a = Creep_melee1a()
		creep_melee1b = Creep_melee1b()
		creep_melee1c = Creep_melee1c()
		creep_melee2a = Creep_melee2a()
		creep_melee2b = Creep_melee2b()
		creep_melee2c = Creep_melee2c()
		team1cma_list.add(creep_melee1a)
		team1cmb_list.add(creep_melee1b)
		team1cmc_list.add(creep_melee1c)
		team2cma_list.add(creep_melee2a)
		team2cmb_list.add(creep_melee2b)
		team2cmc_list.add(creep_melee2c)

		all_sprites.add(creep_melee1a, creep_melee2a, creep_melee1b, creep_melee2b, creep_melee1c, creep_melee2c)
					
		creep_ranged1 = Creep_range1()
		creep_ranged2 = Creep_range2()
		team1cr_list.add(creep_ranged1)
		team2cr_list.add(creep_ranged2)
		all_sprites.add(creep_ranged1, creep_ranged2)
		start_time = pygame.time.get_ticks()
		
	if wave:
		wave = False
		creep_melee1a = Creep_melee1a()
		creep_melee1b = Creep_melee1b()
		creep_melee1c = Creep_melee1c()
		creep_melee2a = Creep_melee2a()
		creep_melee2b = Creep_melee2b()
		creep_melee2c = Creep_melee2c()
		team1cma_list.add(creep_melee1a)
		team1cmb_list.add(creep_melee1b)
		team1cmc_list.add(creep_melee1c)
		team2cma_list.add(creep_melee2a)
		team2cmb_list.add(creep_melee2b)
		team2cmc_list.add(creep_melee2c)

		all_sprites.add(creep_melee1a, creep_melee2a, creep_melee1b, creep_melee2b, creep_melee1c, creep_melee2c)
			
		creep_ranged1 = Creep_range1()
		creep_ranged2 = Creep_range2()
		team1cr_list.add(creep_ranged1)
		team2cr_list.add(creep_ranged2)
		all_sprites.add(creep_ranged1, creep_ranged2)
		
	if waveca:
		waveca = False
		creep_asedio1 = Creep_asedio1()	
		creep_asedio2 = Creep_asedio2()
		team1ca_list.add(creep_asedio1)
		team2ca_list.add(creep_asedio2)
		all_sprites.add(creep_asedio1, creep_asedio2)

	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	now = pygame.time.get_ticks() - start_time

	anow = pygame.time.get_ticks()

	if (anow//100) % 300 == 0:
		wave = True
	
	bnow = pygame.time.get_ticks()

	if (bnow//100) % 600 == 0:
		waveca = True
		
	if tower1.hp == 0:
		game_over2 = True
	if tower2.hp == 0:
		game_over1 = True

	if len(team1p_list) == 0:
		p1now = pygame.time.get_ticks()
		if (p1now//100) % 150 == 0:
			print("ahora")
			player1 = Player1()
			team1p_list.add(player1)
			all_sprites.add(player1)
		
	if len(team2p_list) == 0:
		p2now = pygame.time.get_ticks()
		if (p2now//100) % 150 == 19:
			print("ahora2")
			player2 = Player2()
			team2p_list.add(player2)
			all_sprites.add(player2)
		
	# Checar colisiones - player1 - player2
	hits = pygame.sprite.spritecollide(player1, team2p_list, False)
	for hit in hits:
		keystate = pygame.key.get_pressed()
		if player1.counter:
			if keystate[pygame.K_e]:
				player1.counter = False
				player2.hp -= 5
		if not keystate[pygame.K_e]:
			player1.counter = True
		
	# Checar colisiones - player2 - player1
	hits = pygame.sprite.spritecollide(player2, team1p_list, False)
	for hit in hits:
		keystate = pygame.key.get_pressed()
		if player2.counter:
			if keystate[pygame.K_1]:
				player2.counter = False
				player1.hp -= 5
		if not keystate[pygame.K_1]:
			player2.counter = True
		
	# Checar colisiones - player1 - creeps meleea
	hits = pygame.sprite.spritecollide(player1, team2cma_list, False)
	for hit in hits:	
		player1.hp -= 1/10
		keystate = pygame.key.get_pressed()
		if player1.counter:
			if keystate[pygame.K_e]:
				player1.counter = False
				creep_melee2a.hp -= 5
		if not keystate[pygame.K_e]:
			player1.counter = True
		
	# Checar colisiones - player2 - creeps meleea
	hits = pygame.sprite.spritecollide(player2, team1cma_list, False)
	for hit in hits:
		player2.hp -= 1/10
		keystate = pygame.key.get_pressed()
		if player2.counter:
			if keystate[pygame.K_1]:
				player2.counter = False
				creep_melee1a.hp -= 5
		if not keystate[pygame.K_1]:
			player2.counter = True
		
	# Checar colisiones - player1 - creeps meleeb
	hits = pygame.sprite.spritecollide(player1, team2cmb_list, False)
	for hit in hits:
		player1.hp -= 1/10
		keystate = pygame.key.get_pressed()
		if player1.counter:
			if keystate[pygame.K_e]:
				player1.counter = False
				creep_melee2b.hp -= 5
		if not keystate[pygame.K_e]:
			player1.counter = True
		
	# Checar colisiones - player2 - creeps meleeb
	hits = pygame.sprite.spritecollide(player2, team1cmb_list, False)
	for hit in hits:
		player2.hp -= 1/10
		keystate = pygame.key.get_pressed()
		if player2.counter:
			if keystate[pygame.K_1]:
				player2.counter = False
				creep_melee1b.hp -= 5
		if not keystate[pygame.K_1]:
			player2.counter = True
		
	# Checar colisiones - player1 - creeps meleec
	hits = pygame.sprite.spritecollide(player1, team2cmc_list, False)
	for hit in hits:
		player1.hp -= 1/10
		keystate = pygame.key.get_pressed()
		if player1.counter:
			if keystate[pygame.K_e]:
				player1.counter = False
				creep_melee2c.hp -= 5
		if not keystate[pygame.K_e]:
			player1.counter = True
	
	# Checar colisiones - player2 - creeps meleec
	hits = pygame.sprite.spritecollide(player2, team1cmc_list, False)
	for hit in hits:
		player2.hp -= 1/10
		keystate = pygame.key.get_pressed()
		if player2.counter:
			if keystate[pygame.K_1]:
				player2.counter = False
				creep_melee1c.hp -= 5
		if not keystate[pygame.K_1]:
			player2.counter = True
		
	# Checar colisiones - player1 - creeps ranged
	hits = pygame.sprite.spritecollide(player1, team2cr_list, False)
	for hit in hits:
		player1.hp -= 1/10
		keystate = pygame.key.get_pressed()
		if player1.counter:
			if keystate[pygame.K_e]:
				player1.counter = False
				creep_ranged2.hp -= 5
		if not keystate[pygame.K_e]:
			player1.counter = True
		
	# Checar colisiones - player2 - creeps ranged
	hits = pygame.sprite.spritecollide(player2, team1cr_list, False)
	for hit in hits:
		player2.hp -= 1/10
		keystate = pygame.key.get_pressed()
		if player2.counter:
			if keystate[pygame.K_1]:
				player2.counter = False
				creep_ranged1.hp -= 5
		if not keystate[pygame.K_1]:
			player2.counter = True
		
	# Checar colisiones - player1 - creep asedio
	hits = pygame.sprite.spritecollide(player1, team2ca_list, False)
	for hit in hits:
		player1.hp -= 1/10
		keystate = pygame.key.get_pressed()
		if player1.counter:
			if keystate[pygame.K_e]:
				player1.counter = False
				creep_asedio2.hp -= 5
		if not keystate[pygame.K_e]:
			player1.counter = True
		
	# Checar colisiones - player2 - creep asedio
	hits = pygame.sprite.spritecollide(player2, team1ca_list, False)
	for hit in hits:
		player2.hp -= 1/10
		keystate = pygame.key.get_pressed()
		if player2.counter:
			if keystate[pygame.K_1]:
				player2.counter = False
				creep_asedio1.hp -= 5
		if not keystate[pygame.K_1]:
			player2.counter = True
		
	# Checar colisiones - torre1 - player2
	hits = pygame.sprite.spritecollide(tower1, team2p_list, False)
	for hit in hits:
		#player2.hp -= 1
		keystate = pygame.key.get_pressed()
		if player2.counter:
			if keystate[pygame.K_1]:
				player2.counter = False
				tower1.hp -= 3
		if not keystate[pygame.K_1]:
			player2.counter = True
				
	# Checar colisiones - torre2 - player1
	hits = pygame.sprite.spritecollide(tower2, team1p_list, False)
	for hit in hits:
		#player1.hp -= 1
		keystate = pygame.key.get_pressed()
		if player1.counter:
			if keystate[pygame.K_e]:
				player1.counter = False
				tower2.hp -= 3
		if not keystate[pygame.K_e]:
			player1.counter = True

	# Checar colisiones - torre1 - player2
	hits = pygame.sprite.spritecollide(tower1, team1p_list, False)
	for hit in hits:
		player1.hp += 1
				
	# Checar colisiones - torre2 - player1
	hits = pygame.sprite.spritecollide(tower2, team2p_list, False)
	for hit in hits:
		player2.hp += 1
		
	# Checar colisiones - torre1 - creeps meleea
	hits = pygame.sprite.spritecollide(tower1, team2cma_list, False)
	for hit in hits:
		tower1.hp -= 1/70
			
	# Checar colisiones - torre2 - creeps meleea
	hits = pygame.sprite.spritecollide(tower2, team1cma_list, False)
	for hit in hits:
		tower2.hp -= 1/70
		
	# Checar colisiones - torre1 - creeps meleeb
	hits = pygame.sprite.spritecollide(tower1, team2cmb_list, False)
	for hit in hits:
		tower1.hp -= 1/70
		
	# Checar colisiones - torre2 - creeps meleeb
	hits = pygame.sprite.spritecollide(tower2, team1cmb_list, False)
	for hit in hits:
		tower2.hp -= 1/70
		
	# Checar colisiones - torre1 - creeps meleec
	hits = pygame.sprite.spritecollide(tower1, team2cmc_list, False)
	for hit in hits:
		tower1.hp -= 1/70
		
	# Checar colisiones - torre2 - creeps meleec
	hits = pygame.sprite.spritecollide(tower2, team1cmc_list, False)
	for hit in hits:
		tower2.hp -= 1/70
		
	# Checar colisiones - torre1 - creeps ranged
	hits = pygame.sprite.spritecollide(tower1, team2cr_list, False)
	for hit in hits:
		tower1.hp -= 1/70
		
	# Checar colisiones - torre2 - creeps ranged
	hits = pygame.sprite.spritecollide(tower2, team1cr_list, False)
	for hit in hits:
		tower2.hp -= 1/70

	# Checar colisiones - torre1 - creeps asedio
	hits = pygame.sprite.spritecollide(tower1, team2ca_list, False)
	for hit in hits:
		tower1.hp -= 1/10
		
	# Checar colisiones - torre2 - creeps asedio
	hits = pygame.sprite.spritecollide(tower2, team1ca_list, False)
	for hit in hits:
		tower2.hp -= 1/10
	
	# Checar colisiones - creeps meleea - creeps meleea
	hits = pygame.sprite.spritecollide(creep_melee1a, team2cma_list, False)
	for hit in hits:
		creep_melee1a.hp -= 1/10
		creep_melee2a.hp -= 1/10
		
	# Checar colisiones - creep melee - creeps meleea
	hits = pygame.sprite.spritecollide(creep_melee2a, team1cma_list, False)
	for hit in hits:
		creep_melee2a.hp -= 1/10
		creep_melee1a.hp -= 1/10
		
	# Checar colisiones - creep melee - creeps meleeb
	hits = pygame.sprite.spritecollide(creep_melee1a, team2cmb_list, False)
	for hit in hits:
		creep_melee1a.hp -= 1/10
		creep_melee2b.hp -= 1/10
			
	# Checar colisiones - creep melee - creeps meleeb
	hits = pygame.sprite.spritecollide(creep_melee2a, team1cmb_list, False)
	for hit in hits:
		creep_melee2a.hp -= 1/10
		creep_melee1b.hp -= 1/10
		
	# Checar colisiones - creep melee - creeps meleec
	hits = pygame.sprite.spritecollide(creep_melee1a, team2cmc_list, False)
	for hit in hits:
		creep_melee1a.hp -= 1/10
		creep_melee2c.hp -= 1/10
		
	# Checar colisiones - creep melee - creeps meleec
	hits = pygame.sprite.spritecollide(creep_melee2a, team1cmc_list, False)
	for hit in hits:
		creep_melee2a.hp -= 1/10
		creep_melee1c.hp -= 1/10
		
	# Checar colisiones - creep melee - creeps ranged
	hits = pygame.sprite.spritecollide(creep_melee1a, team2cr_list, False)
	for hit in hits:
		creep_melee1a.hp -= 1/10
		creep_ranged2.hp -= 1/10
		
	# Checar colisiones - creep melee - creeps ranged
	hits = pygame.sprite.spritecollide(creep_melee2a, team1cr_list, False)
	for hit in hits:
		creep_melee2a.hp -= 1/10
		creep_ranged1.hp -= 1/10
	
	# Checar colisiones - creeps meleea - creeps meleea
	hits = pygame.sprite.spritecollide(creep_melee1b, team2cma_list, False)
	for hit in hits:
		creep_melee1b.hp -= 1/10
		creep_melee2a.hp -= 1/10
		
	# Checar colisiones - creep melee - creeps meleea
	hits = pygame.sprite.spritecollide(creep_melee2b, team1cma_list, False)
	for hit in hits:
		creep_melee2b.hp -= 1/10
		creep_melee1a.hp -= 1/10
		
	# Checar colisiones - creep melee - creeps meleeb
	hits = pygame.sprite.spritecollide(creep_melee1b, team2cmb_list, False)
	for hit in hits:
		creep_melee1b.hp -= 1/10
		creep_melee2b.hp -= 1/10
		
	# Checar colisiones - creep melee - creeps meleeb
	hits = pygame.sprite.spritecollide(creep_melee2b, team1cmb_list, False)
	for hit in hits:
		creep_melee2b.hp -= 1/10
		creep_melee1b.hp -= 1/10
		
	# Checar colisiones - creep melee - creeps meleec
	hits = pygame.sprite.spritecollide(creep_melee1b, team2cmc_list, False)
	for hit in hits:
		creep_melee1b.hp -= 1/10
		creep_melee2c.hp -= 1/10
		
	# Checar colisiones - creep melee - creeps meleec
	hits = pygame.sprite.spritecollide(creep_melee2b, team1cmc_list, False)
	for hit in hits:
		creep_melee2b.hp -= 1/10
		creep_melee1c.hp -= 1/10
		
	# Checar colisiones - creep melee - creeps ranged
	hits = pygame.sprite.spritecollide(creep_melee1b, team2cr_list, False)
	for hit in hits:
		creep_melee1b.hp -= 1/10
		creep_ranged2.hp -= 1/10
		
	# Checar colisiones - creep melee - creeps ranged
	hits = pygame.sprite.spritecollide(creep_melee2b, team1cr_list, False)
	for hit in hits:
		creep_melee2b.hp -= 1/10
		creep_ranged1.hp -= 1/10

	# Checar colisiones - creeps meleea - creeps meleea
	hits = pygame.sprite.spritecollide(creep_melee1c, team2cma_list, False)
	for hit in hits:
		creep_melee1c.hp -= 1/10
		creep_melee2a.hp -= 1/10
		
	# Checar colisiones - creep melee - creeps meleea
	hits = pygame.sprite.spritecollide(creep_melee2c, team1cma_list, False)
	for hit in hits:
		creep_melee2c.hp -= 1/10
		creep_melee1a.hp -= 1/10
		
	# Checar colisiones - creep melee - creeps meleeb
	hits = pygame.sprite.spritecollide(creep_melee1c, team2cmb_list, False)
	for hit in hits:
		creep_melee1c.hp -= 1/10
		creep_melee2b.hp -= 1/10
		
	# Checar colisiones - creep melee - creeps meleeb
	hits = pygame.sprite.spritecollide(creep_melee2c, team1cmb_list, False)
	for hit in hits:
		creep_melee2c.hp -= 1/10
		creep_melee1b.hp -= 1/10
		
	# Checar colisiones - creep melee - creeps meleec
	hits = pygame.sprite.spritecollide(creep_melee1c, team2cmc_list, False)
	for hit in hits:
		creep_melee1c.hp -= 1/10
		creep_melee2c.hp -= 1/10
		
	# Checar colisiones - creep melee - creeps meleec
	hits = pygame.sprite.spritecollide(creep_melee2c, team1cmc_list, False)
	for hit in hits:
		creep_melee2c.hp -= 1/10
		creep_melee1c.hp -= 1/10
		
	# Checar colisiones - creep melee - creeps ranged
	hits = pygame.sprite.spritecollide(creep_melee1c, team2cr_list, False)
	for hit in hits:
		creep_melee1c.hp -= 1/10
		creep_ranged2.hp -= 1/10
		
	# Checar colisiones - creep melee - creeps ranged
	hits = pygame.sprite.spritecollide(creep_melee2c, team1cr_list, False)
	for hit in hits:
		creep_melee2c.hp -= 1/10
		creep_ranged1.hp -= 1/10
		
	# Checar colisiones - creeps rango - creeps meleea
	hits = pygame.sprite.spritecollide(creep_ranged1, team2cma_list, False)
	for hit in hits:
		creep_ranged1.hp -= 1/10
		creep_melee2a.hp -= 1/10
		
	# Checar colisiones - creep rango - creeps meleea
	hits = pygame.sprite.spritecollide(creep_ranged2, team1cma_list, False)
	for hit in hits:
		creep_ranged2.hp -= 1/10
		creep_melee1a.hp -= 1/10
		
	# Checar colisiones - creep rango - creeps meleeb
	hits = pygame.sprite.spritecollide(creep_ranged1, team2cmb_list, False)
	for hit in hits:
		creep_ranged1.hp -= 1/10
		creep_melee2b.hp -= 1/10
		
	# Checar colisiones - creep rango - creeps meleeb
	hits = pygame.sprite.spritecollide(creep_ranged2, team1cmb_list, False)
	for hit in hits:
		creep_ranged2.hp -= 1/10
		creep_melee1b.hp -= 1/10
		
	# Checar colisiones - creep rango - creeps meleec
	hits = pygame.sprite.spritecollide(creep_ranged1, team2cmc_list, False)
	for hit in hits:
		creep_ranged1.hp -= 1/10
		creep_melee2c.hp -= 1/10
		
	# Checar colisiones - creep rango - creeps meleec
	hits = pygame.sprite.spritecollide(creep_ranged2, team1cmc_list, False)
	for hit in hits:
		creep_ranged2.hp -= 1/10
		creep_melee1c.hp -= 1/10
		
	# Checar colisiones - creep rango - creeps ranged
	hits = pygame.sprite.spritecollide(creep_ranged1, team2cr_list, False)
	for hit in hits:
		creep_ranged1.hp -= 1/10
		creep_ranged2.hp -= 1/10
		
	# Checar colisiones - creep rango - creeps ranged
	hits = pygame.sprite.spritecollide(creep_ranged2, team1cr_list, False)
	for hit in hits:
		creep_ranged2.hp -= 1/10
		creep_ranged1.hp -= 1/10

	# Checar colisiones - player1  - disparo torre
	hits = pygame.sprite.spritecollide(player1, bullets2, True)
	for hit in hits:
		player1.hp -= 150

	# Checar colisiones - player2  - disparo torre
	hits = pygame.sprite.spritecollide(player2, bullets1, True)
	for hit in hits:
		player2.hp -= 150

	# Checar colisiones - creep  - disparo torre
	hits = pygame.sprite.spritecollide(creep_melee1a, bullets2, True)
	for hit in hits:
		creep_melee1a.hp -= 150

	# Checar colisiones - creep  - disparo torre
	hits = pygame.sprite.spritecollide(creep_melee1b, bullets2, True)
	for hit in hits:
		creep_melee1b.hp -= 150

	# Checar colisiones - creep  - disparo torre
	hits = pygame.sprite.spritecollide(creep_melee1c, bullets2, True)
	for hit in hits:
		creep_melee1c.hp -= 150

	# Checar colisiones - creep  - disparo torre
	hits = pygame.sprite.spritecollide(creep_ranged1, bullets2, True)
	for hit in hits:
		creep_ranged1.hp -= 150

	# Checar colisiones - creep asedio - disparo torre
	try:
		hits = pygame.sprite.spritecollide(creep_asedio1, bullets2, True)
		for hit in hits:
			creep_asedio1.hp -= 150
	except(AttributeError):
		pass

	# Checar colisiones - creep  - disparo torre
	hits = pygame.sprite.spritecollide(creep_melee2a, bullets1, True)
	for hit in hits:
		creep_melee2a.hp -= 150

	# Checar colisiones - creep  - disparo torre
	hits = pygame.sprite.spritecollide(creep_melee2b, bullets1, True)
	for hit in hits:
		creep_melee2b.hp -= 150

	# Checar colisiones - creep  - disparo torre
	hits = pygame.sprite.spritecollide(creep_melee2c, bullets1, True)
	for hit in hits:
		creep_melee2c.hp -= 150

	# Checar colisiones - creep  - disparo torre
	hits = pygame.sprite.spritecollide(creep_ranged2, bullets1, True)
	for hit in hits:
		creep_ranged2.hp -= 150

	# Checar colisiones - player1  - disparo torre
	try:
		hits = pygame.sprite.spritecollide(creep_asedio2, bullets1, True)
		for hit in hits:
			creep_asedio2.hp -= 150
	except(AttributeError):
		pass

	all_sprites.update()
			
	"""
	# dtención del juego en t = () en mlseg	
	now = pygame.time.get_ticks()
	if now > 16000:
		game_over = True"""
	
	screen.blit(background, [0, 0])

	all_sprites.draw(screen)

	#Marcador
	#draw_text(screen, str(score), 25, WIDTH // 2, 10)

	# Escudo.
	draw_text2(screen, "P1", 20, 210, 6)
	draw_text2(screen, "P2", 20, 740, 6)

	draw_hp_bar1(screen, 220, 5, player1.hp/5)
	draw_text2(screen, str(int(player1.hp)) + "/500", 10, 270, 6)
	if player1.hp > 0:
		draw_hp_bar(screen, player1.rect.x, player1.rect.y - 10, player1.hp/5)

	draw_hp_bar3(screen, 750, 5, player2.hp/5)
	draw_text1(screen, str(int(player2.hp))+ "/500", 10, 800, 6)
	if player2.hp > 0:
		draw_hp_bar2(screen, player2.rect.x, player2.rect.y - 10, player2.hp/5)

	draw_mana_bar(screen, 220, 15, player1.mana)
	draw_text2(screen, str(int(player1.mana))+ "/100", 10, 270, 16)

	draw_mana_bar(screen, 750, 15, player2.mana)
	draw_text2(screen, str(int(player2.mana))+ "/100", 10, 800, 16)

	draw_hp_bar1(screen, tower1.rect.x, tower1.rect.y - 5, tower1.hp/20)
	draw_text2(screen, str(int(tower1.hp)) + "/2000", 10, 50, 116)

	draw_hp_bar3(screen, tower2.rect.x, tower2.rect.y - 10, tower2.hp/20)
	draw_text2(screen, str(int(tower2.hp))+ "/2000", 10, 1145, 691)

	for creep_melee1a in team1cma_list:
		draw_hp_bar(screen, creep_melee1a.rect.x, creep_melee1a.rect.y - 10, creep_melee1a.hp/(55/10))
	
	for creep_melee1b in team1cmb_list:
		draw_hp_bar(screen, creep_melee1b.rect.x, creep_melee1b.rect.y - 10, creep_melee1b.hp/(55/10))
	
	for creep_melee1c in team1cmc_list:
		draw_hp_bar(screen, creep_melee1c.rect.x, creep_melee1c.rect.y - 10, creep_melee1c.hp/(55/10))
	
	for creep_ranged1 in team1cr_list:
		draw_hp_bar(screen, creep_ranged1.rect.x, creep_ranged1.rect.y - 10, creep_ranged1.hp/3)
	
	for creep_asedio1 in team1ca_list:
		draw_hp_bar(screen, creep_asedio1.rect.x, creep_asedio1.rect.y - 10, creep_asedio1.hp/(935/100))

	for creep_melee2a in team2cma_list:
		draw_hp_bar2(screen, creep_melee2a.rect.x, creep_melee2a.rect.y - 10, creep_melee2a.hp/(55/10))
	
	for creep_melee2b in team2cmb_list:
		draw_hp_bar2(screen, creep_melee2b.rect.x, creep_melee2b.rect.y - 10, creep_melee2b.hp/(55/10))
	
	for creep_melee2c in team2cmc_list:
		draw_hp_bar2(screen, creep_melee2c.rect.x, creep_melee2c.rect.y - 10, creep_melee2c.hp/(55/10))

	for creep_ranged2 in team2cr_list:
		draw_hp_bar2(screen, creep_ranged2.rect.x, creep_ranged2.rect.y - 10, creep_ranged2.hp/3)
		
	for creep_asedio2 in team2ca_list:
		draw_hp_bar2(screen, creep_asedio2.rect.x, creep_asedio2.rect.y - 10, creep_asedio2.hp/(935/100))
	

	#reloj
	draw_text2(screen, str(((now//60000)+(60))%(60))+":" + str(((now//1000)+(60))%(60)), 30, 600, 50)

	pygame.display.flip()