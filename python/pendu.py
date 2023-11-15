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
    if(lettre not in liste_lettres):
        liste_lettres.append(lettre)
    
    elif (lettre not in mot):
        print("Reessayez")
        return +1
    
    if ( lettre in liste_lettres):
        print("deja essayer")
        return +1
    
    
    
    
   





for i in range(len(mot1)):
    listemot.append("*")

for i in range(len(listemot)):
    motfinal += listemot[i]


while(True):

    print(motfinal)
    print(erreurs)
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
        break


