import pygame
pygame.init()

import sys

from configuration import *
from sprites import *

class Spritesheet:
    def __init__(self, path):
        self.spritesheet = pygame.image.load(path).convert()

    def get_image(self, x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.blit(self.spritesheet, (0,0), (x, y, width, height))
        sprite.set_colorkey((0,0,0))
        return sprite

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode([WIN_WIDTH, WIN_HEIGHT])
        self.clock = pygame.time.Clock()
        self.terrain_spritesheet = Spritesheet('images/terrain.png')
        self.player_spritesheet = Spritesheet('images/cats.png')  
        self.enermy_spritesheet = Spritesheet('images/evil.png')
        self.running = True
    
    def createTileMap(self):
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == 'B':
                    Block(self, j, i)
                if column == 'P':
                    self.player = Player(self, j, i)
                if column == 'E':
                    Enermy(self, j, i)

    def create(self):
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.createTileMap()

    def update(self):
        self.all_sprites.update()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()
  
    def main (self):
        while self.running:
            self.event()
            self.update()
            self.draw()

game = Game()
game.create()

while game.running:
    game.main()

pygame.quit()
sys.exit()