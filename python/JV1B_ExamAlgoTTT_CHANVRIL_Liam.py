grid = ["1","2","3","4","5","6","7","8","9"]
player = "X"
victoire = False
turn = 0

def print_grid(tableau):
    for i in range(9):
        print(tableau[i],end =" ")
        if(i == 2 or i == 5):
            print("\n")
            print("-----------")
        elif(i != 8):
            print("|",end = " ")
    print("\n")

def play(player):
    peux_jouer = False
    choix_correct = False
    print("C'est à",player,"de jouer")

    while(peux_jouer == False):
        while(choix_correct == False):
            choix = int(input("Quelle case choississez vous? (1-9) :"))
            if(choix <=9 and choix >= 1):
                choix_correct = True
            else:
                print("Cette case n'existe pas")

        if(grid[choix-1] != "X" and grid[choix-1] != "O" ):
            grid[choix-1] = player
            peux_jouer = True
            
        else:
            print("La case est déjà occupée.")

def verif_h(grid):
    if(grid[0]==grid[1]==grid[2] or grid[3]==grid[4]==grid[5] or grid[6]==grid[7]==grid[8]): 
        return True
    else:
        return False
    
def verif_v(grid):
    if(grid[0]==grid[3]==grid[6] or grid[1]==grid[4]==grid[7] or grid[2]==grid[5]==grid[8]): 
        return True
    else:
        return False
    
def verif_d(grid):
    if(grid[0]==grid[4]==grid[8] or grid[2]==grid[4]==grid[6]): 
        return True
    else:
        return False

while(victoire == False and turn <=8):

    print_grid(grid)
    play(player)

    if(verif_h(grid) == True or verif_v(grid) == True or verif_d(grid) == True):
        victoire = True
        
    if(victoire == False):
        if(player == "X"):
            player = "O"
        else:
            player = "X"

    turn +=1

    print("\n")

if(victoire == True):
    print(player,"a gagné !!!")
else:
    print("égalité !!!")
print_grid(grid)
