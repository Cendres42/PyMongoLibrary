import pprint
from bson.objectid import ObjectId
from bson.errors import InvalidId
from classes.livres import *
import sys
import curses
from curses import wrapper
from menurecherche import *
#
# @brief fonction qui affiche un menu en fin d'opération 
# @param la base de données (bibli) et le résultat de la sélection à filtrer (publi)
#
def menuChoice(bibli,publi):
    while True:
        try:
            next_menu=int(input("Que souhaitez-vous faire :\n 1- Une nouvelle sélection\n 2- Filtrer vos résultats\n 3- Revenir au menu principal\n 4- Obiwankenobi\n"))
            if next_menu<=0 or next_menu>4:
                raise ValueError
        except ValueError:
            print("Votre saisie doit être un chiffre entre 1 et 4")
        else:
            if next_menu==1:
                return 1
            elif next_menu==2:     
                return 2
            elif next_menu==3:
                return 0
            elif next_menu==4:
                print("Je suis ton père")
#
# @brief fonction qui affiche les données recherchée par auteur, titre ou année de parution
# @param la base de données (bibli)
#
def rechercherMedia(bibli,result):
    selection = 0
    tri = 0
    sous_selection = ""
    toSkip=0
    result=""
    tofiltre=""
    typefiltre=""
    filtre=""
    while True:
        try:
            if selection == 0:
                menu=Menurecherche()
                selection=menu.open()
                print(selection)
                #selection=int(input("Voulez-vous choisir par:\n 1- Titre : \n 2- Auteur : \n 3- Année de parution : \n"))
                if selection<=0 or selection>3:
                    raise ValueError
        except ValueError:
            print("Votre saisie doit être un chiffre entre 1 et 3")
            break   
        try:
            if tri == 0:
                tri=int(input("Pour trier par auteur, tapez 1,\n pour trier par année de parution, tapez 2,\n pour trier par titre, tapez 3,\n pour ne pas trier, tapez 4\n"))
                if selection<=0 or selection>4:
                    raise ValueError
        except ValueError:
            print("Votre saisie doit être un chiffre entre 1 et 4")
            break
        else:
            if selection==1:
                try:
                    if sous_selection == "":
                        sous_selection=input("Entrez le titre du livre ou une partie du titre: ")
                except ValueError:
                    print("Votre saisie est incorrecte")
                else:
                    if typefiltre!="":
                        tofiltre=filtre
                        publi=bibli.findByTitle(sous_selection,tri,toSkip,typefiltre,tofiltre)
                        print(publi)
                    else:
                        publi=bibli.findByTitle(sous_selection,tri,toSkip)
                        print(publi)
            elif selection==2:
                try:
                    if sous_selection == "":
                        sous_selection=input("Entrez l'auteur du livre : ")
                except ValueError:
                    print("Votre saisie est incorrecte")
                else:
                    if typefiltre!="":
                        tofiltre=filtre
                        publi=bibli.findByAuthors(sous_selection,tri,toSkip,typefiltre,tofiltre)
                        print(publi)
                    else:
                        publi=bibli.findByAuthors(sous_selection,tri,toSkip)
                        print(publi)
            elif selection==3:
                try:
                    if sous_selection == "":
                        sous_selection=int(input("Entrez l'année de parution : "))
                except ValueError:
                    print("Votre saisie est incorrecte")
                else:
                    if typefiltre!="":
                        tofiltre=filtre
                        publi=bibli.findByYear(sous_selection,tri,toSkip,typefiltre,tofiltre)
                        print(publi)
                    else:
                        publi=bibli.findByYear(sous_selection,tri,toSkip)
                        print(publi)
            try:
                next=int(input("Pour afficher les 5 résultats suivants tapez 1 \n sinon tapez 2\n"))
                if next<=0 or next>2:
                    raise ValueError
            except ValueError:
                print("Vous devez saisir 1 ou 2")
            else:
                if next==1:
                    toSkip+=5
                elif next==2:
                    x= menuChoice(bibli,publi)
                    if x==0:
                        break
                    elif x==1:
                        selection = 0
                        tri = 0
                        sous_selection = ""
                        toSkip=0
                        result=""
                        tofiltre=""
                        typefiltre=""
                        filtre=""
                    elif x==2:
                        toSkip=0
                        result=filtreMedia()
                        result2=result.split(":")
                        typefiltre=result2[0]
                        filtre=result2[1]



#
# @brief fonction qui affiche les données filtrées par auteur, titre ou année de parution
# @param la base de données (bibli) et le résultat de la sélection à filtrer (publi)
#
def filtreMedia():
    result=""
    while True:
        try:
            filtre=int(input("Par quoi voulez-vous filtrer vos résultats ? \n 1- Par auteur : \n 2- Par année de parution : \n 3- Par titre\n"))
            if filtre<=0 or filtre>3:
                raise ValueError
            break
        except ValueError:
            print("Votre saisie doit être un chiffre entre 1 et 3")
    if filtre==1:
        auteur=input("Saisissez le nom complet de l'auteur pour filtrer : ")
        result="authors:"+ auteur
    elif filtre==2:
        year=input("Saisissez l'année de parution pour filtrer : ")
        result="year:"+year
    elif filtre==3:
        title=input("Saisissez le titre ou une partie du titre pour filtrer: ")
        result="title:"+title
    return result



   
   
