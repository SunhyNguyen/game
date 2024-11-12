import pygame
from configuration import *

import random

import math

class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE

        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_spritesheet.get_image(991, 545, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Ground(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE

        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_spritesheet.get_image(447, 353, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE

        self.width = TILESIZE
        self.height = TILESIZE

        self.x_change = 0
        self.y_change = 0

        self.animationCounter = 0

        self.image = self.game.player_spritesheet.get_image(0, 0, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.direction = "right"
    
    def move(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_LEFT]:
            self.x_change = self.x_change - PLAYER_STEP
            self.direction = "left"
        
        elif pressed[pygame.K_RIGHT]:
            self.x_change = self.x_change + PLAYER_STEP
            self.direction = "right"

        elif pressed[pygame.K_UP]:
            self.y_change = self.y_change - PLAYER_STEP
            self.direction = "up"

        elif pressed[pygame.K_DOWN]:
            self.y_change = self.y_change + PLAYER_STEP
            self.direction = "down"

    def update(self):
        self.move()
        self.animation()
        self.collide_block()
        self.rect.x = self.rect.x + self.x_change
        self.rect.y = self.rect.y + self.y_change
        
        self.x_change = 0
        self.y_change = 0

    def animation(self):
        downAnimation = [self.game.player_spritesheet.get_image(0,0, self.width, self.height),
                        self.game.player_spritesheet.get_image(32,0, self.width, self.height),
                        self.game.player_spritesheet.get_image(64,0, self.width, self.height)]
        
        if self.direction == "down":
            if self.y_change == 0:
                self.image = self.game.player_spritesheet.get_image(32,0, self.width, self.height)
            else:
                self.image = downAnimation[math.floor(self.animationCounter)]
                self.animationCounter += 0.2
                if self.animationCounter >= 3:
                    self.animationCounter = 0


        upAnimation = [self.game.player_spritesheet.get_image(0,96, self.width, self.height),
                       self.game.player_spritesheet.get_image(32,96, self.width, self.height),
                       self.game.player_spritesheet.get_image(64,96, self.width, self.height)]
        
        if self.direction == "up":
            if self.y_change == 0:
                self.image = self.game.player_spritesheet.get_image(32,0, self.width, self.height)
            else:
                self.image = upAnimation[math.floor(self.animationCounter)]
                self.animationCounter += 0.2
                if self.animationCounter >= 3:
                    self.animationCounter = 0


        leftAnimation = [self.game.player_spritesheet.get_image(0,32, self.width, self.height),
                       self.game.player_spritesheet.get_image(32,32, self.width, self.height),
                       self.game.player_spritesheet.get_image(64,32, self.width, self.height)]
        
        if self.direction == "left":
            if self.x_change == 0:
                self.image = self.game.player_spritesheet.get_image(32,0, self.width, self.height)
            else:
                self.image = leftAnimation[math.floor(self.animationCounter)]
                self.animationCounter += 0.2
                if self.animationCounter >= 3:
                    self.animationCounter = 0


        rightAnimation = [self.game.player_spritesheet.get_image(0,64, self.width, self.height),
                       self.game.player_spritesheet.get_image(32,64, self.width, self.height),
                       self.game.player_spritesheet.get_image(64,64, self.width, self.height)]
        
        if self.direction == "right":
            if self.x_change == 0:
                self.image = self.game.player_spritesheet.get_image(32,0, self.width, self.height)
            else:
                self.image = rightAnimation[math.floor(self.animationCounter)]
                self.animationCounter += 0.2
                if self.animationCounter >= 3:
                    self.animationCounter = 0

    def collide_block(self):
        pressed = pygame.key.get_pressed()
        collide = pygame.sprite.spritecollide(self, self.game.blocks, False, pygame.sprite.collide_rect_ratio(1))

        if collide:
            if pressed[pygame.K_LEFT]:
                self.rect.x += PLAYER_STEP
            
            if pressed[pygame.K_RIGHT]:
                self.rect.x -= PLAYER_STEP

            if pressed[pygame.K_UP]:
                self.rect.y += PLAYER_STEP
            
            if pressed[pygame.K_DOWN]:
                self.rect.y -= PLAYER_STEP
        

class Enermy(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = ENERMY_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE

        self.width = TILESIZE
        self.height = TILESIZE

        self.x_change = 0
        self.y_change = 0

        self.animationCounter = 0

        self.image = self.game.enermy_spritesheet.get_image(0, 0, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.direction = random.choice(['left', 'right', 'up', 'down'])
        self.numberSteps = random.choice([30, 40, 50, 60, 70, 80, 90])
        self.stallSteps = 80
        self.currentSteps = 0 

        self.state = "moving"

    def move(self):
        if self.state == "moving":
            if self.direction == "left":
                self.x_change = self.x_change - ENERMY_STEP
                self.currentSteps += 1

            elif self.direction == "right":
                self.x_change = self.x_change + ENERMY_STEP
                self.currentSteps += 1

            elif self.direction == "up":
                self.y_change = self.y_change - ENERMY_STEP
                self.currentSteps += 1

            elif self.direction == "down":
                self.y_change = self.y_change + ENERMY_STEP
                self.currentSteps += 1
        elif self.state == "stalling":
            self.currentSteps += 1
            if self.currentSteps == self.stallSteps:
                self.state = "moving"
                self.currentSteps = 0
                self.direction = random.choice(['left', 'right', 'up', 'down'])


    def update(self):
        self.move()
        self.animation()
        self.rect.x = self.rect.x + self.x_change
        self.rect.y = self.rect.y + self.y_change

        self.x_change = 0
        self.y_change = 0
        if self.currentSteps == self.numberSteps:
            if self.state != "stalling":
                self.currentSteps = 0
            self.numberSteps = random.choice([30, 40, 50, 60, 70, 80, 90])
            self.state = "stalling"

    def animation(self):
        downAnimation = [self.game.enermy_spritesheet.get_image(0,0, self.width, self.height),
                        self.game.enermy_spritesheet.get_image(32,0, self.width, self.height),
                        self.game.enermy_spritesheet.get_image(64,0, self.width, self.height)]
        
        if self.direction == "down":
            if self.y_change == 0:
                self.image = self.game.enermy_spritesheet.get_image(32,0, self.width, self.height)
            else:
                self.image = downAnimation[math.floor(self.animationCounter)]
                self.animationCounter += 0.2
                if self.animationCounter >= 3:
                    self.animationCounter = 0


        upAnimation = [self.game.enermy_spritesheet.get_image(0,96, self.width, self.height),
                       self.game.enermy_spritesheet.get_image(32,96, self.width, self.height),
                       self.game.enermy_spritesheet.get_image(64,96, self.width, self.height)]
        
        if self.direction == "up":
            if self.y_change == 0:
                self.image = self.game.enermy_spritesheet.get_image(32,0, self.width, self.height)
            else:
                self.image = upAnimation[math.floor(self.animationCounter)]
                self.animationCounter += 0.2
                if self.animationCounter >= 3:
                    self.animationCounter = 0


        leftAnimation = [self.game.enermy_spritesheet.get_image(0,32, self.width, self.height),
                       self.game.enermy_spritesheet.get_image(32,32, self.width, self.height),
                       self.game.enermy_spritesheet.get_image(64,32, self.width, self.height)]
        
        if self.direction == "left":
            if self.x_change == 0:
                self.image = self.game.enermy_spritesheet.get_image(32,0, self.width, self.height)
            else:
                self.image = leftAnimation[math.floor(self.animationCounter)]
                self.animationCounter += 0.2
                if self.animationCounter >= 3:
                    self.animationCounter = 0


        rightAnimation = [self.game.enermy_spritesheet.get_image(0,64, self.width, self.height),
                       self.game.enermy_spritesheet.get_image(32,64, self.width, self.height),
                       self.game.enermy_spritesheet.get_image(64,64, self.width, self.height)]
        
        if self.direction == "right":
            if self.x_change == 0:
                self.image = self.game.enermy_spritesheet.get_image(32,0, self.width, self.height)
            else:
                self.image = rightAnimation[math.floor(self.animationCounter)]
                self.animationCounter += 0.2
                if self.animationCounter >= 3:
                    self.animationCounter = 0