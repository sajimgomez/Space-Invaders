import pygame, SpInvBullet


class Charger(pygame.sprite.Group) :

    def __init__(self, NumberOfBullets, Width, Length) :

        pygame.sprite.Group.__init__(self)

        self.ChargerCapacity = NumberOfBullets

        for i in range(self.ChargerCapacity) :

            bullet = SpInvBullet.Bullet(Width, Length)

            self.add(bullet)


    def Shoot(self, event, SpaceShipPosition) :

        if event.key == pygame.K_SPACE :

            for bullet in self.sprites() :

                if bullet.state == 'Ready' :

                    bullet.ShootBullet(SpaceShipPosition)

                    break


    def UpdateBullets(self, Enemies, Screen) :

        for bullet in self.sprites() :

            if bullet.state == 'Fired' :

                Screen.blit(bullet.image, bullet.rect)

                bullet.UpdateBullet()

            if bullet.rect[1] < 0 or bullet.IsCollision(Enemies):

                bullet.kill()

                del bullet


    def ReloadCharger(self, event, Width, Length) :

        if len(self) != self.ChargerCapacity and event.key == pygame.K_r :

            for i in range(self.ChargerCapacity) :

                bullet = SpInvBullet.Bullet(Width, Length)

                self.add(bullet)