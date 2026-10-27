#                   Base de donnee
# importer mongo client
from pymongo import MongoClient 
# initialiser la table
def createtable():
    client = MongoClient("mongodb://localhost:27017")
    db = client["game_db"]
    return db
# creer les deux colection monstre et heros
def createcol(db):
    list_heros = db["heros"]
    list_monstres = db["monstres"]
    return list_heros, list_monstres
# vider les deux colonne pour cas ou donner deja presente
def clearcol(list_heros, list_monstres):
    list_heros.del()
    list_monstres.drop()
# remplir la table
def insertdata() :
    heros_data = [{"id" : "1", "nom" : "Darius", "ATK" : "100", "DEF" : "100", "PV" : "500"},
                 {"id" : "2", "nom" : "Sett", "ATK" : "100", "DEF" : "100", "PV" : "500"},
                 {"id" : "3", "nom" : "Mordekaiser", "ATK" : "100", "DEF" : "100", "PV" : "500"},
                 {"id" : "4", "nom" : "Olaf", "ATK" : "100", "DEF" : "100", "PV" : "500"},
                 {"id" : "5", "nom" : "Dr.Mundo", "ATK" : "100", "DEF" : "100", "PV" : "500"},
                 {"id" : "6", "nom" : "Viego", "ATK" : "100", "DEF" : "100", "PV" : "500"},
                 {"id" : "7", "nom" : "Smolder", "ATK" : "100", "DEF" : "100", "PV" : "500"},
                 {"id" : "8", "nom" : "Caytlin", "ATK" : "100", "DEF" : "100", "PV" : "500"},
                 {"id" : "9", "nom" : "Yone", "ATK" : "100", "DEF" : "100", "PV" : "500"},
                 {"id" : "10", "nom" : "Jax", "ATK" : "100", "DEF" : "100", "PV" : "500"}]



    monstres_data = [{"id" : "1", "nom" : "Drake", "ATK" : "100", "DEF" : "100", "PV" : "500"},
                    {"id" : "2", "nom" : "Nash", "ATK" : "100", "DEF" : "100", "PV" : "500"},
                    {"id" : "3", "nom" : "Elder", "ATK" : "100", "DEF" : "100", "PV" : "500"},
                    {"id" : "4", "nom" : "void grubs", "ATK" : "100", "DEF" : "100", "PV" : "500"},
                    {"id" : "5", "nom" : "Red Buff", "ATK" : "100", "DEF" : "100", "PV" : "500"},
                    {"id" : "6", "nom" : "Blue Buff", "ATK" : "100", "DEF" : "100", "PV" : "500"},
                    {"id" : "7", "nom" : "Herald", "ATK" : "100", "DEF" : "100", "PV" : "500"},
                    {"id" : "8", "nom" : "Rapors", "ATK" : "100", "DEF" : "100", "PV" : "500"},
                    {"id" : "9", "nom" : "Gromp", "ATK" : "100", "DEF" : "100", "PV" : "500"},
                    {"id" : "10", "nom" : "carap", "ATK" : "100", "DEF" : "100", "PV" : "500"}]
    return heros_data, monstres_data
# inserer les donner dans la table
def insertcol (list_heros, list_monstres, heros_data, monstres_data) :
    list_heros.insert_many(heros_data)
    list_monstres.insert_many(monstres_data)
# message pour montrer que c passer
db = createtable()
list_heros, list_monstres = createcol(db)
clearcol(list_heros = any, list_monstres = any)
heros_data, monstres_data = insertdata()
insertcol(list_heros, list_monstres, heros_data, monstres_data)
print ("donner inserer")