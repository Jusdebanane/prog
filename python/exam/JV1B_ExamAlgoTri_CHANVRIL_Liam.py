#1

myTable =[2,5,1,3,4]

print(myTable)

def switch(tableau,index1,index2):
    save = tableau[index1]
    tableau[index1] = tableau[index2]
    tableau[index2] = save

switch(myTable,1,2)

print(myTable)
print("\n")


#2

print(myTable)

for i in range(len(myTable)-1):
    if(myTable[i]>myTable[i+1]):
        switch(myTable,i,(i+1))

print(myTable)
print("\n")

#3

myTable = [2,0,4,1,5,3]

print(myTable)

for i in range(len(myTable)-1):
    for j in range(len(myTable)-1):
        if(myTable[j]>myTable[j+1]):
            cswitch(myTable,j,(j+1))

print(myTable)
print("\n")

#upgrade
#1

myTable = [2,0,4,1,5,3]

print(myTable)

for i in range(len(myTable)-1):
    for j in range(len(myTable)-1-i):
        if(myTable[j]>myTable[j+1]):
            switch(myTable,j,(j+1))

print(myTable)
print("\n")

#2

nonTrie = True
myTable = [2,0,4,1,5,3]

print(myTable)

while (nonTrie):
    nonTrie = False

    for j in range(len(myTable)-1-i):
        if(myTable[j]>myTable[j+1]):
            switch(myTable,j,(j+1))
            nonTrie = True

print(myTable)
print("\n")