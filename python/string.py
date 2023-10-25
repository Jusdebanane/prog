def inverse(mot):
    a = ''
    for i in range (len(mot)):
        a += mot[(len(mot)-1)-i]
    print(a)

def consonne(mot):
    voyelle = 0
    consonne = len(mot)
    for i in range (len(mot)):
        if(mot[i] == 'a' or mot[i] ==  'e' or mot[i] ==  'i' or mot[i] ==  'o' or mot[i] ==  'u' or mot[i] ==  'y'):
            voyelle += 1 
    
    consonne -= voyelle
    print("il y a",consonne,"consonnes")

def code(mot,clé):
    ord_mot = []
    chr_mot = []
    b = ''
    for j in range (len(mot)):
        ord_mot.append(ord(mot[j]+clé))
    
    for k in range (len(ord)):
        chr_mot.append(chr(ord_mot[k]))
    
    for i in range (len(mot)):
        b += mot[i]
    print(b)

choix = input("Choississez un mot : ")

inverse(choix)
consonne(choix)
code(choix,7)

