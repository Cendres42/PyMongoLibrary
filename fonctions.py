
import pprint
from bson.objectid import ObjectId


def rechercherLivre(coll):

#def precision(coll,selection):
    selection=int(input("Voulez-vous choisir par:\n 1- Titre : \n 2- Auteur : \n 3- Année de parution : "))

    if selection==1:
        sous_selection=input("Entrez le titre du livre ou une partie du titre: ")
        query2=coll.find({"title":{"$regex":sous_selection}})
        #query2=coll.aggregate([{"$match": {"title":{"$eq":sous_selection}}},{"$limit":5}])
        print(list(query2))
    elif selection==2:
        sous_selection=input("Entrez l'auteur du livre : ")
        query2=coll.aggregate([{"$match": {"authors":{"$eq":sous_selection}}},{"$limit":5}])
        print(list(query2))
    elif selection==3:
        sous_selection=int(input("Entrez l'année de parution : "))
        query2=coll.aggregate([{"$match": {"year":{"$eq":sous_selection}}},{"$limit":5}])
        print(list(query2))



def ajouterPubli(coll):
    choix2=int(input("Voulez-vous ajouter\n 1- Un livre : \n 2- Un article : "))
    title=input("Saisissez le titre : ")
    year=input("Saisissez l'année de parution : ")
    auteur=input("Saisissez le nom complet de l'auteur : ")
    if choix2==1:
        coll.insert_one({ "type": "Livre", "title" : title, "year":year, "authors": auteur})
    elif choix2==2:
        coll.insert_one({ "type": "Article", "title" : title, "year":year, "authors": auteur})

def supprimerPubli(coll):
    id=input("Saisissez l'identifiant du livre' : ")
    coll.delete_one({ "_id": ObjectId(id)})
 


   
   
