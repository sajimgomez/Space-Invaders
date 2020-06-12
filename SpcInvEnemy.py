import pygame


class SpaceEnemy(pygame.sprite.Sprite) :

    def __init__(self, Position) :

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('Eye.png')

        self.rect = self.image.get_rect()

        self.speed = [5, 0]

        self.rect.topleft = Position


    def UpdateEnemy(self, Width) :

        if self.rect.left < 0 :
        
            self.speed = [0, 40]

            self.rect.move_ip(self.speed)

            self.rect.left = 0

            self.speed = [5, 0]

        elif self.rect.right > Width :

            self.speed = [0, 40]

            self.rect.move_ip(self.speed)

            self.rect.right = Width

            self.speed = [-5, 0]


        self.rect.move_ip(self.speed)


    def IsCollision(self, Bullets) :


        for bullet in Bullets.sprites() :

            if self.rect.colliderect(bullet) :

                return True

            else :

                return False


    def IsGameOver(self) :

        if self.rect.top > 400 :

            return True

        return False