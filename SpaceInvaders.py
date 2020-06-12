import pygame, sys, random, SpInvBullet, SpcInvCharger, SpcInvSpaceShip, SpcInvEnemy, SpcInvEnemyArmy, SpcInvGlobalVar, SpcInvScreenFunc

from pygame import mixer

pygame.init()

pygame.display.set_caption('Space Invaders')

Icon = pygame.image.load('ufo.png')

pygame.display.set_icon(Icon)

BackgroundImage = pygame.image.load('background.jpg')

mixer.music.load('BackgroundSound.wav')

mixer.music.play(- 1)

Text_X_Coordinate = 10

Text_Y_Coordinate = 10

Player = SpcInvSpaceShip.SpaceShip(SpcInvGlobalVar.Width, SpcInvGlobalVar.Length)

charger = SpcInvCharger.Charger(6, SpcInvGlobalVar.Width, SpcInvGlobalVar.Length)

Enemies = SpcInvEnemyArmy.EnemyArmy(6, SpcInvGlobalVar.Width)

Clock = pygame.time.Clock()

pygame.key.set_repeat(30)


while True :

    Clock.tick(60)

    SpcInvGlobalVar.Screen.blit(BackgroundImage, (0, 0))
    
    
    for event in pygame.event.get() :

        if event.type == pygame.QUIT :

            pygame.quit()

            sys.exit()

        if event.type == pygame.KEYDOWN :

            Player.Update(event, SpcInvGlobalVar.Width)

            charger.Shoot(event, Player.rect)

            charger.ReloadCharger(event, SpcInvGlobalVar.Width, SpcInvGlobalVar.Length)


    if SpcInvGlobalVar.Score == Enemies.NumberOfEnemies :

        SpcInvScreenFunc.GameFinished()


    charger.UpdateBullets(Enemies, SpcInvGlobalVar.Screen)

    Enemies.UpdateGroup(charger, SpcInvGlobalVar.Width)

    Enemies.draw(SpcInvGlobalVar.Screen)

    SpcInvGlobalVar.Screen.blit(Player.image, Player.rect)


    if Enemies.IsGameOver() :

        SpcInvScreenFunc.GameOver()


    SpcInvScreenFunc.ShowScore(Text_X_Coordinate, Text_Y_Coordinate)

    pygame.display.update()