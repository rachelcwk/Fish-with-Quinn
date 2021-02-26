class Fish:
  def __init__(self, pos):
    self.fish_image = pygame.image.load("fish.png")
    self.fish_image= pygame.transform.smoothscale(fish_image, (60, 60))
    self.fish_rect = fish_image.get_rect()
    fish_rect.center= (width//2, height//2)

    speed = pygame.math.Vector2(0,10)
    rotation = random.randint(0,360)
    self.speed.rotate_ip(rotation)
    self.fish_image = pygame.transform.rotate(fish_image, rotation)

  def update(self):
    screen_info = pygame.display.Info()
    self.rect.move_ip(speed)
    if self.fish_rect.left < 0 or self.fish_rect.right > screen_info.current_w:
      self.speed[0] *= -1
      self.fish_image = pygame.transform.flip(self.fish_image, True, False)
      fish_rect.move_ip(speed[0],0)
    if self.fish_rect.top < 0 or self.fish_rect.bottom > screen_info.current_h:
      self.speed[1] *= -1
      self.fish_image = pygame.transform.flip(self.fish_image, False, True)
      self.fish_rect.move_ip(0, speed[1])
  
  def draw(self, screen):
    screen.blit(self.image, self.rect)