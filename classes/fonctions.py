import pprint
from bson.objectid import ObjectId
from classes.livres import *


def filtreMedia(bibli,publi):
    filtre=int(input("Par quoi voulez-vous filtrer vos résultats ? \n 1- Par auteur : \n 2- Par année de parution : \n 3- Par titre\n"))
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

def rechercherMedia(bibli):
    while True:
        selection=int(input("Voulez-vous choisir par:\n 1- Titre : \n 2- Auteur : \n 3- Année de parution : \n"))
        tri=int(input("Pour trier par auteur, tapez 1,\n pour trier par année de parution, tapez 2,\n pour trier par titre, tapez 3,\n pour ne pas trier, tapez 4\n"))
        if selection==1:
            sous_selection=input("Entrez le titre du livre ou une partie du titre: ")
            publi=bibli.findByTitle(sous_selection,tri)
            print(publi)
        elif selection==2:
            sous_selection=input("Entrez l'auteur du livre : ")
            publi=bibli.findByAuthors(sous_selection,tri)
            print(publi)
        elif selection==3:
            sous_selection=int(input("Entrez l'année de parution : "))
            publi=bibli.findByYear(sous_selection,tri)
            print(publi)
        #next_pages=int(input("Pour afficher les 5 documents suivants"))
        if menuChoice(bibli,publi)==True:
            continue
        else:
            break
    
def menuChoice(bibli,publi):
    while True:
        next_menu=int(input("Que souhaitez-vous faire :\n 1- Une nouvelle sélection\n 2- Filtrer vos résultats\n 3- Revenir au menu principal\n 4- Obiwankenobi\n"))
        if next_menu==1:
            return True
        elif next_menu==2:     
            filtreMedia(bibli,publi)
        elif next_menu==3:
            return False
        elif next_menu==4:
            print("Je suis ton père")

def ajouterPubli(bibli):
    #utilisation variable définie à l'extérieur
    choix2=int(input("Voulez-vous ajouter\n 1- Un livre : \n 2- Un article : \n 3- Revenir au menu principal"))
    title=input("Saisissez le titre : ")
    year=int(input("Saisissez l'année de parution : "))
    auteur=input("Saisissez le nom complet de l'auteur : ")
    if choix2==1:
        bibli.createBook(title,auteur,year)
    elif choix2==2:
        bibli.createArticle(title,auteur,year)

def supprimerPubli(bibli):
    id=input("Saisissez l'identifiant du document à supprimer : ")
    bibli.removeMedia(id)
 


   
   
