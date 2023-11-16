mot1 = "bonjour"
listemot = []
motfinal ="bonjour"
liste_lettres= []
erreurs = 0

def check(mot,lettre):
    for i in range(len(mot)):
        if(lettre == mot[i]):
            listemot[i] = choix
    
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
    
def pendu(nmb):
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


for i in range(len(mot1)):
    listemot.append("*")
for i in range(len(listemot)):
    motfinal += listemot[i]


while(True):

    print(motfinal)
    pendu(erreurs)
    print("lettres essayées :",liste_lettres)
    choix = input("saississez un caractère: ")
    
    check(mot1,choix)
    erreurs += failcheck(mot1,choix)

    motfinal = " "   
    for i in range(len(listemot)):
        motfinal += listemot[i]
    
    if("*" not in motfinal):
        print("VOUS AVEZ GAGNE")
        break

    if(erreurs == 8):
        print("LOSE")
        pendu(erreurs)
        break


