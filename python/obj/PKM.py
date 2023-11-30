class Monster :
    def __init__(self,nom,type,resistance,actions):
        self.__nom = nom
        self.__type = type
        self.__resis = resistance
        self.__pv = 100
        self.__liste_act = actions

    def dmg(self,dmg):
        degat = dmg + self.__resis
        if (degat > 0):
            degat = 0
        self.__pv += degat
        if(self.__pv < 0):
            self.__pv = 0

    def get_nom(self):
        return self.__nom
    def get_type(self):
        return self.__type
    def get_resistance(self):
        return self.__resis
    def get_liste_act(self,nmb):
        return self.__liste_act[nmb]
    def get_pv(self):
        return self.__pv

class Action : 
    def __init__(self,nom,type,force,utilisations):
        self.__nom = nom
        self.__type = type
        self.__force = force
        self.__use = utilisations

    def get_nom(self):
        return self.__nom
    def get_type(self):
        return self.__type
    def get_force(self):
        return self.__force

def attaque(atk,deff):

    if(deff.get_type() == "FEU" and atk.get_type() == "EAU"):
        print("C'est très efficace")
        return (atk.get_force() * 1,5)*-1
    if(deff.get_type() == "EAU" and atk.get_type() == "PLANTE"):
        print("C'est très efficace")
        return (atk.get_force() * 1,5)*-1
    if(deff.get_type() == "PLANTE" and atk.get_type() == "FEU"):
        print("C'est très efficace")
        return (atk.get_force() * 1,5)*-1
    else:
        return atk.get_force()/-1
    
act_feu = {}
act_eau = {}
act_plante = {}

act_feu[1] = act_eau[1] = act_plante[1] = Action("Charge","NORMAL",10,100)

act_feu[2] = Action("Flamèche","FEU",15,10)
act_feu[3] = Action("Lance-Flamme","FEU",25,3)

act_eau[2] = Action("Bulle d'O","EAU",15,10)
act_eau[3] = Action("Cascade","EAU",25,3)

act_plante[2] = Action("Coup' Coup'","PLANTE",15,10)
act_plante[3] = Action("Fouet Ronce'","PLANTE",25,3)


salapeche = Monster("Salapeche","FEU",10,act_feu)
bulbisaure = Monster("bulbisaure","PLANTE",1,act_plante)

print(bulbisaure.get_pv())

print(salapeche.get_liste_act(2).get_nom())
bulbisaure.dmg(attaque(salapeche.get_liste_act(1),bulbisaure))

print(bulbisaure.get_pv())