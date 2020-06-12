import pygame, SpcInvEnemy, SpcInvGlobalVar


class EnemyArmy(pygame.sprite.Group) :

    def __init__(self, NumberOfEnemies, Width) :

        self.NumberOfEnemies = NumberOfEnemies

        pygame.sprite.Group.__init__(self)

        pos_x = 64

        pos_y = 0

        for i in range(self.NumberOfEnemies) :

            Enemy = SpcInvEnemy.SpaceEnemy((pos_x, pos_y))

            self.add(Enemy)

            pos_x += Enemy.rect.width

            if pos_x >= Width :
                
                pos_x = 0

                pos_y += Enemy.rect.height

    
    def UpdateGroup(self, Bullets, Width) :

        for Enem in self.sprites() :

            Enem.UpdateEnemy(Width)


            if Enem.IsCollision(Bullets) :

                Enem.kill()

                del Enem

                SpcInvGlobalVar.Score += 1

    
    def IsGameOver(self) :

        for Enem in self.sprites() :

            if Enem.IsGameOver() :

                for j in self.sprites() :

                    j.speed = [0, 0]

                return True

        return False