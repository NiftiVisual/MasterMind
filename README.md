# MasterMind

## Description : 

Le Mastermind ou Master Mind est un jeu de société pour deux joueurs dont le but est de trouver un code. C'est un jeu de réflexion, et de déduction, inventé par Mordecai Meirowitz dans les années 1970 alors qu'il travaillait comme expert en télécommunications. Au départ, il est édité par Capiépa1. Le but du jeu consiste a retrouver un code de quatre ou cinq couleurs 

## Solutions retenues :

Listes aléatoires avec : 
```python
[str(randint(1,coul)) for i in range(niv)]
```

Enumérer des listes avec :
```python
for i, v in enumerate(j):
            if v == code[i]:
                bien += 1
                j[i] = "#"
                code[i] = "*"
                
```

Faire en sorte que le code ne contient pas de doublons du même chiffre.
```python
def MasterMind(niv= 4, coul = 6): 
    
    #nombre de tentatives qui augmentera au fil des tours
    c = 1
    secret = []
    for i in range(niv):
        if i not in secret:
            secret.append(str(randint(1,coul)))
```
## Cahier journal :

### Avant Mars :

Après recherche d'aide sur internet, je suis tombé sur un code python que j'ai modifié pour pouvoir avoir un code plus court et plus facile a trouver car je ne pose pas de limite de coups pour le joueur. Le voici :

``` python
from random import * #on importe la librairie random pour pouvoir avoir un code aléatoire


'''on définit la fonction 
   MasterMind niv= nombres de 
   chiffres dans le code 
   coul = chiffre de 1à6'''
def MasterMind(niv= 4, coul = 6): 
    
    #nombre de tentatives qui augmentera au fil des tours
    c = 1 
    secret = [str(randint(1,coul)) for i in range(niv)] #code secret a trouver sous forme de liste String
    #boucle 
    while True : 
        code= list(secret)  #le code a retrouver
        j= list(input("Coup "+ str(c) + " : "))  #le code a retrouver
        if len(j) == 0: return 'PERDU !' + "".join(secret) #si la réponse du joueur est vide = perdu
        c+=1
        bien, mal = 0, 0
        for i, v in enumerate(j):
            if v == code[i]:
                bien += 1
                j[i] = "#"
                code[i] = "*"
        if bien == 4: return "GAGNE ! Tu es vraiment un MASTERMIND"
        for i,v in enumerate(j):
            if v in code:
                mal += 1
                code[code.index(v)] = "*"
        print("Bien: {}, Mal: {}".format(bien,mal))
```
```python
from random import * #on importe la librairie random pour pouvoir avoir un code aléatoire


'''on définit la fonction 
   MasterMind niv= nombres de 
   chiffres dans le code 
   coul = chiffre de 1à6'''
def MasterMind(niv= 4, coul = 6): 
    
    #nombre de tentatives qui augmentera au fil des tours
    c = 1
    secret = []
    for i in range(niv):
        if i not in secret:
            secret.append(str(randint(1,coul)))
    '''secret = [str(randint(1,coul)) for i in range(niv)]''' #code secret a trouver sous forme de liste String
    #boucle 
    while True : 
        code= list(secret)  #le code a retrouver
        j= list(input("Coup "+ str(c) + " : "))  #le code a retrouver
        if len(j) == 0: return 'PERDU !' + "".join(secret) #si la réponse du joueur est vide = perdu
        c+=1
        bien, mal = 0, 0
        for i, v in enumerate(j):
            if v == code[i]:
                bien += 1
                j[i] = "#"
                code[i] = "*"
        if bien == 4: return "GAGNE ! Tu es vraiment un MASTERMIND"
        for i,v in enumerate(j):
            if v in code:
                mal += 1
                code[code.index(v)] = "*"
        print("Bien: {}, Mal: {}".format(bien,mal))
```
code après le réglage du beug des doublons.       

PLusieures recherches ont été faites pour comprendre l'utilisation de la fonction enumerate permettant d'énumérer des objets itérables c'est a dire qui se trouvent dans une liste, ainsi que comment créer une liste aléatoire. On notera cependant un bug (?) faisant que la liste peut contenir des chiffres en double, c'est l'une des raison pour laquelle le nombre de tentatives est illimité, le code devenant beaucoup plus dur a trouver.



