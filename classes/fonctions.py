import pprint
from bson.objectid import ObjectId
from bson.errors import InvalidId
from classes.livres import *
import sys
import curses
from curses import wrapper

#
# @brief fonction qui affiche les données filtrées par auteur, titre ou année de parution
# @param la base de données (bibli) et le résultat de la sélection à filtrer (publi)
#
def filtreMedia(bibli,publi):
    try:
        filtre=int(input("Par quoi voulez-vous filtrer vos résultats ? \n 1- Par auteur : \n 2- Par année de parution : \n 3- Par titre\n"))
        if filtre<0 or filtre>3:
                raise ValueError
    except ValueError:
        print("Votre saisie doit être un chiffre entre 1 et 3")
    else:
        if filtre==1:
            auteur=input("Saisissez le nom complet de l'auteur pour filtrer : ")
            publi_triee=bibli.filteredByAuthors(auteur,publi)
            print(publi_triee)
        elif filtre==2:
            year=int(input("Saisissez l'année de parution pour filtrer : "))
            publi_triee=bibli.filteredByYear(year,publi)
            print(publi_triee)
        elif filtre==3:
            title=input("Saisissez le titre ou une partie du titre pour filtrer: ")
            publi_triee=bibli.filteredByBook(title,publi)
            print(publi_triee)
#
# @brief fonction qui affiche les données recherchée par auteur, titre ou année de parution
# @param la base de données (bibli)
#
def rechercherMedia(bibli):
    while True:
        try:
            selection=int(input("Voulez-vous choisir par:\n 1- Titre : \n 2- Auteur : \n 3- Année de parution : \n"))
            if selection<0 or selection>3:
                raise ValueError
        except ValueError:
            print("Votre saisie doit être un chiffre entre 1 et 3")
            break   
        try:
            tri=int(input("Pour trier par auteur, tapez 1,\n pour trier par année de parution, tapez 2,\n pour trier par titre, tapez 3,\n pour ne pas trier, tapez 4\n"))
            if selection<0 or selection>4:
                raise ValueError
        except ValueError:
            print("Votre saisie doit être un chiffre entre 1 et 4")
            break
        else:
            if selection==1:
                try:
                    sous_selection=input("Entrez le titre du livre ou une partie du titre: ")
                except ValueError:
                    print("Votre saisie est incorrecte")
                else:
                    publi=bibli.findByTitle(sous_selection,tri)
                    print(publi)
            elif selection==2:
                try:
                    sous_selection=input("Entrez l'auteur du livre : ")
                except ValueError:
                    print("Votre saisie est incorrecte")
                else:
                    publi=bibli.findByAuthors(sous_selection,tri)
                    print(publi)
            elif selection==3:
                try:
                    sous_selection=int(input("Entrez l'année de parution : "))
                except ValueError:
                    print("Votre saisie est incorrecte")
                else:
                    publi=bibli.findByYear(sous_selection,tri)
                    print(publi)
            #next_pages=int(input("Pour afficher les 5 documents suivants"))
            if menuChoice(bibli,publi)==True:
                continue
            else:
                break

#
# @brief fonction qui affiche un menu en fin d'opération 
# @param la base de données (bibli) et le résultat de la sélection à filtrer (publi)
#
def menuChoice(bibli,publi):
    while True:
        try:
            next_menu=int(input("Que souhaitez-vous faire :\n 1- Une nouvelle sélection\n 2- Filtrer vos résultats\n 3- Revenir au menu principal\n 4- Obiwankenobi\n"))
            if next_menu<0 or next_menu>4:
                raise ValueError
        except ValueError:
            print("Votre saisie doit être un chiffre entre 1 et 4")
        else:
            if next_menu==1:
                return True
            elif next_menu==2:     
                filtreMedia(bibli,publi)
            elif next_menu==3:
                return False
            elif next_menu==4:
                print("Je suis ton père")
#
# @brief fonction qui permet l'ajout d'une publication
# @param la base de donnée "bibli"
# utilise la livrairie ncurses pour les inputs
#  
def ajouterPubli(bibli):
    #utilisation variable définie à l'extérieur
    try:
        choix2=int(input("Voulez-vous ajouter\n 1- Un livre : \n 2- Un article : \n 3- Revenir au menu principal \n"))
        if choix2<0 or choix2>4:
                raise ValueError
    except ValueError:
            print("Votre saisie doit être un chiffre entre 1 et 4")
    else:

