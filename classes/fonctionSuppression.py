import pprint
from bson.objectid import ObjectId
from bson.errors import InvalidId
from classes.livres import *
import sys
import curses
from curses import wrapper
#
# @brief fonction qui permet la suppression d'une publication à partir de son identifiant
# @param la base de donnée "bibli"
#  
def supprimerPubli(bibli):
    try:
        choix=int(input("Pour supprimer par : \n id tapez 1\n auteur tapez 2\n titre tapez 3\n selection mutlicritères tapez 4 \n"))
        if choix<0 or choix>4:
                raise ValueError
    except ValueError:
            print("Votre saisie doit être un chiffre entre 1 et 4")
    else:
        if choix==1:
            id=input("Saisissez l'identifiant du document à supprimer : \n")
            try:  
                bibli.removeMediabyID(id)
            except InvalidId:
                    print("Votre saisie doit être être un id de 24 caractères")
        if choix==2:
            auteur=input("Saisissez l'auteur dont vous souhaitez supprimer les publications : \n ")
            try:  
                nbSup=bibli.removeMediabyAuteur(auteur)
                if nbSup==0:
                    print("Aucune publication n'a été supprimée")
            except :
                print("Erreur fatale lors de la tentative")
        if choix==3:
            titre=input("Saisissez le titre de la publication à supprimer : \n ")
            try:  
                nbSup=bibli.removeMediabyTitre(titre)
                if nbSup==0:
                    print("Aucune publication n'a été supprimée")
            except :
                print("Erreur fatale lors de la tentative")
        if choix==4:
            auteur=input("Saisissez l'auteur dont vous souhaitez supprimer les publications : \n ")
            year=input("Saisissez l'année de publication : \n ")
            try:  
                nbSup=bibli.removeMediabyMulti(auteur,year)
                if nbSup==0:
                    print("Aucune publication n'a été supprimée")
            except :
                print("Erreur fatale lors de la tentative")