### Mars 2021 : 

Changement total de but pour le projet et passage sur tkinter, apprentissage des bases et tentative de réaliser le plateau de jeu ainsi que le menu.

``` python
from tkinter import *

window = Tk()

window.title("Test")
window.geometry("500x400")
window.minsize(480, 360)
window.maxsize(600, 750)
window.config(background='#cae4fa')
can = Canvas(window,bg='grey', height=750, width=600)
can.pack(side=LEFT)
can.create_line(0,0,0,320,fill='black')
can.create_line(60,0,60,320,fill='black')
can.create_line(120,0,120,320,fill='black')
can.create_line(180,0,180,320,fill='black')
can.create_line(240,0,240,320,fill='black')
can.create_line(0,0,240,0,fill='black')
can.create_line(0,53,240,53,fill='black')
can.create_line(0,106,240,106,fill='black')
can.create_line(0,160,240,160,fill='black')
can.create_line(0,213,240,213,fill='black')
can.create_line(0,266,240,266,fill='black')
can.create_line(0,320,240,320,fill='black')


 
    
def vérifier():
    global bon, bienPlace, choix, NB_RENDU
    bon=0
    bienPlace=0

    
window.mainloop()
```

### Mercredi 14 avril :

Changement de code tkinter et ajout d'un nouveau canvas avec une grille

```python
from tkinter import *
from tkinter import messagebox 
import tkinter as tk

window = tk.Tk()

window.title("Test")
window.geometry("500x400")
window.minsize(480, 360)
window.maxsize(502, 734)
window.title("Mastermind")
can1=Canvas(window, width=600, height=750, bg="ivory")
can1.pack(padx=50, pady=50)

'''
btn = Button(window, text='Welcome to Tkinter!', width=4,
             height=2, bd='10', command=window.destroy)
  
btn.place(x=100, y=100)
'''

def create_grid(event=None):
    w = can1.winfo_width() # Get current width of canvas
    h = can1.winfo_height() # Get current height of canvas
    can1.delete('grid_line') # Will only remove the grid_line

    # Creates all vertical lines at intevals of 100
    for i in range(0, w, 100):
        can1.create_line([(i, 0), (i, h)], tag='grid_line')

    # Creates all horizontal lines at intevals of 100
    for i in range(0, h, 100):
        can1.create_line([(0, i), (w, i)], tag='grid_line')

can1.bind('<Configure>', create_grid)

def nouveau():
    pass

def ouvrir():
    pass

def quitter_logiciel():
    window.destroy()

def a_propos():
    mon_message = messagebox.showinfo("Jeu mastermind sur tkinter version 1.0", "Informations complémentaires")
    
barremenu = Menu(window)
window.config(menu = barremenu)

fichier_menu = Menu(barremenu, tearoff = 0)
barremenu.add_cascade(label = "Fichier", menu = fichier_menu)
fichier_menu.add_command(label = "Nouveau", command = nouveau)
fichier_menu.add_command(label = "Ouvrir", command = ouvrir)
fichier_menu.add_separator()
fichier_menu.add_command(label = "Quitter le logiciel", command = quitter_logiciel)

edition_menu = Menu(barremenu, tearoff = 0)
barremenu.add_cascade(label = "Edition 1.0", menu = edition_menu)

apropos = Menu(barremenu, tearoff = 0)
barremenu.add_cascade(label = "A propos", menu = apropos)
apropos.add_command(label = "Mastermind", command = a_propos)



    
window.mainloop()
```
Ajout d'une grille pour placer les éléments du jeu sur le canavs (j'ai galérer)

```python
def create_grid(event=None):
    w = can1.winfo_width() # Get current width of canvas
    h = can1.winfo_height() # Get current height of canvas
    can1.delete('grid_line') # Will only remove the grid_line

    # Creates all vertical lines at intevals of 100
    for i in range(0, w, 100):
        can1.create_line([(i, 0), (i, h)], tag='grid_line')

    # Creates all horizontal lines at intevals of 100
    for i in range(0, h, 100):
        can1.create_line([(0, i), (w, i)], tag='grid_line')
```
 
