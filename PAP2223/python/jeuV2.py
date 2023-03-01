import random

playerName="" #variable contenant le nom de la personne qui joue

playerName= str(input("Bienvenue, quel est votre nom ?\n"))
print("Bonjour"+ " " + playerName + ". "+ "Vous pouvez quitter le jeu en entrant un nombre négatif")

secret = random.randint(0,100)
#print(secret)
n=102 #pour rentrer dans la boucle

while n != secret:
    n= int(input("Entrez un nombre \n"))

    if ((n<secret) and (n>= 0)) :
        print("Le nombre est trop petit")
    elif ((n>secret) and (n>= 0)) :
        print("Le nombre est trop grand")
    elif ((n!=secret) and (n<0)) :
        print("Dommage … A la prochaine fois")
        exit()
    elif ((n==secret) and (n>= 0)) :
        print("Super tu as trouvé !!!")



