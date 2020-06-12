import pygame


class Bullet(pygame.sprite.Sprite) :

    def __init__(self, Width, Length) :

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('bullet.png')

        self.rect = self.image.get_rect()

        self.rect.midbottom = (Width / 2, Length - 64)

        self.speed = [0, 0]

        self.state = 'Ready'


    def ShootBullet(self, SpaceshipPosition) :

        self.state = 'Fired'

        self.rect.midbottom = (SpaceshipPosition[0] + 32, SpaceshipPosition[1] - 64)

        self.speed = [0, -5]

    
    def UpdateBullet(self) :

        self.rect.move_ip(self.speed)

    
    def IsCollision(self, Enemies) :

        for enemy in Enemies.sprites() :

            if self.rect.colliderect(enemy) :

                return True

            else :

                return False