class Carte:
    def __init__(self,mana_cost,name,txt):
        self.__mana = mana_cost
        self.__nom = name
        self.__description = txt

    def get_mana(self):
        return self.__mana
    def get_nom(self):
        return self.__nom
    def get_description(self):
        return self.__description

class Crystal(Carte):
    def __init__(self,mana_cost,name,txt,value):
        Carte.__init__(self,mana_cost,name,txt)
        self.__valeur = value
    
    def get_valeur(self):
        return self.__valeur

class Blast(Carte):
    def __init__(self,mana_cost,name,txt,value):
        Carte.__init__(self,mana_cost,name,txt)
        self.__valeur = value
    
    def get_valeur(self):
        return self.__valeur 

class Creature(Carte):
    def __init__(self,mana_cost,name,txt,pv,atk):
        Carte.__init__(self,mana_cost,name,txt)
        self.__pv = pv
        self.__atk = atk
    
    def get_pv(self):
        return self.__pv
    
    def get_atk(self):
        return self.__atk

class Mage:
    def __init__(self,name):
        self.__nom = name
        self.__pv = 20
        self.__total_mana = 10
        self.__mana = 0

        self.__main = []
        self.__board = []
        self.__defausse = []
    
    def get_nom(self):
        return self.__nom
    def get_pv(self):
        return self.__pv
    def get_mana(self):
        return self.__mana
    

    def affiche_main(self):
        nom = []
        for i in range (len(self.__main)):
            nom.append(self.__main[i].get_nom())
        
        print(nom)

    def affiche_board(self):
        nom = []
        for i in range (len(self.__board)):
            nom.append(self.__board[i].get_nom())
        
        print(nom)

    def affiche_defausse(self):
        nom = []
        for i in range (len(self.__defausse)):
            nom.append(self.__defausse[i].get_nom())
        
        print(nom)

    def jouer_carte (self, nmb):
        self.__board.append(self.__main[nmb])
        del(self.__main[nmb])

    def mana_regen (self):
        self.__mana = self.__total_mana
        for i in range (len(self.__board)):
            if isinstance(self.__board[i],Crystal):
                self.__mana += self.__board[i].get_valeur()
    
    def atk(self):
        pass