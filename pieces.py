import pygame

class piece():
	def __init__(self, x, y, image, colour):
		self.image = pygame.transform.scale(image, (100, 100))
		self.x = x
		self.y = y
		self.rect = self.image.get_rect()
		self.rect.topleft = (self.x, self.y)
		self.clicked = False
		self.colour = colour
		
		
	def get_colour(self):
		return self.colour

	def get_piece(self):
		return self.image
	
	def set_coordinates(self, x, y):
		self.x = x
		self.y = y
		self.rect.topleft = (self.x, self.y)
		
	def move_piece(self, square):
		self.y = int(square/8)*100
		self.x = (square % 8) * 100
		self.rect.topleft = (self.x, self.y)
		
	def draw(self, surface):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True

        #piece has been moved
		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False
			#update the coordinates of the piece to fit the board
			self.x = int((self.x+50)/100)*100
			self.y = int((self.y+50)/100)*100
			self.rect.topleft = (self.x, self.y)
			
		#draw image on screen
		surface.blit(self.image, (self.x, self.y))
		
		return self.clicked
