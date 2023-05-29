import random as r

pdvJ = 50
pdvE = 50

Nb_Potions = 3

tonTour = True

print("\nDans ce jeu de rôles, vous incarnez un joueur dont le but est de terraser l'ennemi. \n\
Vous commencez chacun avec 50 points de vie. Le 1er à atteindre 0 subit une défaite cuisante.\n\
Le joueur détient 3 potions, lorsqu'il en utilise une, il passe son tour. Que le meilleur gagne !\n")

D = "Souhaitez-vous attaquer ou utiliser une potion ? \n 1: Attaquer ! \n 2: Boire une potion\n"

while pdvJ >= 0 or pdvE >= 0:
    
    while True:
        choix = int(input(D))
        if choix not in range(1,3):
            print("Merci d'entrer un choix (numéro) valide.")
            continue
        else:
            break

    if choix == 1:
        AtkJ = r.randint(5,10)
        pdvE-=AtkJ
        print(f"Vous infligez {AtkJ} points de dégâts à l'ennemi ! Il lui reste {pdvE} points de vie !")
        tonTour = False
        if pdvE <= 0:
            print("Vous avez terrassé l'ennemi ! Gloire à vous ! ")
            break
    elif choix == 2:
        if Nb_Potions == 0:
            print("Vous n'avez plus aucune potion ! ")
            while choix != 1:
                choix = int(input(D))
                if choix != 1:
                    print("Vous n'avez plus de potions ! Vous ne pouvez donc qu'attaquer !.")
                    continue
                else:
                    AtkJ = r.randint(5,10)
                    pdvE-=AtkJ
                    print(f"Vous infligez {AtkJ} points de dégâts à l'ennemi ! Il lui reste {pdvE} points de vie !")
                    if pdvE <= 0:
                         print("Vous avez terrassé l'ennemi ! Gloire à vous ! ")
                         break
                    tonTour = False
        elif Nb_Potions > 0:
            PdvPotion = r.randint(15,50)
            pdvJ+=PdvPotion
            Nb_Potions -= 1
            print(f"Vous buvez une potion qui vous régénère de {PdvPotion} pts ! Votre santé atteint ainsi {pdvJ} pts !\
            \net il vous reste {Nb_Potions}. Vous passez néanmoins votre tour.")
            tonTour = False
    
    if tonTour == False:
        print("\nC'est au tour de l'ennemi !")
        AtkE = r.randint(5,15)
        pdvJ -= AtkE
        print(f"L'ennemi contre-attaque et vous inflige {AtkE} points de dégâts ! Il vous reste {pdvJ} points de vie.")
        if pdvJ <= 0:
            print("L'ennemi vous a anéanti ! Déshonneur sur vous !")
            break
    
    print(f"Points de vie du Joueur : {pdvJ}.\nPoints de vie de l'ennemi : {pdvE} .\n")
    print("-"*50)

