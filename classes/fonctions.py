import pprint
from bson.objectid import ObjectId
from classes.livres import *

def rechercherMedia(bibli):
#def precision(coll,selection):
    selection=int(input("Voulez-vous choisir par:\n 1- Titre : \n 2- Auteur : \n 3- Année de parution : \n"))
    if selection==1:
        sous_selection=input("Entrez le titre du livre ou une partie du titre: ")
        publi=bibli.findByTitle(sous_selection)
        print(publi)
    elif selection==2:
        sous_selection=input("Entrez l'auteur du livre : ")
        publi=bibli.findByAuthors(sous_selection)
        print(publi)
    elif selection==3:
        sous_selection=int(input("Entrez l'année de parution : "))
        publi=bibli.findByYear(sous_selection)
        print(publi)



def ajouterPubli(bibli):
    #utilisation variable définie à l'extérieur
    choix2=int(input("Voulez-vous ajouter\n 1- Un livre : \n 2- Un article : "))
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
 


   
   
