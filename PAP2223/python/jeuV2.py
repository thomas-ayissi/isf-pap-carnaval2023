import random

# variable contenant le nom de la personne qui joue

playerName = str(input("Bienvenue, quel est votre nom ?\n"))
print("Bonjour" + " " + playerName + ". " + "Vous pouvez quitter le jeu en entrant un nombre négatif")

# mise en place de la valeur permettant de recommencer une partie
replayGame = "launch"

while replayGame == "launch" or replayGame == "y" or replayGame == "Y":
    secret = random.randint(0, 100)
    print(secret)

    # pour rentrer dans la boucle
    n = 102

    # mise en place du compteur
    counter = 1

    while (replayGame != "") and (n != secret):
        n = int(input("Entrez un nombre \n"))
        if (n < secret) and (n >= 0):
            counter = counter + 1
            print("Le nombre est trop petit")

        elif (n > secret) and (n >= 0):
            counter = counter + 1
            print("Le nombre est trop grand")

        elif (n != secret) and (n < 0):
            print("{}, tu as fait {} essais avant de choisir de quitter le jeu. Dommage a la prochaine fois" .format(playerName, counter))
            exit()

        else:
            print("Bravo {}, tu as trouve le nombre {} en {} coups".format(playerName, secret, counter))
            replayGame = str(input("Tapez « Y » ou « y » pour refaire une partie sinon le jeu s’arrête\n"))

else:
 print("C etait super {}, A la prochaine fois".format(playerName))
