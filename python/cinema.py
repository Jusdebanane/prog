prix_total = 0
popcorn = False

age = int(input("Quel age as tu?: "))

if (age >=18):
    prix_total += 12
else:
    prix_total += 7

choix = int(input("Voulez vous du popcorn? 1: oui / 2: non    : "))
if(choix == 1):
    popcorn = True
    prix_total += 5

print(prix_total ,"euros")


