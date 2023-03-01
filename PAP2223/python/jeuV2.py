import random

# variable contenant le nom de la personne qui joue

playerName = str(input("Bienvenue, quel est votre nom ?\n"))
print("Bonjour" + " " + playerName + ". " + "Vous pouvez quitter le jeu en entrant un nombre négatif")

secret = random.randint(0, 100)
print(secret)

# pour rentrer dans la boucle
n = 102

# mise en place du compteur
counter = 1

while n != secret:
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


print("Bravo {}, tu as trouve le nombre {} en {} coups".format(playerName, secret, counter))