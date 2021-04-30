from random import * #on importe la librairie random pour pouvoir avoir un code aléatoire
from tkinter import *
import tkinter as tk
from tkinter import messagebox 

fenetre = tk.Tk()
fenetre.geometry("500x400")
fenetre.title("Mastermind")


'''on définit la fonction 
   MasterMind niv= nombres de 
   chiffres dans le code 
   coul = chiffre de 1à6'''





def MasterMind():
    print("Vous avez un nombre de 4 chiffre a trouver entre 1 et 6. ATTENTION il peut y avoir des répétitions\n")
    generer_code()
    
def generer_code(niv = 4, coul = 6):
    c = 1
    secret = []
    for i in range(niv):
        if i not in secret:
            secret.append(str(randint(1,coul)))
    while True : 
        code= list(secret)  #le code a retrouver
        j= list(input("Coup "+ str(c) + " : "))#le code a retrouver
        if len(j) == 0:
            print('PERDU ! ' + "".join(secret))
            break
        c+=1
        bien, mal = 0, 0
        for i, v in enumerate(j):
            if v == code[i]:
                bien += 1 
                j[i] = "#"
                code[i] = "*"
        if bien == 4:
            print("GAGNE ! Tu es vraiment un MASTERMIND")
        for i,v in enumerate(j):
            if v in code:
                mal += 1
                code[code.index(v)] = "*"
        print("Bien: {}, Mal: {}".format(bien,mal))
        


def MasterMind3(): 
    print("Vous avez un nombre de 7 chiffre a trouver entre 1 et 9. ATTENTION il peut y avoir des répétitions\n")
    generer_code2()
    
def generer_code2(niv= 7, coul = 9):
    c = 1
    secret = []
    for i in range(niv):
        if i not in secret:
            secret.append(str(randint(1,coul)))
    '''secret = [str(randint(1,coul)) for i in range(niv)]''' #code secret a trouver sous forme de liste String
    #boucle 
    while True : 
        code= list(secret)  #le code a retrouver
        j= list(input("Coup "+ str(c) + " : "))#le code a retrouver
        if len(j) == 0:
            print('PERDU ! ' + "".join(secret))
            break #si la réponse du joueur est vide = perdu
        c+=1
        bien, mal = 0, 0
        for i, v in enumerate(j):
            if v == code[i]:
                bien += 1
                j[i] = "#"
                code[i] = "*"
        if bien == 7:
            print("GAGNE ! Tu es vraiment un MASTERMIND")
            break
        for i,v in enumerate(j):
            if v in code:
                mal += 1
                code[code.index(v)] = "*"
        print("Bien: {}, Mal: {}".format(bien,mal))

def quitter_logiciel():
    fenetre.destroy()

def a_propos():
    mon_message = messagebox.showinfo("Jeu mastermind sur tkinter version 1.0", "Le Mastermind ou Master Mind est un jeu de société pour deux joueurs dont le but est de trouver un code. C'est un jeu de réflexion, et de déduction, inventé par Mordecai Meirowitz dans les années 1970 alors qu'il travaillait comme expert en télécommunications. Au départ, il est édité par Capiépa1. Le but du jeu consiste a retrouver un code de quatre ou cinq couleurs. Le jeu suivant est une recréation simple allant de 1à9 couleurs représentés par des chiffres")
    
barremenu = Menu(fenetre)
fenetre.config(menu = barremenu)

fichier_menu = Menu(barremenu, tearoff = 0)
barremenu.add_cascade(label = "Fichier", menu = fichier_menu)
fichier_menu.add_separator()
fichier_menu.add_command(label = "Quitter le logiciel", command = quitter_logiciel)

edition_menu = Menu(barremenu, tearoff = 0)
barremenu.add_cascade(label = "Edition 1.0", menu = edition_menu)

apropos = Menu(barremenu, tearoff = 0)
barremenu.add_cascade(label = "A propos", menu = apropos)
apropos.add_command(label = "Mastermind", command = a_propos)

b1 = Button(fenetre, text ='mode Facile', command =MasterMind)
b1.pack(side =TOP, padx =3, pady =3)


b3 = Button(fenetre, text ='mode Difficile', command =MasterMind3)
b3.pack(side =TOP, padx =11, pady =11)

'''b4 = Button(fenetre, text='quitter', command = fenetre.destroy)
b4.pack(side =TOP, padx =15, pady =15)'''

fenetre.mainloop()