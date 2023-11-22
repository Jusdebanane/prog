inventaire = []

class ITEM : 
    def __init__ (self,nom,qnt,pow):
        self.__nom = nom
        self.__qnt = qnt
        self.__puissance = pow

    def affiche(self):
        print("vous avez",self.__qnt,self.__nom + ".")
        if (self.__puissance > 0):
            print(self.__nom,"est un item curatif.")
        elif (self.__puissance < 0):
            print(self.__nom,"est un item agressif.")

    
    def use(self):
        if(self.__puissance == 0):
            print("Vous ne pouvez pas utiliser",self.__nom,"maintenant.")
        elif (self.__puissance > 0):
            print("Vous utilisez",self.__nom,"sur vous.")
            self.__qnt -= 1
        elif (self.__puissance < 0):
            print("Vous utilisez",self.__nom,"sur votre enemis.")
            self.__qnt -= 1
    
    def ajout_inventaire(self,liste):
        liste.append(self)


potion = ITEM("potion de soin",3,3)
epee = ITEM("epée",1,0)
flechette = ITEM("fléchette",2,-3)

potion.ajout_inventaire(inventaire)
epee.ajout_inventaire(inventaire)
flechette.ajout_inventaire(inventaire)

inventaire[0].affiche()
inventaire[1].affiche()
inventaire[2].affiche()

print("\n")

potion.use()
epee.use()
flechette.use()

print("\n")

potion.affiche()
epee.affiche()
flechette.affiche()