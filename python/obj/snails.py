import random
class Escargot:
    def __init__(self,nom,nmb,motiv):
        self.__nom = nom
        self.__numero = nmb
        self.__motivation = motiv
        self.__distance = 0
    
    def get_nom(self):
        return self.__nom
    def get_look(self):
        return "@"+str(self.__numero)
    def get_motivation(self):
        return self.__motivation
    def get_distance(self):
        return self.__distance
    
    def avance(self):
        self.__distance += self.__motivation
        if(self.__distance > 100):
            self.__distance = 100
        self.__motivation -= random.randint(0,10)
        if (self.__motivation < 0):
            self.__motivation = 0

    def repos(self):
        self.__motivation += random.randint(0,10)

    def affiche_distance(self):
        ligne_print = ""
        ligne = ["-","-","-","-","-","-","-","-","-","-","+"]
        ligne[self.__distance//10] = self.get_look()
        for i in range (len(ligne)):
            ligne_print += ligne[i]
        print(ligne_print)


escargots = {}
nmb = 0
fin = False

escargots[1] = Escargot("Oscar",1,23)
escargots[2] = Escargot("Turbo",2,32)

while(True):
    for i in range (1,len(escargots)+1):
        escargots[i].affiche_distance()

    for i in range(1,len(escargots)+1):
        print(escargots[i].get_nom(),"a",escargots[i].get_motivation(),"points de motivation et a parcouru",escargots[i].get_distance(),"m.")
        
        while(True):
            nmb = int(input("1.Se reposer / 2.Avancer : "))
            if(nmb == 1):
                escargots[i].repos()
                break
            elif(nmb == 2):
                escargots[i].avance()
                break
            else:
                print("Mauvaise réponse")
          
    for i in range (1,len(escargots)+1):
        if(escargots[i].get_distance == 100):
            fin = True
            nmb = i

    if(fin == True):
        break



for i in range (1,len(escargots)+1):
        escargots[i].affiche_distance()
print(escargots[nmb].get_nom,"a gagné !")
            
