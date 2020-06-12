import SpcInvGlobalVar


def ShowScore(TextXC, TextYC) :

    sc = SpcInvGlobalVar.Font.render('Score: ' + str(SpcInvGlobalVar.Score), True, (0, 255, 0))

    SpcInvGlobalVar.Screen.blit(sc, (TextXC, TextYC))


def GameOver() :

    Over = SpcInvGlobalVar.OverFont.render('GAME OVER', True, (255, 255, 255))

    SpcInvGlobalVar.Screen.blit(Over, (200, 250))


def GameFinished() :

    Finished = SpcInvGlobalVar.OverFont.render('YOU WON', True, (255, 255, 255))

    SpcInvGlobalVar.Screen.blit(Finished, (200, 250))