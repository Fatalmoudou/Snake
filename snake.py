import pygame 
import time
import random

pygame.init()

#couleurs
blanc = (255, 255, 255)
jaune = (255, 255, 102)
noir = (0, 0, 0)
rouge = (213, 50, 80)
vert = (0, 255, 0)
bleu = (50, 153, 213)

# Dimensions de la fenêtre
largeur = 600
hauteur = 400

# Créer la fenêtre de jeu
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption('Snake Game')

# Définir la vitesse du Snake
vitesse_snake = 5
#taille ( épaisseur) du snake et de la pomme
taille_block = 10
horloge = pygame.time.Clock()

# Fontes pour le texte
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def currentScore(score):
    value=score_font.render("Score:" + str(score),True, rouge)
    fenetre.blit(value,[0,0])

def snake(taille_block,snake_list):
    #snake_list est une liste de block
    # chaque block a 2 coordonnées (x,y)=(block[0],block[1])
    for block in snake_list:
        #couleur noiret width=taille et height=taille 
        pygame.draw.rect(fenetre,noir,[block[0],block[1],taille_block,taille_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    fenetre.blit(mesg, [largeur / 15, hauteur / 3])

def game():

    game_over=False
    game_close=False

    #position initiale du snake
    x_snake=largeur/2
    y_snake=hauteur/2

    #changements de position

    x_change=0
    y_change=0

    snake_list=[]
    #taille du snake
    snake_long=1

    #generer la pomme aléatoirement sur l'écran
    x_pomme = round(random.randrange(0, largeur - taille_block) / 10.0) * 10.0
    y_pomme = round(random.randrange(0, hauteur - taille_block) / 10.0) * 10.0

    while not game_over:
        while game_close:
            #couleur de fond
            fenetre.fill(bleu)
            message("Tu as perdu! Appuie sur Q-Quitter ou C-Continuer", rouge)
            currentScore(snake_long - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over=True
                        game_close=False
                    if event.key == pygame.K_c:
                        game()
    
        for event in pygame.event.get():
                if event.type== pygame.QUIT:
                    game_over=True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_change = -taille_block
                        y_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x_change = taille_block
                        y_change = 0
                    elif event.key == pygame.K_UP:
                        y_change = -taille_block
                        x_change = 0
                    elif event.key == pygame.K_DOWN:
                        y_change = taille_block
                        x_change = 0  
            #si les limites de l'ecran sont atteints terminer              
        if x_snake >= largeur or x_snake < 0 or y_snake >= hauteur or y_snake < 0:
                game_close = True

            # Mettre à jour la position du Snake
        x_snake += x_change
        y_snake += y_change
        fenetre.fill(bleu)

        # Dessiner la pomme
        pygame.draw.rect(fenetre, vert, [x_pomme, y_pomme, taille_block, taille_block])

        # Mettre à jour la taille du Snake
        snake_head = []
        snake_head.append(x_snake)
        snake_head.append(y_snake)
        snake_list.append(snake_head)#head = 1 bloque qu'on ajoute à liste

        if len(snake_list) > snake_long:
            del snake_list[0]
        
        # Si le Snake se touche lui-même
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True
        
        snake(taille_block,snake_list)
        currentScore(snake_long-1)

        pygame.display.update()

        if x_snake == x_pomme and y_snake == y_pomme:
            x_pomme = round(random.randrange(0, largeur - taille_block) / 10.0) * 10.0
            y_pomme = round(random.randrange(0, hauteur - taille_block) / 10.0) * 10.0
            snake_long += 1
        horloge.tick(vitesse_snake)
    pygame.quit()

    quit()

game()






            
            