import random
secret = random.randint(0,100)
#print(secret)
n=102 #pour rentrer dans la boucle
while n != secret:
    n= int(input("Entrez un nombre \n"))
    if n<secret :
        print("Le nombre est trop petit")
    elif n>secret :
        print("Le nombre est trop grand")
print("Super tu as trouvé !!!")
        