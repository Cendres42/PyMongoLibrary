from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pymongo
import pprint
from classes.fonctionRecherche import *
from classes.fonctionAjout import *
from bson.objectid import ObjectId
from classes.livres import *
from bson.errors import InvalidId
from classes.fonctionSuppression import *
from menuprincipal import *
from menurecherche import *

# création des variables liées à la base de donnnées
client = MongoClient("localhost",27017)
db=client["my-first-db"]     
coll = db["books"]
bibli=Bibliotheque(coll)
result=""
#
#@ brief fonction de menu proposant à l'utilisateur différents choix 
#
def Menu():
    while True:
        try:
            #choix=int(input("Faites votre choix dans ce menu : \n 1- Rechercher un livre :\n 2- Ajouter une publication : \n 3- Supprimer un livre\n 4- Quitter l'application : \n"))
            menu=Menuprincipal()
            choix=menu.open()
            if choix<=0 or choix>4:
                raise ValueError
        except ValueError:
            print("Votre choix doit être un chiffre entre 1 et 4")
        else:    
            if choix==1:
                rechercherMedia(bibli)
            elif choix==2:
                menu=MenuAjout()
                menu.open(bibli)
            elif choix==3:
                supprimerPubli(bibli)
            elif choix==4:
                break

        
Menu()
