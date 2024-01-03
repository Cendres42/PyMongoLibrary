from bson.objectid import ObjectId

#Création d'une classe Bibliothèque  

class Bibliotheque():
    def __init__(self,db):
        self.db=db
    
    # @brief une bibliothèque peut créer des livres
    def createBook(self,title,auteur,year):
        livre=Livre(self.db)
        self.filMedia(livre,title,auteur,year)
        livre.save()
    
    # @brief une bibliothèque peut créer des articles
    def createArticle(self,title,auteur,year):
        article=Article(self.db)
        self.filMedia(article,title,auteur,year)
        article.save()
    
    # @brief méthode qui remplit un objet avec les inputs communs à tous les médias
    def filMedia(self,objet,title,auteur,year):
        objet.title=title
        objet.auteur=auteur
        objet.year=year
        print(objet.title,objet.auteur,objet.year)
    
    # @brief méthode   qui supprime une publi à partir de son id 
    def removeMediabyID(self,id):
        self.db.delete_one({ "_id": ObjectId(id)})
    
    # @brief méthode   qui supprime des publis à partir de leur auteur
    def removeMediabyAuteur(self,auteur):
        result=self.db.delete_many({ "authors": auteur})
        return result.deleted_count
    
    # @brief méthode   qui supprime une publi à partie de son titre  
    def removeMediabyTitre(self,titre):
        result=self.db.delete_one({ "title": titre})
        return result.deleted_count
    
    # @brief méthode   qui supprime des publis à partir de leur auteur
    def removeMediabyMulti(self,auteur,year):
        result=self.db.delete_many({ "authors": auteur,"year": year})
        return result.deleted_count

    # @brief méthode   qui affiche les 5 premières publis à partir de leur titre
    def findByTitle(self,selec,tri,toSkip,tofiltre="",filtre=""):
        # Construit le pipeline d'agregate mongo
        pipe = []
        pipe.append({"$project":{"type":1,"title":1,"authors":1,"year":1}})
        pipe.append({"$match": {"title":{"$regex":selec}}})
        if filtre!="":
            pipe.append({"$match": {tofiltre:filtre}})
        if tri==1:
            pipe.append({"$sort":{"authors":1}})
        elif tri==2:
            pipe.append({"$sort":{"year":1}})
        elif tri==3:
            pipe.append({"$sort":{"title":1}})
        pipe.append({"$skip":toSkip})
        pipe.append({"$limit":5})
        query2=self.db.aggregate(pipe)

        publi_tab=[]
        for item in query2:
            if item["type"]=="Book" or item["type"]=="Livre":
                new_publi = Livre(self.db, item["_id"])
            elif item["type"]=="Article":
                new_publi=Article(self.db,item["_id"])
            else :
                continue
            publi_tab.append(new_publi)    
        return publi_tab
    
    # @brief méthode   qui affiche les 5 premières publis à partir de leur auteur
    def findByAuthors(self,selec,tri,toSkip,tofiltre="",filtre=""):
        # Construit le pipeline d'agregate mongo
        pipe = []
        pipe.append({"$project":{"type":1,"title":1,"authors":1,"year":1}})
        pipe.append({"$match": {"authors":selec}})
        if filtre!="":
            pipe.append({"$match": {tofiltre:filtre}})
        if tri==1:
            pipe.append({"$sort":{"authors":1}})
        elif tri==2:
            pipe.append({"$sort":{"year":1}})
        elif tri==3:
            pipe.append({"$sort":{"title":1}})
        pipe.append({"$skip":toSkip})
        pipe.append({"$limit":5})
        query2=self.db.aggregate(pipe)

        publi_tab=[]
        for item in query2:
            if item["type"]=="Book" or item["type"]=="Livre":
                new_publi = Livre(self.db, item["_id"])
            elif item["type"]=="Article":
                new_publi=Article(self.db,item["_id"])
            else :
                continue
            publi_tab.append(new_publi)  
        return publi_tab
    
    # @brief méthode   qui affiche les 5 premières publis à partir de leur année de publi
    def findByYear(self,selec,tri,toSkip,tofiltre="",filtre=""):
        # création nouvelle recherche
        # Construit le pipeline d'agregate mongo
        pipe = []
        pipe.append({"$project":{"type":1,"title":1,"authors":1,"year":1}})
        pipe.append({"$match": {"year":selec}})
        if filtre!="":
            pipe.append({"$match": {tofiltre:filtre}})
        if tri==1:
            pipe.append({"$sort":{"authors":1}})
        elif tri==2:
            pipe.append({"$sort":{"year":1}})
        elif tri==3:
            pipe.append({"$sort":{"title":1}})
        pipe.append({"$skip":toSkip})
        pipe.append({"$limit":5})
        query2=self.db.aggregate(pipe)
        
        publi_tab=[]
        for item in query2:
            if item["type"]=="Book" or item["type"]=="Livre":
                new_publi = Livre(self.db, item["_id"])
            elif item["type"]=="Article":
                new_publi=Article(self.db,item["_id"])
            else :
                continue
            publi_tab.append(new_publi)  
        return publi_tab
    
