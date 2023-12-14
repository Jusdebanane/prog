import colorama
import os

colorama.init(autoreset=True)
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

mot = 'AHUV'
guess_list =[]

victoire = False
tour = 0

def check(mot,guess):
    oui = []
    final = ''
    for i in range (len(guess)):
        if (guess[i] in mot):
            if (mot[i] == guess[i]):
                oui.append(colorama.Fore.GREEN + guess[i])
            else:
                oui.append(colorama.Fore.YELLOW + guess[i])
        else:
            oui.append(colorama.Fore.RED + guess[i])
        
    for j in range (len(oui)):
        final += oui[j]
    
    guess_list.append(final)
def affiche_guess():
    for i in range (len(guess_list)):
        print (guess_list[i])
def check_w(mot,guess):
    if(len(guess) == len(mot)):
        for i in range(len(guess)):
            if guess[i] != mot[i]:
                return False
            
        return True
    else:
        return False

cls()

while(True):
    tour += 1 
    print("RAPPEL --> Nombre de lettre :",len(mot))
    while (True):
        guess_mot = input("Saississez un mot : ")
        if len(guess_mot) <= len(mot):
            break
        else:
            print("Trop de lettre")
    check(mot,guess_mot)

    victoire = check_w(mot,guess_mot)


    cls()
    affiche_guess()
    print("\n")

    if(victoire == True):
        print(colorama.Fore.WHITE + colorama.Back.GREEN + "VICTOIRE !")
        print("Nombre d'essai :", len(guess_list))
        break