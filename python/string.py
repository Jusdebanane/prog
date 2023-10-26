import commun

choix_mot = input("Choississez un mot : ")
commun.inverse(choix_mot)
commun.consonne(choix_mot)

print("\n")

print("CODE CESAR")
choix_clé = int(input("Choississez une clé (nmb) : ")) 

commun.cesar(choix_mot,choix_clé)