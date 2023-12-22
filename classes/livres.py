from bson.objectid import ObjectId


class Bibliotheque():
    def __init__(self,db):
        self.db=db
    def createBook(self,title,auteur,year):
        livre=Livre(self.db)
        self.filMedia(livre,title,auteur,year)
        livre.save()

    def createArticle(self,title,auteur,year):
        article=Article(self.db)
        self.filMedia(article,title,auteur,year)
        article.save()

    def filMedia(self,objet,title,auteur,year):
        objet.setTitle(title)
        objet.setAuteur(auteur)
        objet.setYear(year)
        
    def removeMedia(self,id):
        self.db.delete_one({ "_id": ObjectId(id)})

    def findByTitle(self,selec):
        publi_tab=[]
        query2=self.db.aggregate([{"$project":{"type":1,"title":1,"authors":1,"year":1}},{"$match":{"title":{"$regex":selec}}}])
        for item in query2:
            if item["type"]=="Book" or item["type"]=="Livre":
                new_publi = Livre(self.db, item["_id"])
            elif item["type"]=="Article":
                new_publi=Article(self.db,item["_id"])
            else :
                continue
            publi_tab.append(new_publi)    
        return publi_tab
    
    def findByAuthors(self,selec):
        publi_tab=[]
        query2=self.db.aggregate([{"$project":{"type":1,"title":1,"authors":1,"year":1}},{"$match": {"authors":{"$eq":selec}}}])
        for item in query2:
            if item["type"]=="Book" or item["type"]=="Livre":
                new_publi = Livre(self.db, item["_id"])
            elif item["type"]=="Article":
                new_publi=Article(self.db,item["_id"])
            else :
                continue
            publi_tab.append(new_publi)  
        return publi_tab
    
    def findByYear(self,selec):
        publi_tab=[]
        query2=self.db.aggregate([{"$project":{"type":1,"title":1,"authors":1,"year":1}},{"$match": {"year":{"$eq":selec}}}])
        for item in query2:
            if item["type"]=="Book" or item["type"]=="Livre":
                new_publi = Livre(self.db, item["_id"])
            elif item["type"]=="Article":
                new_publi=Article(self.db,item["_id"])
            else :
                continue
            publi_tab.append(new_publi)  
        return publi_tab
    
    

    

class Media():
    def __init__(self,db,id=""):
        self.type=""
        self.title=""
        self.auteur=""
        self.year=0
        self.id=id
        self.db=db
        if self.id != "":
            obj = db.find_one({"_id":self.id})
            self.setTitle( obj["title"] )
            self.setType(obj["type"])
            self.setAuteur(obj["authors"])
            self.setYear(obj["year"])
    def setType(self,type):
        self.type=type
    def setTitle(self,title):
        self.title=title
    def setAuteur(self,auteur):
        self.auteur=auteur
    def setYear(self,year):
        self.year=year
    
    def __repr__(self):
        return(f"Type : {self.type}\n Titre :{self.title}\n Auteur : {self.auteur}\n Année de parution : {self.year}")

    
    
class Livre(Media):
    def __init__(self,db, id=""):
        #appelle fonction constructeur de média
        super().__init__(db, id)
        self.setType("Book")
        self.publisher=""
    def setPublisher(self,name):
        self.publisher=name
    def save(self):
        #possibilité rajouter un if else selon bd appelée
        self.db.insert_one({ "type": self.type, "title" : self.title, "year":self.year, "authors": self.auteur,"publisher":self.publisher})


class Article(Media):
    def __init__(self,db,id=""):
        super().__init__(db,id)
        self.setType("Article")
        self.booktitle=""
    def setBooktitle(self,name):
        self.booktitle=name
    def save(self):
        self.db.insert_one({ "type": self.type, "title" : self.title, "year":self.year, "authors": self.auteur,"booktile":self.booktitle})

