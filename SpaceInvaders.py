import pygame, sys, random

from pygame import mixer

pygame.init()

Length = 600

Width = 800

Screen = pygame.display.set_mode((Width, Length))

pygame.display.set_caption('Space Invaders')

Icon = pygame.image.load('ufo.png')

pygame.display.set_icon(Icon)

BackgroundImage = pygame.image.load('background.jpg')

mixer.music.load('BackgroundSound.wav')

mixer.music.play(- 1)

Font = pygame.font.Font('freesansbold.ttf', 32)

Text_X_Coordinate = 10

Text_Y_Coordinate = 10

OverFont = pygame.font.Font('freesansbold.ttf', 64)

Score = 0


class Bullet(pygame.sprite.Sprite) :

    def __init__(self) :

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


class Charger(pygame.sprite.Group) :

    def __init__(self, NumberOfBullets) :

        pygame.sprite.Group.__init__(self)

        self.ChargerCapacity = NumberOfBullets

        for i in range(self.ChargerCapacity) :

            bullet = Bullet()

            self.add(bullet)


    def Shoot(self, event, SpaceShipPosition) :

        if event.key == pygame.K_SPACE :

            for bullet in self.sprites() :

                if bullet.state == 'Ready' :

                    bullet.ShootBullet(SpaceShipPosition)

                    break


    def UpdateBullets(self, Enemies) :

        for bullet in self.sprites() :

            if bullet.state == 'Fired' :

                Screen.blit(bullet.image, bullet.rect)

                bullet.UpdateBullet()

            if bullet.rect[1] < 0 or bullet.IsCollision(Enemies):

                bullet.kill()

                del bullet


    def ReloadCharger(self, event) :

        if len(self) != self.ChargerCapacity and event.key == pygame.K_r :

            for i in range(self.ChargerCapacity) :

                bullet = Bullet()

                self.add(bullet)


class SpaceShip(pygame.sprite.Sprite) :

    def __init__(self) :

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('space-invaders.png')

        self.rect = self.image.get_rect()

        self.rect.midbottom = (Width / 2, Length)

        self.speed = [0, 0]


    def Update(self, event) :

        if event.key == pygame.K_LEFT and self.rect.left > 0 :
        
            self.speed = [- 5, 0]

        elif event.key == pygame.K_RIGHT and self.rect.right < Width :

            self.speed = [5, 0]
            

        else:
        
            self.speed = [0, 0]


        self.rect.move_ip(self.speed)


class SpaceEnemy(pygame.sprite.Sprite) :

    def __init__(self, Position) :

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('Eye.png')

        self.rect = self.image.get_rect()

        self.speed = [5, 0]

        self.rect.topleft = Position


    def UpdateEnemy(self) :

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


class EnemyArmy(pygame.sprite.Group) :

    def __init__(self, NumberOfEnemies) :

        self.NumberOfEnemies = NumberOfEnemies

        pygame.sprite.Group.__init__(self)

        pos_x = 64

        pos_y = 0

        for i in range(self.NumberOfEnemies) :

            Enemy = SpaceEnemy((pos_x, pos_y))

            self.add(Enemy)

            pos_x += Enemy.rect.width

            if pos_x >= Width :
                
                pos_x = 0

                pos_y += Enemy.rect.height

    
    def UpdateGroup(self, Bullets) :

        for Enem in self.sprites() :

            Enem.UpdateEnemy()


            if Enem.IsCollision(Bullets) :

                global Score

                Enem.kill()

                del Enem

                Score += 1

    
    def IsGameOver(self) :

        for Enem in self.sprites() :

            if Enem.IsGameOver() :

                for j in self.sprites() :

                    j.speed = [0, 0]

                return True

        return False


def ShowScore(TextXC, TextYC) :

    sc = Font.render('Score: ' + str(Score), True, (0, 255, 0))

    Screen.blit(sc, (TextXC, TextYC))


def GameOver() :

    Over = OverFont.render('GAME OVER', True, (255, 255, 255))

    Screen.blit(Over, (200, 250))


def GameFinished() :

    Finished = OverFont.render('YOU WON', True, (255, 255, 255))

    Screen.blit(Finished, (200, 250))


Player = SpaceShip()

charger = Charger(6)

Enemies = EnemyArmy(6)

Clock = pygame.time.Clock()

pygame.key.set_repeat(30)


while True :

    Clock.tick(60)

    Screen.blit(BackgroundImage, (0, 0))
    
    
    for event in pygame.event.get() :

        if event.type == pygame.QUIT :

            pygame.quit()

            sys.exit()

        if event.type == pygame.KEYDOWN :

            Player.Update(event)

            charger.Shoot(event, Player.rect)

            charger.ReloadCharger(event)


    if Score == Enemies.NumberOfEnemies :

        GameFinished()



    charger.UpdateBullets(Enemies)

    Enemies.UpdateGroup(charger)

    Enemies.draw(Screen)

    Screen.blit(Player.image, Player.rect)


    if Enemies.IsGameOver() :

        GameOver()


    ShowScore(Text_X_Coordinate, Text_Y_Coordinate)

    pygame.display.update()