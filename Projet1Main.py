from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pymongo
import pprint
from classes.fonctions import *
from bson.objectid import ObjectId
from classes.livres import *

client = MongoClient("localhost",27017)
db=client["my-first-db"]     
coll = db["books"]
bibli=Bibliotheque(coll)


def Menu():
    while True:
        choix=int(input("Faites votre choix dans ce menu : \n 1- Rechercher un livre : \n 2- Ajouter une publication : \n 3- Supprimer un livre\n 4- Quitter l'application : \n"))
        if choix==1:
            rechercherMedia(bibli)
        elif choix==2:
            ajouterPubli(bibli)
        elif choix==3:
            supprimerPubli(bibli)
        elif choix==4:
           break
        
Menu()
"""
query=coll.aggregate([{"$match": {"type":{"$eq":"Article"},"year":{"$eq":2006}}},{"$limit":5}])
for item in query:
    print(item)
"""
#print(db["books"].index_information())

    