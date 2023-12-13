import os
os.system('cls')

livre = {}

class Chapter:
    def __init__(self,gold,pv,txt,links):
        self.__or = gold
        self.__dmg = pv
        self.__texte = txt
        self.__liens = links
    
    def get_or(self):
        return self.__or
    def get_dmg(self):
        return self.__dmg
    def get_txt(self):
        return self.__texte
    def get_liens(self):
        return self.__liens

class Hero:
    def __init__(self,nom):
        self.__nom = nom
        self.__gold = 100
        self.__pv = 20

    def get_nom(self):
        return self.__nom
    def get_gold(self):
        return self.__gold
    def get_pv(self):
        return self.__pv

    # Affiche les infos du perso
    def affiche(self):
        print(self.__nom,"\nPV:",self.__pv,"\nPO:",self.__gold)

    # Permet de gagner/perdre des PO
    def gagne_gold(self, nmb):

        self.__gold += nmb

        if(nmb < 0):
            print("Vous perdez",nmb,"pièces d'Or.")
        if(nmb > 0):
            print("Vous gagnez",nmb,"pièces d'Or.")

    # Permet de gagner/perdre des PV
    def gagne_pv(self, nmb):
        self.__pv += nmb

        if(nmb < 0):
            print("Vous perdez",nmb*-1,"points de Vie.")
        if(nmb > 0):
            print("Vous gagnez",nmb,"points de Vie.")
        
        if(self.__pv <0) :
            self.__pv = 0

def change_chapter(chapitre):
    liens= chapitre.get_liens()
    while(True):
        print(chapitre.get_liens())
        choix = int(input("Quel chapitre shouaiteriez vous visiter? : "))
        if(choix in liens):
            break
        else:
            print("Vous ne pouvez pas visiter ce chapitre pour l'instant...")
    return choix

livre[0] = Chapter(0,0,"debut de votre aventure \nPrendre la porte en bois: CHAPITRE 1 \nPrendre la porte en argent: CHAPITRE 2 \nPrendre la porte en or: CHAPITRE 3",[1,2,3])
livre[1] = Chapter(100000,0,"chapitre 1 \nVous trouvez le trésor! \n\nVous rendre a la fin : CHAPITRE 4",[4])
livre[2] = Chapter(0,-19,"chapitre 2 \nVous vous faites agresser par un goblin et dans une bataille épique vous triomphez de lui. Cependant vous etes gravement blessé pendant la bataille... \n\nPrendre la porte en bois: CHAPITRE 1 \nPrendre la porte en argent: CHAPITRE 3",[1,3])
livre[3] = Chapter(0,-1000,"chapitre 3 \nVous tombez dans un immense gouffre et mourrez sur le coup... dommage ",[])
livre[4] = Chapter(0,0,"The end.",[])

#CREATION DU PERSO
choix_nom = input("Saississez votre nom: ")
perso = Hero(choix_nom)

victoire = False
en_cours = 0

while(True):
    os.system('cls')

    perso.affiche()
    print("\n")
    print(livre[en_cours].get_txt())

    perso.gagne_gold(livre[en_cours].get_or())
    perso.gagne_pv(livre[en_cours].get_dmg())

    if(perso.get_pv() == 0):
        break

    if(en_cours == 4):
        victoire = True
        break

    en_cours = (change_chapter(livre[en_cours]))

print("\n\n")
if(victoire == True):
    print("BRAVO!\n")
    perso.affiche()
else:
    print("Vous avez succombé aux forces du MAL!\n")
    perso.affiche()