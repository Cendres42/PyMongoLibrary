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
        titre=input("Saisissez le titre : ")
        year=input("Saisissez l'année de parution :")
        auteur=input("Saisissez le nom complet de l'auteur :")
    if choix2==1:
        bibli.createBook(titre,auteur,year)
    elif choix2==2:
        bibli.createArticle(titre,auteur,year)


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
 


   
   
