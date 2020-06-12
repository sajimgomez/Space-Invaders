import pygame


class SpaceShip(pygame.sprite.Sprite) :

    def __init__(self, Width, Length) :

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('space-invaders.png')

        self.rect = self.image.get_rect()

        self.rect.midbottom = (Width / 2, Length)

        self.speed = [0, 0]


    def Update(self, event, Width) :

        if event.key == pygame.K_LEFT and self.rect.left > 0 :
        
            self.speed = [- 5, 0]

        elif event.key == pygame.K_RIGHT and self.rect.right < Width :

            self.speed = [5, 0]
            

        else:
        
            self.speed = [0, 0]


        self.rect.move_ip(self.speed)