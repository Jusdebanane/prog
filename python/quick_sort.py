#ne fonctionne pas !!!

import random
liste = []


def swap(tableau,index1,index2):
    save = tableau[index1]
    tableau[index1] = tableau[index2]
    tableau[index2] = save

def part(tableau,first,last,pivot):
    swap(tableau,pivot,last)

    j = first

    for i in range(first,(last-1)):
        if(tableau[i] <= tableau[last]):
            swap(tableau,i,j)
            j += 1
    
    swap(tableau,last,j)
    return j

def quick_sort(tableau,first,last):
    if(first < last):

        pivot = first
        part(tableau,first,last,pivot)

        quick_sort(tableau,first,(pivot-1))
        quick_sort(tableau,(pivot+1),last)

for i in range (16):
    liste.append(random.randint(0,100))

print(liste)

quick_sort(liste,0,15)

print(liste)