mot1 = "bonjour"
listemot = []
motfinal =" "
win = False

def check(mot1,mot2):
    for i in range(len(mot1)):
        if(mot2[i] != mot1[i]):
            return False

for i in range(len(mot1)):
    listemot.append("*")

for i in range(len(listemot)):
    motfinal += listemot[i]



while(win == False):
    print(motfinal)
    choix = input("saississez un caractère: ")

    for i in range(len(mot1)):
        if(choix == mot1[i]):
            listemot[i] = choix

    win = True