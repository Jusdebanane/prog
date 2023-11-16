import random

dico = []
fichier = open("pendu.txt")
dico = fichier.read().split(",")

print(dico)

def check(mot,lettre):
    for i in range(len(mot)):
        if(lettre == mot[i]):
            liste_mot[i] = choix
    
def failcheck(mot,lettre):
    if ( lettre in liste_lettres):
        print("deja essayer")
        return +1
    else:
        liste_lettres.append(lettre)
    
    if(lettre in mot):
        return 0
    elif (lettre not in mot):
        print("Reessayez")
        return +1
    
def affiche_pendu(nmb):
    for i in range (nmb):
        if(i == 0):
            print("+-------+")
        if(i == 1):
            print("|       |")
        if(i == 2):
            print("|       O")
        if(i == 3):
            print("|       |")
        if(i == 4):
            print("|        ")
        if(i == 5):
            print("|        ")
        if(i == 6):
            print("|        ")
        if(i == 7):
            print("=========")



mot1 = ""
liste_mot = []
motfinal =""
liste_lettres= []
erreurs = 0


mot1 = dico[random.randint(0,len(dico)-1)]

for i in range(len(mot1)):
    liste_mot.append("*")
for i in range(len(liste_mot)):
    motfinal += liste_mot[i]


while(True):

    print(motfinal)
    affiche_pendu(erreurs)
    print("lettres essayées :",liste_lettres)


    choix = input("saississez un caractère: ")
    check(mot1,choix)
    erreurs += failcheck(mot1,choix)


    motfinal = " "   
    for i in range(len(liste_mot)):
        motfinal += liste_mot[i]
    

    if("*" not in motfinal):
        print("VOUS AVEZ GAGNE")
        break
    if(erreurs == 8):
        print("LOSE")
        affiche_pendu(erreurs)
        break