# -------------------------------------------------
	# - Etape 1: Demarrer ncurses                     -
	# -------------------------------------------------

	# Initialise la librairie ncurses
        win = curses.initscr()

	# Par defaut, le curseur est masque
        curses.curs_set(0)
        curses.noecho()
    
        # Permet a ncurses d'utiliser des couleurs (optionnel)
        curses.start_color()
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLUE)

        # Efface tout l'ecran
        win.clear()

        # Rafraichit tout l'écran
        win.refresh()

        # -------------------------------------------------
        # - Etape 2: Construire une fenetre               -
        # -------------------------------------------------

        # Construction d'une fenetre centree
        width  = 50  # Largeur de la fenetre
        height = 15   # Hauteur de la fenetre
        posX = int( (curses.COLS - width) / 2)
        posY = int( (curses.LINES - height) / 2)
        box1 = curses.newwin(height, width, posY, posX)
        # utilisation partie droite clavier
        box1.keypad(True)
        # Fixe la couleur de fond (texte noir sur fond bleu)
        box1.bkgd(' ', curses.color_pair(2))
        # Dessine une "boite" sur les bords de la fenetre
        box1.box()

        # Ajoute un titre a la fenetre (avec bordures)
        box1.addch(0,2, curses.ACS_RTEE)
        box1.addstr(0, 3, " Ajout d'une publication : ")
        box1.addstr(2, 3, "Complétez les champs ci-dessous. ")
        box1.addstr(3, 3, "Utilisez les flèches pour naviguer. ")
        box1.addstr(4, 3, "Appuyez sur entrée pour valider votre saisie. ")

        box1.addch(0, 29, curses.ACS_LTEE)

        # Rafraichit la fenetre
        box1.refresh()

        # -------------------------------------------------
        # - Etape 3: Lecture d'une saisie                 -
        # -------------------------------------------------

        # Intitule de la zone de saisie
        box1.addstr(6, 3, "Titre : ")
        box1.addstr(8, 3, "Année de parution :")
        box1.addstr(10, 3, "Nom de l'auteur :")
        # Affiche une zone noire pour montrer la zone de saisie
        box1.addstr(7, 8, "                ", curses.color_pair(1))
        box1.addstr(9, 8, "                ", curses.color_pair(1))
        box1.addstr(11, 8, "                ", curses.color_pair(1))

        box1.move(7,8)
        curses.curs_set(1)
        box1.refresh()

        # Boucle pour lire la saisie clavier du champ "nom"
        k   = 0
        titre=""
        year=""
        auteur = ""
        select=0
        pos = 0
        i=0
        while True:
            k = box1.getch()
            if k in [10,13,curses.KEY_ENTER]:
                if select<2:
                    select+=1
                    pos=0
                    box1.move(7+select*2,8)
                    win.refresh()
                    box1.refresh()
                else:
                    break
            elif k==27:
                break
            elif k==curses.KEY_UP:
                select-=1
                pos=0
                box1.move(7+select*2,8)
                win.refresh()
                box1.refresh()
            elif k==curses.KEY_DOWN:
                select+=1
                pos=0
                box1.move(7+select*2,8)
                win.refresh()
                box1.refresh()
            elif k == curses.KEY_BACKSPACE or k == 127 or k == 8:
                if select==0:
                    if pos > 0:
                        pos -= 1
                        box1.addstr(7, 8+pos, " ", curses.color_pair(1))
                        titre = titre[:-1]
                elif select==1: 
                    if pos > 0:
                        pos -= 1
                        box1.addstr(9, 8+pos, " ", curses.color_pair(1))
                        year = year[:-1]
                elif select==2:
                    if pos > 0:
                        pos -= 1
                        box1.addstr(11, 8+pos, " ", curses.color_pair(1))
                        auteur = auteur[:-1]
            elif pos < 30:
                if select==0:
                    box1.addch(7, 8+pos, k, curses.color_pair(1))
                    titre += chr(k)
                    pos += 1
                elif select==1:
                    box1.addch(9, 8+pos, k, curses.color_pair(1))
                    year += chr(k)
                    pos += 1
                elif select==2:
                    box1.addch(11, 8+pos, k, curses.color_pair(1))
                    auteur += chr(k)    
                    pos += 1			

            
        # Si la touche "Entree" a ete pressee
        if k in [10,13, curses.KEY_ENTER]:
            # Re-ecrit la zone noire ... pour la remettre en bleu
            for i in range(1,11):
                box1.addstr(i, 3, "                                                ", curses.color_pair(2))

            # Dis bonjour a l'utilisateur
            box1.addstr(2,3, "Vous avez ajouté cette publication ")
            box1.addstr(4, 3, "Titre : ")
            box1.addstr(6, 3, "Année de parution :")
            box1.addstr(8, 3, "Auteur :")
            box1.addstr(5,3,titre)
            box1.addstr(7,3,year)
            box1.addstr(9,3,auteur)

            box1.refresh()
            # Attend l'appui sur une touche avant de sortir
            key = win.getch()

            if choix2==1:
                bibli.createBook(titre,auteur,year)
            elif choix2==2:
                bibli.createArticle(titre,auteur,year)
        # Wait key-press before end of program
        #key = win.getch()

        curses.endwin()


#
# @brief fonction qui permet la suppression d'une publication à partir de son identifiant
# @param la base de donnée "bibli"
#  
def supprimerPubli(bibli):
    id=input("Saisissez l'identifiant du document à supprimer : ")
    try:  
        bibli.removeMedia(id)
    except InvalidId:
            print("Votre saisie doit être être un id de 24 caractères")
 


   
   
