import pygame
import colors
import game

class Player(pygame.sprite.Sprite):

    def __init__(self, startingX, startingY, playerSize, playerSpeed, starting_health, playerimage):

        pygame.sprite.Sprite.__init__(self)
        #self.image.fill(colors.green)
        self.image = playerimage[0]
        self.rect = self.image.get_rect()
        self.rect.centerx  = startingX
        self.rect.bottom = startingY
        self.speedx = 0
        self.speedy = 0
        self.health = starting_health
        self.score = 0
        self.playerSpeed = playerSpeed
        self.spritetimer = 0

    def update(self, WIDTH, HEIGHT, playerimage):
        # Update sprite
        if self.spritetimer == 90:
            self.image = playerimage[2]
            self.spritetimer = 0
        elif self.spritetimer == 60:
            self.image = playerimage[1]
        elif self.spritetimer == 30:
            self.image = playerimage[0]
        self.spritetimer += 1

        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_a]:
            self.speedx = -1 * self.playerSpeed
        if keystate[pygame.K_d]:
            self.speedx = self.playerSpeed
        if keystate[pygame.K_w]:
            self.speedy = -1 * self.playerSpeed
        if keystate[pygame.K_s]:
            self.speedy = self.playerSpeed

        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0
