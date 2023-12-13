class Animal:
    def __init__ (self,nom,poids):
        self.__nom = nom
        self.__poids = poids

class Chat(Animal):
    def __init__(self, nom, poids):
        super().__init__(nom, poids)
    