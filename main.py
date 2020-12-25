import pygame, math
pygame.init()

class main_app:
	def __init__(self):
		self.screen = pygame.display.set_mode((600, 400))
		self.clock = pygame.time.Clock()
		self.l = loading((300, 200), (255, 255, 255), 10, 5)

		self.FPS = 20
	def run(self):
		while True:
			[exit() for i in pygame.event.get() if i.type == pygame.QUIT]
			self.screen.fill((0, 0, 0))
			self.clock.tick(self.FPS)
			self.l.draw()
			self.choose()
			pygame.display.update()

	def choose(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_UP]:
			self.l.coef += 1
			self.l.trail.clear()
			print(self.l.coef)
		if keys[pygame.K_DOWN]:
			self.l.coef -= 1
			self.l.trail.clear()
			print(self.l.coef)


class loading:
	def __init__(self, position, color, radius, width):
		self.color = color
		self.pos = position
		self.rad = radius
		self.w = width
		self.a = -90
		self.coef = 1000
		self.res = 1000
		self.trail = [self.pos]

	def draw(self):
		if len(self.trail) == 0:
			self.trail.append(self.pos)
		for i in self.trail:
			x = i[0] + round(self.rad * math.cos(self.a))
			y = i[1] + round(self.rad * math.sin(self.a))
			pygame.draw.circle(app.screen, self.color, (x, y), self.w)
			self.a -= self.coef
			self.trail.append((x, y))
			if len(self.trail) > self.res:
				del self.trail[0]


if __name__ =="__main__":
	app = main_app()
	app.run()
	
