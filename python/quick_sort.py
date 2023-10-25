#a ameliorer !

import random
array = [10,80,30,90,40]
trie = False

def swap(tableau,index1,index2):
    save = tableau[index1]
    tableau[index1] = tableau[index2]
    tableau[index2] = save