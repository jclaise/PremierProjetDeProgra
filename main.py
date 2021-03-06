import pygame

"""
"
" Classe World, initialisation de pygame et affichage de la carte, joueurs
"
"""


class World:
    def __init__(self):
        pygame.init()
        self.time = pygame.time.Clock()
        self.FPS = 60
        self.SCALE = 40
        self.LIMITES = [30, 18]
        self.surface = pygame.display.set_mode([self.LIMITES[0] * self.SCALE, self.LIMITES[1] * self.SCALE])
        pygame.display.set_caption('SplatULg')
        self.environnement = str()
        self.ending = False
        self.imageBlock = list()
        self.level = list()
        self.player = list()
        self.carte = object()
        pygame.display.flip()

    """
    "
    " Demarrage du jeu: initialisations des blocks joueurs et levels
    "
    """

    def start(self):
        self.environnement = 'menu'
        self.initblocks()
        self.initlevels()
        self.initcarte()
        self.initplayers()
        while not self.ending:
            if self.environnement == 'menu':
                self.showmenu()

            if self.environnement == 'playing':
                self.play()

            self.eventlistener()
            self.time.tick(self.FPS)

        pygame.display.quit()
        pygame.quit()
        exit()

    def showmenu(self):
        menu = list()

        menu.append(pygame.image.load('./menu/main.png').convert())
        menu[0] = pygame.transform.scale(menu[0], (self.LIMITES[0] * self.SCALE, self.LIMITES[1] * self.SCALE))

        menu.append(pygame.image.load('./menu/mainanim.png').convert())
        menu[1] = pygame.transform.scale(menu[1], (self.LIMITES[0] * self.SCALE, self.LIMITES[1] * self.SCALE))

        tmp = 1
        while self.environnement == 'menu' and not self.ending:
            tmp = not tmp
            self.surface.blit(menu[tmp], [0, 0])
            pygame.display.flip()
            self.eventlistener()
            self.time.tick(10)

    def play(self):
        self.dessinecarte()
        self.dessineplayers()
        while self.environnement == 'playing' and not self.ending:
            self.player[0].diminuepenalite()
            self.player[1].diminuepenalite()
            self.eventlistener()
            self.time.tick(60)

    """
    "
    " Verifie les entrées au clavier
    "
    """

    def eventlistener(self):
        for evenement in pygame.event.get():
            if self.environnement == "menu":
                if evenement.type == pygame.QUIT:
                    if evenement.type == pygame.QUIT:
                        self.ending = True
                if evenement.type == pygame.MOUSEBUTTONDOWN:
                    self.environnement = 'playing'

            if self.environnement == "playing":
                if evenement.type == pygame.QUIT:
                    self.environnement = 'menu'
                if evenement.type == pygame.KEYDOWN:
                    if evenement.key == pygame.K_z:
                        self.player[0].deplacer('UP')
                    if evenement.key == pygame.K_d:
                        self.player[0].deplacer('RIGHT')
                    if evenement.key == pygame.K_s:
                        self.player[0].deplacer('DOWN')
                    if evenement.key == pygame.K_q:
                        self.player[0].deplacer('LEFT')
                    if evenement.key == pygame.K_UP:
                        self.player[1].deplacer('UP')
                    if evenement.key == pygame.K_RIGHT:
                        self.player[1].deplacer('RIGHT')
                    if evenement.key == pygame.K_DOWN:
                        self.player[1].deplacer('DOWN')
                    if evenement.key == pygame.K_LEFT:
                        self.player[1].deplacer('LEFT')

    """
    "
    " initialisation des differents blocks
    "
    """

    def initblocks(self):
        self.imageBlock.append(ImageBlock("0", False))
        self.imageBlock.append(ImageBlock("1", False))
        self.imageBlock.append(ImageBlock("2", False))
        self.imageBlock.append(ImageBlock("3", True))
        self.imageBlock.append(ImageBlock("4", True))
        self.imageBlock.append(ImageBlock("5", True))
        self.imageBlock.append(ImageBlock("6", True))
        self.imageBlock.append(ImageBlock("7", True))
        self.imageBlock.append(ImageBlock("8", True))
        self.imageBlock.append(ImageBlock("9", True))
        self.imageBlock.append(ImageBlock("10", True))
        self.imageBlock.append(ImageBlock("11", True))
        self.imageBlock.append(ImageBlock("12", True))
        self.imageBlock.append(ImageBlock("13", True))
        self.imageBlock.append(ImageBlock("14", True))
        self.imageBlock.append(ImageBlock("15", True))
        self.imageBlock.append(ImageBlock("16", True))
        self.imageBlock.append(ImageBlock("17", True))

    """
    "
    " initialisation des joureurs
    "
    """

    def initplayers(self):
        self.player.append(Personnage(1, [[0], [1, 1]], 2))
        self.player.append(Personnage(2, [[0], [28, 16]], 2))

    def dessineplayers(self):
        self.player[0].dessine()
        self.player[1].dessine()

    """
    "
    " initalisations des diferents levels
    "
    """

    def initlevels(self):
        self.level.append([
            # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29
            [ 3, 7, 7,12, 0, 0, 0,13, 7,12, 0, 0, 0,13, 7, 7,12, 0, 0, 0,13, 7,12, 0, 0, 0,13, 7, 7, 3],  #0
            [ 6, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],  #1
            [ 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],  #2
            [12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,13],  #3
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  #4
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  #5
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  #6
            [11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,10],  #7
            [ 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],  #8
            [ 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],  #9
            [12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,13],  #10
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  #11
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  #12
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  #13
            [11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,10],  #14
            [ 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],  #15
            [ 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 4],  #16
            [ 3, 5, 5,11, 0, 0, 0,10, 5,11, 0, 0, 0,10, 5, 5,11, 0, 0, 0,10, 5,11, 0, 0, 0,10, 5, 5, 3]   #17
            ]
        )
        self.level.append([
            # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29
            [ 3, 7, 7,12, 0,17, 0,13, 7,12, 0, 9, 0,13, 7, 7,12, 0, 9, 0,13, 7,12, 0,17, 0,13, 7, 7, 3],  #0
            [ 6, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],  #1
            [ 6, 0,10,11, 0, 0,10,11, 0, 0, 0,17, 0, 0, 0, 0, 0, 0,17, 0, 0, 0,10,11, 0, 0,10,11, 0, 4],  #2
            [12, 0, 4, 6, 0, 0, 4, 6, 0, 0, 0, 0, 0,14, 8, 8,16, 0, 0, 0, 0, 0, 4, 6, 0, 0, 4, 6, 0,13],  #3
            [ 0, 0, 4, 6, 0, 0, 4, 6, 0,10, 5,11, 0, 0, 0, 0, 0, 0,10, 5,11, 0, 4, 6, 0, 0, 4, 6, 0, 0],  #4
            [16, 0, 4, 6, 0, 0, 4, 6, 0, 4, 3, 6, 0,10, 8, 8,11, 0, 4, 3, 6, 0, 4, 6, 0, 0, 4, 6, 0,14],  #5
            [ 0, 0, 4, 6, 0, 0, 4, 6, 0,13, 7,12, 0,17, 0, 0,17, 0,13, 7,12, 0, 4, 6, 0, 0, 4, 6, 0, 0],  #6
            [11, 0, 4, 6, 0, 0,13,12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,13,12, 0, 0, 4, 6, 0,10],  #7
            [ 6, 0, 4, 6, 0, 0, 0, 0, 0,10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,11, 0, 0, 0, 0, 0, 4, 6, 0, 4],  #8
            [ 6, 0, 4, 6, 0, 0, 0, 0, 0,13, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,12, 0, 0, 0, 0, 0, 4, 6, 0, 4],  #9
            [12, 0, 4, 6, 0, 0,10,11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,10,11, 0, 0, 4, 6, 0,13],  #10
            [ 0, 0, 4, 6, 0, 0, 4, 6, 0,10, 5,11, 0,15, 0, 0,15, 0,10, 5,11, 0, 4, 6, 0, 0, 4, 6, 0, 0],  #11
            [16, 0, 4, 6, 0, 0, 4, 6, 0, 4, 3, 6, 0,13, 8, 8,12, 0, 4, 3, 6, 0, 4, 6, 0, 0, 4, 6, 0,14],  #12
            [ 0, 0, 4, 6, 0, 0, 4, 6, 0,13, 7,12, 0, 0, 0, 0, 0, 0,13, 7,12, 0, 4, 6, 0, 0, 4, 6, 0, 0],  #13
            [11, 0, 4, 6, 0, 0, 4, 6, 0, 0, 0, 0, 0,14, 8, 8,16, 0, 0, 0, 0, 0, 4, 6, 0, 0, 4, 6, 0,10],  #14
            [ 6, 0,13,12, 0, 0,13,12, 0, 0, 0,15, 0, 0, 0, 0, 0, 0,15, 0, 0, 0,13,12, 0, 0,13,12, 0, 4],  #15
            [ 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 4],  #16
            [ 3, 5, 5,11, 0,15, 0,10, 5,11, 0, 9, 0,10, 5, 5,11, 0, 9, 0,10, 5,11, 0,15, 0,10, 5, 5, 3]   #17
            ]
        )
        self.level.append([
            # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29
            [ 3, 7, 7,12, 0, 0, 0,13, 7,12, 0, 0, 0,13, 7, 7,12, 0, 0, 0,13, 7,12, 0, 0, 0,13, 7, 7, 3],  #0
            [ 6, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],  #1
            [ 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],  #2
            [12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,13],  #3
            [ 0, 0, 0, 0,10, 5,11, 0, 0, 0,10, 5,11, 0, 0, 0, 0,10, 5,11, 0, 0, 0,10, 5,11, 0, 0, 0, 0],  #4
            [ 0, 0, 0, 0, 4, 3, 6, 0, 0, 0, 4, 3, 6, 0, 0, 0, 0, 4, 3, 6, 0, 0, 0, 4, 3, 6, 0, 0, 0, 0],  #5
            [ 0, 0, 0, 0,13, 7,12, 0, 0, 0,13, 7,12, 0, 0, 0, 0,13, 7,12, 0, 0, 0,13, 7,12, 0, 0, 0, 0],  #6
            [11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,10],  #7
            [ 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,10,11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],  #8
            [ 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,13,12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],  #9
            [12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,13],  #10
            [ 0, 0, 0, 0,10, 5,11, 0, 0, 0,10, 5,11, 0, 0, 0, 0,10, 5,11, 0, 0, 0,10, 5,11, 0, 0, 0, 0],  #11
            [ 0, 0, 0, 0, 4, 3, 6, 0, 0, 0, 4, 3, 6, 0, 0, 0, 0, 4, 3, 6, 0, 0, 0, 4, 3, 6, 0, 0, 0, 0],  #12
            [ 0, 0, 0, 0,13, 7,12, 0, 0, 0,13, 7,12, 0, 0, 0, 0,13, 7,12, 0, 0, 0,13, 7,12, 0, 0, 0, 0],  #13
            [11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,10],  #14
            [ 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],  #15
            [ 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 4],  #16
            [ 3, 5, 5,11, 0, 0, 0,10, 5,11, 0, 0, 0,10, 5, 5,11, 0, 0, 0,10, 5,11, 0, 0, 0,10, 5, 5, 3]   #17
            ]
        )
        self.level.append([
            # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29
            [ 3, 7, 7, 7,12, 0,13, 7, 3, 7,12, 0,13, 7, 3, 3, 7,12, 0,13, 7, 3, 7,12, 0,13, 7, 7, 7, 3],  #0
            [ 6, 1, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 4, 6, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 4],  #1
            [ 6, 0,10,11, 0,14,16, 0, 9, 0,14, 5,16, 0, 4, 6, 0,14, 5,16, 0, 9, 0,14,16, 0,10,11, 0, 4],  #2
            [ 6, 0,13,12, 0, 0, 0, 0, 9, 0, 0, 9, 0, 0, 4, 6, 0, 0, 9, 0, 0, 9, 0, 0, 0, 0,13,12, 0, 4],  #3
            [12, 0, 0, 0,14, 8,11, 0, 9, 0,10, 7,16, 0,13,12, 0,14, 7,16, 0, 9, 0,10, 8,16, 0, 0, 0,13],  #4
            [ 0, 0,15, 0, 0, 0, 9, 0, 9, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 9, 0, 0, 0,15, 0, 0],  #5
            [11, 0,13, 8,11, 0, 9, 0,17, 0,13, 8, 8,11, 0,10, 8,11, 0,15, 0,17, 0, 9, 0,10, 8,12, 0,10],  #6
            [ 6, 0, 0, 0, 9, 0,17, 0, 0, 0, 0, 0, 0,17, 0, 9, 0, 9, 0,13,16, 0, 0, 9, 0, 9, 0, 0, 0, 4],  #7
            [ 3, 5,11, 0, 9, 0, 0, 0,14, 8, 8, 8,11, 0, 0,17, 0, 9, 0, 0, 0, 0,14,12, 0, 9, 0,10, 5, 3],  #8
            [ 3, 7,12, 0, 9, 0,10,16, 0, 0, 0, 0, 9, 0,15, 0, 0,13, 8, 8, 8,16, 0, 0, 0, 9, 0,13, 7, 3],  #9
            [ 6, 0, 0, 0, 9, 0, 9, 0, 0,14,11, 0, 9, 0, 9, 0,15, 0, 0, 0, 0, 0, 0,15, 0, 9, 0, 0, 0, 4],  #10
            [12, 0,10, 8,12, 0, 9, 0,15, 0,17, 0,13, 8,12, 0,13, 8, 8,11, 0,15, 0, 9, 0,13, 8,11, 0,13],  #11
            [ 0, 0,17, 0, 0, 0, 9, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 9, 0, 9, 0, 0, 0,17, 0, 0],  #12
            [11, 0, 0, 0,14, 8,12, 0, 9, 0,14, 5,16, 0,10,11, 0,14, 5,12, 0, 9, 0,13, 8,16, 0, 0, 0,10],  #13
            [ 6, 0,10,11, 0, 0, 0, 0, 9, 0, 0, 9, 0, 0, 4, 6, 0, 0, 9, 0, 0, 9, 0, 0, 0, 0,10,11, 0, 4],  #14
            [ 6, 0,13,12, 0,14,16, 0, 9, 0,14, 7,16, 0, 4, 6, 0,14, 7,16, 0, 9, 0,14,16, 0,13,12, 0, 4],  #15
            [ 6, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 4, 6, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 2, 4],  #16
            [ 3, 5, 5, 5,11, 0,10, 5, 3, 5,11, 0,10, 5, 3, 3, 5,11, 0,10, 5, 3, 5,11, 0,10, 5, 5, 5, 3]   #17
            ]
        )

    def initcarte(self):
        self.carte = Carte([])
        self.carte.elements = self.level[1]

    def dessinecarte(self):
        self.carte.affichecarte()