#
# @brief Création d'une classe Media, parente de Livre et Article   
# @param  la base de donnée et l'id de l'objet à créer
# un media a un type, un titre, un auteur, une année de publi, un id et est rattaché à une bd
#
class Media():
    def __init__(self,db,id=""):
        self._type=""
        self._title=""
        self._auteur=""
        self._year=0
        self._id=id
        self._db=db
        # les publi de la bd deviennent des objets
        if self._id != "":
            obj = db.find_one({"_id":self._id})
            self.type=obj["type"]
            self.title= obj["title"] 
            self.auteur=obj["authors"]
            self.year=obj["year"]
    #définition de properties pour type, titre, auteur et année de publi
    @property
    def type(self)->str:
        return(self._type)
    @type.setter
    def type(self, new_nom):
        self._type = new_nom
    @type.deleter
    def type(self):
       del self._type
    @type.getter
    def type(self):
       return self._type

    @property
    def title(self)->str:
        return(self._title)
    @title.setter
    def title(self, new_nom):
        self._title = new_nom
    @title.deleter
    def title(self):
       del self._title
    @title.getter
    def title(self):
       return self._title

    @property
    def auteur(self)->str:
        return(self._auteur)
    @auteur.setter
    def auteur(self, new_nom):
        self._auteur = new_nom
    @auteur.deleter
    def auteur(self):
       del self._auteur
    @auteur.getter
    def auteur(self):
       return self._auteur

    @property
    def year(self)->str:
        return(self._year)
    @year.setter
    def year(self, new_nom):
        self._year = new_nom
    @year.deleter
    def year(self):
       del self._year
    @year.getter
    def year(self):
       return self._year

    # création méthode magique __repr__ pour affichage données objet
    def __repr__(self):
        return(f"\nType : {self.type}\n Titre : {self.title}\n Auteur : {self.auteur}\n Année de parution : {self.year}\n ------------------------------\n")
#
# @brief Création d'une classe Livre, enfant de Media   
# @param  la base de donnée et l'id du livre à créer   
#    
class Livre(Media):
    def __init__(self,db, id=""):
        #appelle fonction constructeur de média
        super().__init__(db, id)
        self.type="Book"
        self.publisher=""
    #fonction pour ajout maison d'edition à livre
    def setPublisher(self,name):
        self.publisher=name
    def save(self):
        #insertion de lu livre dans la bd MongoDB
        #possibilité rajouter un if else selon bd appelée
        self._db.insert_one({ "type": self.type, "title" : self.title, "year":self.year, "authors": self.auteur,"publisher":self.publisher})
#
# @brief Création d'une classe Article, enfant de Media   
# @param  la base de donnée et l'id de l'article à créer 
#
class Article(Media):
    def __init__(self,db,id=""):
        #appelle fonction constructeur de média
        super().__init__(db,id)
        self.type="Article"
        self.booktitle=""

    # @brief méthode pour ajout revue qui a publié article
    def setBooktitle(self,name):
        self.booktitle=name
    
    #@ brief méthode d'insertion de l'article dans la bd MongoDB
    def save(self):
        self._db.insert_one({ "type": self.type, "title" : self.title, "year":self.year, "authors": self.auteur,"booktitle":self.booktitle})
