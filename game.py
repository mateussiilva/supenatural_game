import pygame
from pygame import event, display
from pygame.image import load
from pygame.transform import scale
from pygame.locals import QUIT
from pygame.sprite import Group,GroupSingle
import personagem




class Window():
    def __init__(self,size:tuple) -> None:
        pygame.init()
        self.display = pygame.display.set_mode(display=0,size=size)
        self.__background = scale(load("inferno.jpg"),size=size)

    def loaf_background(self):
        self.display.blit(self.__background,(0,0))



if __name__ == "__main__":
    SIZE= (1200,800)
    janela_jogo = Window(SIZE)
    dean = personagem.Heroi(path_img="jon.jpg",size=SIZE)
    grupo_herois = GroupSingle()
    grupo_herois.add(dean)
    while True:
        janela_jogo.loaf_background()
    
        # LER OS EVENTOS
        for eventos in event.get():
            if eventos.type == QUIT:
                pygame.quit()
                break
        grupo_herois.draw(janela_jogo.display)
        grupo_herois.update()

        display.update()

pygame.quit()