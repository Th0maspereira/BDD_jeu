# j'ai repris ma bdd de l'annee derniere 

from pymongo import MongoClient

def initialisation_de_la_db():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["game_db"]
    
    #pour reset les col
#def clearcol(db):
    db.heros.drop()
    db.monstres.drop()
    db.equipe.drop()
    db.score.drop()

#def createcol():
    list_heros = [
        {"id" : "1", "nom": "Darius", "ATK": "30", "DEF": "15", "PV": "200"},
        {"id" : "2", "nom": "Sett", "ATK": "20", "DEF": "10", "PV": "200"},
        {"id" : "3", "nom": "Mordekaiser", "ATK": "30", "DEF": "7", "PV": "200"},
        {"id" : "4", "nom": "Jax", "ATK": "25", "DEF": "8", "PV": "200"},
        {"id" : "5", "nom": "Olaf", "ATK": "20", "DEF": "7", "PV": "200"},
        {"id" : "6", "nom": "Viego", "ATK": "20", "DEF": "3", "PV": "200"},
        {"id" : "7", "nom": "Dr.mundo", "ATK": "20", "DEF": "15", "PV": "300"},
        {"id" : "8", "nom": "Caytlin", "ATK": "25", "DEF": "9", "PV": "200"},
        {"id" : "9", "nom": "Smolder", "ATK": "20", "DEF": "15", "PV": "300"},
        {"id" : "10","nom": "Yone", "ATK": "23", "DEF": "15", "PV": "300"}
    ]

    list_monstres=[
        {"id" : "1", "nom": "Drake", "ATK": "20", "DEF": "5", "PV": "200"},
        {"id" : "2", "nom": "Nash", "ATK": "25", "DEF": "8", "PV": "300"},
        {"id" : "3", "nom": "Elder", "ATK": "25", "DEF": "20", "PV":"350"},
        {"id" : "4", "nom": "void grubs", "ATK": "12", "DEF": "6", "PV": "150"},
        {"id" : "5", "nom": "herald", "ATK": "15", "DEF": "15", "PV": "200"},
        {"id" : "6", "nom": "Blue buff", "ATK": "10", "DEF": "10", "PV": "100"},
        {"id" : "7", "nom": "Red buff", "ATK": "10", "DEF": "25", "PV": "100"},
        {"id" : "8", "nom": "carap", "ATK": "25", "DEF": "18", "PV": "250"},
        {"id" : "9", "nom": "raptors", "ATK": "20", "DEF": "12", "PV": "200"},
        {"id" : "10", "nom": "gromp", "ATK": "30", "DEF": "5", "PV": "150"}    
    ]
    list_equipe = []
    list_score = []
    

    # pour inserer les list
#def insertcol(db, list_heros, list_monstres):
    db.heros.insert_many(list_heros)
    db.monstres.insert_many(list_monstres)

    print("c bon")
initialisation_de_la_db()