"""
"
" Classe Carte, structure de la carte a l'affichage
"
"""


class Carte:
    def __init__(self, elements):
        self.elements = elements

    """
    "
    " Affichage de la carte
    "
    """

    def affichecarte(self):
        i = 0

        for lines in self.elements:
            j = 0

            for element in lines:
                world.imageBlock[element].dessine([j, i])
                j += 1

            i += 1

        pygame.display.flip()

    """
    "
    " Return l'objet block se trouvant aux coordonnées données
    "
    """

    def quelblock(self, coordonnees):
        return world.imageBlock[self.elements[coordonnees[1]][coordonnees[0]]]

    def coloriecase(self, type, coordonnees):
        self.elements[coordonnees[1]][coordonnees[0]] = type
        world.imageBlock[type].dessine([coordonnees[0], coordonnees[1]])


"""
"
" Class imageBlock: proprietés des blocks differents (obstacles ou pas etc)
"
"""


class ImageBlock:
    def __init__(self, nom, obstacle):
        self.nom = nom
        self.url = './imageBlock/' + nom + '.png'
        self.obstacle = obstacle
        self.surface = pygame.image.load(self.url).convert()
        self.surface = pygame.transform.scale(self.surface, (world.SCALE, world.SCALE))

    """
    "
    " Dessine le block sur la carte par rapport aux coordonnées données
    "
    """

    def dessine(self, coordonees):
        world.surface.blit(self.surface, [coordonees[0] * world.SCALE, coordonees[1] * world.SCALE])


