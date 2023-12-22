from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pymongo
import pprint
from fonctions import*
from bson.objectid import ObjectId



client = MongoClient("localhost",27017)
db=client["my-first-db"]     
coll = db["books"]
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Connexion OK")
except Exception as e:
    print(e)

def Menu():

    while True:
        choix=int(input("Faites votre choix dans ce menu : \n 1- Rechercher un livre : \n 2- Ajouter une publication : \n 3- Supprimer un livre\n 4- Quitter l'application : "))
        if choix==1:
            rechercherLivre(coll)
        elif choix==2:
            ajouterPubli(coll)
        elif choix==3:
            supprimerPubli(coll)
        elif choix==4:
           break
        
Menu()
"""
query=coll.aggregate([{"$match": {"type":{"$eq":"Article"},"year":{"$eq":2006}}},{"$limit":5}])
for item in query:
    print(item)
"""
#print(db["books"].index_information())

    