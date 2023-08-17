
import pygame
from pygame.image import load
from pygame.sprite import Sprite


class Heroi(Sprite):
    def __init__(self,path_img:str,size:tuple) -> None:
        super().__init__()
        self.image = load(path_img)
        self.rect = self.image.get_rect()
        self.velocidade = 1.5
        self.size = size

    def update(self):
        keys = pygame.key.get_pressed()


        if keys[pygame.K_LEFT]: # ESQUERDA
            if self.rect.x > 0:
                self.rect.x -= self.velocidade

        if keys[pygame.K_RIGHT]: # DIREITA
            if self.rect.x  < self.size[0] - 100:
                self.rect.x += self.velocidade
        
        if keys[pygame.K_DOWN]:# BAIXO
            if self.rect.y < self.size[1] - 100:
                self.rect.y += self.velocidade

        if keys[pygame.K_UP]: # CIMA
            if self.rect.y > 0:
                self.rect.y -= self.velocidade