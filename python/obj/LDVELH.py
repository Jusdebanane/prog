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
            print("Vous perdez",nmb,"points de Vie.")
        if(nmb > 0):
            print("Vous gagnez",nmb,"points de Vie.")
        
        if(self.__pv <0) :
            self.__pv = 0

#CREATION DU PERSO
choix_nom = input("Saississez votre nom: ")
perso = Hero(choix_nom)

perso.affiche()