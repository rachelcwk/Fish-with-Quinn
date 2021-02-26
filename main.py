import sys, pygame, random
from pygame.locals import *
from fish import *

pygame.init()
screen_info = pygame.display.Info()

size = (width, height) = (int(screen_info.current_w), int(screen_info.current_h))
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (0, 127, 255)




def main():
  while True:
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()
    screen.fill(color)
    fish.update()
    fish.draw(screen)
    screen.blit(fish_image, fish_rect)
    pygame.display.flip()


if __name__=='__main__':
  main()
