import random

liste_nmb = [1,2,3]
moyenne = 0

for i in range(len(liste_nmb)):
    moyenne += liste_nmb[i]

moyenne /= len(liste_nmb)

print(moyenne)

################################################################################

liste_rdm_nmb = []

for j in range(10):
    liste_rdm_nmb.append(random.randint(0,10))

print(liste_rdm_nmb)

################################################################################

liste_rdm_nmb = []
moyenne = 0

nmb = int(input("Saississez le nombre de case du tableau :"))

for k in range(nmb):
    liste_rdm_nmb.append(random.randint(0,100))

for i in range(len(liste_rdm_nmb)):
    moyenne += liste_rdm_nmb[i]
moyenne /= len(liste_rdm_nmb)

print(liste_rdm_nmb)
print("moyenne :", moyenne)

################################################################################

save = 0
correct_nmb = False

while(correct_nmb == False):
    choix_1 = int(input("Quelle case shouaitez vous échanger? (sasir une seule case !) :"))
    if(choix_1 >= len(liste_rdm_nmb)):
        print("Cette case n'existe pas.\n","(rappel: les index de case commence a 0)")
    else:
        correct_nmb = True

save = liste_rdm_nmb[choix_1]
correct_nmb = False

while(correct_nmb == False):
    choix_2 = int(input("Avec quelle case shouaitez vous échanger? :"))
    if(choix_2 >= len(liste_rdm_nmb)):
        print("Cette case n'existe pas.\n","(rappel: les index de case commence a 0)")
    else:
        correct_nmb = True

liste_rdm_nmb[choix_1] = liste_rdm_nmb[choix_2]
liste_rdm_nmb[choix_2] = save

print(liste_rdm_nmb)

################################################################################

save_pos =[]
found = False

nmb = int(input("Quelle chiffre cherchez vous? :"))

for l in range(len(liste_rdm_nmb)):
    if(nmb == liste_rdm_nmb[l]):
        save_pos.append(l)
        found = True

if(found == True):
    print("Il est dans la case",end = " ")
    for m in range(len(save_pos)):
        if(m >0 ):
            print("/",end = " ")
        print(save_pos[m], end =" ")
else:
    print("il n'est pas dans le tableau.")

print("\n")
################################################################################

nmb_petit = 0
save = 0
indice = 0

for n in range(1,len(liste_rdm_nmb)):
    nmb_petit = liste_rdm_nmb[n-1]
    for o in range(n,len(liste_rdm_nmb)):
        if(liste_rdm_nmb[o]< nmb_petit):
            nmb_petit = liste_rdm_nmb[o]
            indice = o
    if(nmb_petit != liste_rdm_nmb[n-1]):
        save = liste_rdm_nmb[n-1]
        liste_rdm_nmb[n-1] = nmb_petit
        liste_rdm_nmb[indice] = save

print(liste_rdm_nmb)
