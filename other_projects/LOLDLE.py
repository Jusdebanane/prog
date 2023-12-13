import random
import colorama

class Champion :
    def __init__(self,nom,genre,role,espece,ressource,portee,regions,sortie):
        self.__nom = nom
        self.__genre = genre
        self.__role = role
        self.__espece = espece
        self.__ressource = ressource
        self.__portee = portee
        self.__regions = regions
        self.__sortie = sortie

    def get_nom(self):
        return self.__nom
    def get_genre(self):
        return self.__genre
    def get_role(self): 
        return self.__role
    def get_espece(self):
        return self.__espece
    def get_ressources(self):
        return self.__ressource
    def get_portee(self):
        return self.__portee
    def get_regions(self):
        return self.__regions
    def get_sortie(self):
        return self.__sortie
    