"""
"
" Class Personnage: Personnage et leur proprietés
"
"""


class Personnage:
    def __init__(self, nom, position, pose):
        self.nom = nom
        self.url = './personnageBlock/' + str(nom) + '/'
        self.position = position
        self.pose = pose
        self.surface = list()
        self.penalite = 0

        for pose in ['TOP', 'RIGHT', 'DOWN', 'LEFT', 'DEAD']:
            self.surface.append(
                pygame.transform.scale(
                    pygame.image.load(self.url + pose + '.png'),
                    (world.SCALE, world.SCALE)
                )
            )
        self.dessine()

    """
    "
    " Renvoi le type d'element (block) se trouvant a sa position
    "
    """

    def caseactuel(self):
        return world.carte.elements[self.position[1][1]][self.position[1][0]]

    """
    "
    " Recois la direction du eventlistener et se deplace si il peut se deplacer (verifie les obstacles, les limites de
    " la fenetre et les autres personnages)
    "
    """

    def deplacer(self, evenement):
        if self.penalite == 0:
            world.imageBlock[self.caseactuel()].dessine([self.position[1][0], self.position[1][1]])
            if not self.autrepersonne(evenement):
                if self.obstacle(evenement):
                    if self.nom == 1:
                        self.position[1] = [1, 1]
                        self.mort()
                    if self.nom == 2:
                        self.position[1] = [28, 16]
                        self.mort()
                else:
                    if evenement == 'UP':
                        if self.limite(evenement):
                            self.position[1][1] = world.LIMITES[1] - 1
                        else:
                            self.position[1][1] -= 1
                        self.pose = 0
                    if evenement == 'RIGHT':
                        if self.limite(evenement):
                            self.position[1][0] = 0
                        else:
                            self.position[1][0] += 1
                        self.pose = 1
                    if evenement == 'DOWN':
                        if self.limite(evenement):
                            self.position[1][1] = 0
                        else:
                            self.position[1][1] += 1
                        self.pose = 2
                    if evenement == 'LEFT':
                        if self.limite(evenement):
                            self.position[1][0] = world.LIMITES[0] - 1
                        else:
                            self.position[1][0] -= 1
                        self.pose = 3
                world.carte.coloriecase(self.nom, [self.position[1][0], self.position[1][1]])
            self.dessine()

    """
    "
    " Verifie si il depace une limite en se deplacant dans $direction
    "
    """

    def limite(self, direction):
        if direction == 'UP':
            return self.position[1][1] == 0
        if direction == 'RIGHT':
            return self.position[1][0] == world.LIMITES[0] - 1
        if direction == 'DOWN':
            return self.position[1][1] == world.LIMITES[1] - 1
        if direction == 'LEFT':
            return self.position[1][0] == 0

    """
    "
    " Verifie si en se deplacant on se deplace sur un obstacle par rapport a $direction
    "
    """

    def obstacle(self, direction):
        if direction == 'UP':
            return world.carte.quelblock([self.position[1][0], (self.position[1][1] - 1) % world.LIMITES[1]]).obstacle
        if direction == 'RIGHT':
            return world.carte.quelblock([(self.position[1][0] + 1) % world.LIMITES[0], self.position[1][1]]).obstacle
        if direction == 'DOWN':
            return world.carte.quelblock([self.position[1][0], (self.position[1][1] + 1) % world.LIMITES[1]]).obstacle
        if direction == 'LEFT':
            return world.carte.quelblock([(self.position[1][0] - 1) % world.LIMITES[0], self.position[1][1]]).obstacle

    """
    "
    " Verifie si en se deplacant on se deplace sur un autre personnage par rapport a $direction
    "
    """

    def autrepersonne(self, direction):
        if direction == 'UP':
            if self.nom == 1:
                return self.position[1][1] == world.player[1].position[1][1] + 1 and self.position[1][0] == \
                                                                                     world.player[1].position[1][0]
            else:
                return self.position[1][1] == world.player[0].position[1][1] + 1 and self.position[1][0] == \
                                                                                     world.player[0].position[1][0]
        if direction == 'RIGHT':
            if self.nom == 1:
                return self.position[1][0] == world.player[1].position[1][0] - 1 and self.position[1][1] == \
                                                                                     world.player[1].position[1][1]
            else:
                return self.position[1][0] == world.player[0].position[1][0] - 1 and self.position[1][1] == \
                                                                                     world.player[0].position[1][1]
        if direction == 'DOWN':
            if self.nom == 1:
                return self.position[1][1] == world.player[1].position[1][1] - 1 and self.position[1][0] == \
                                                                                     world.player[1].position[1][0]
            else:
                return self.position[1][1] == world.player[0].position[1][1] - 1 and self.position[1][0] == \
                                                                                     world.player[0].position[1][0]
        if direction == 'LEFT':
            if self.nom == 1:
                return self.position[1][0] == world.player[1].position[1][0] + 1 and self.position[1][1] == \
                                                                                     world.player[1].position[1][1]
            else:
                return self.position[1][0] == world.player[0].position[1][0] + 1 and self.position[1][1] == \
                                                                                     world.player[0].position[1][1]

    def mort(self):
        self.penalite = 2 * world.FPS
        self.pose = 4

    def diminuepenalite(self):
        if self.penalite != 0:
            self.penalite -= 1
            if self.penalite == 0:
                self.pose = 2
                self.dessine()

    """
    "
    " Affiche le personnage par rapport a sa postion
    "
    """

    def dessine(self):
        world.surface.blit(self.surface[self.pose],
                           [self.position[1][0] * world.SCALE, self.position[1][1] * world.SCALE])
        pygame.display.flip()


"""
"
" Initialise le monde et demarre
"
"""
world = World()
world.start()
