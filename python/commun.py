

def switch(tableau,index1,index2):
    save = tableau[index1]
    tableau[index1] = tableau[index2]
    tableau[index2] = save

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

def cesar(mot,clé):
    a = 0
    code = ''

    for i in range(len(mot)):
       a = (ord(mot[i]))
       a += clé
       code += chr(a)
       
    print(code) 