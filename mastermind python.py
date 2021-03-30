from random import * #on importe la librairie random pour pouvoir avoir un code aléatoire


'''on définit la fonction 
   MasterMind niv= nombres de 
   chiffres dans le code 
   coul = chiffre de 1à6'''
def MasterMind(niv= 4, coul = 6) 
    
    #nombre de tentatives qui augmentera au fil des tours
    c = 1 
    secret = [str(randint(1,coul)) for i in range(niv)] #code secret a trouver sous forme de liste String
    #boucle 
    while True : 
        code= list(secret)  #le code a retrouver
        j= list(input("Coup "+ str(c) + " : "))  #le code a retrouver
        if len(j) == 0: return 'PERDU !' + "".join(secret) #si la réponse du joueur est vide = perdu
        c+=1
        bien; mal = 0, 0
        for i, in enumerate(j):
            if v == code[i]: