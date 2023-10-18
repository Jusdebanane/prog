#1

save = 0
myTable =[2,5,1,3,4]

print(myTable)

save = myTable[2]
myTable[2] = myTable[1]
myTable[1] = save

print(myTable)
print("\n")


#2

print(myTable)

for i in range(len(myTable)-1):
    if(myTable[i]>myTable[i+1]):
        save = myTable[i]
        myTable[i] = myTable[i+1]
        myTable[i+1] = save

print(myTable)
print("\n")

#3

myTable = [2,0,4,1,5,3]

print(myTable)

for i in range(len(myTable)-1):
    for j in range(len(myTable)-1):
        if(myTable[j]>myTable[j+1]):
            save = myTable[j]
            myTable[j] = myTable[j+1]
            myTable[j+1] = save

print(myTable)

#4

#Le tri est bulle est lent puisqu'il doit parcourir plusieur fois le tableau afin d'en comparer tout ses membres et les déplacer a chaque fois.
# Pour un petit tableau comme ici cela n'est pas dérangeant mais pour des tableau plus conséquent, cela multiplie le processus encore et encore 
# ce qui peut utiliser beaucoup de performances. Il doit etre possible de calculer le temps de chaque processus en prenant en compte la vitesse
# calcul du processeur ainsi que le poid en octet du processus.