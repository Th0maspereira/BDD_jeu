#                   Base de donnee
# importer mongo client
from pymongo import MongoClient 
# initialiser la table
def createtable():
    client = MongoClient("http://localhost:27017")
    db = client["game.db"]
# creer les deux tableau monstre et heros
list_heros = []
list_monstres = []
# vider les deux colonne pour cas ou donner deja presente
list_heros.drop()
list_monstres.drop()
# remplir la table
list_heros = [{"id" : "1", "nom" : "Darius", "ATK" : "100", "DEF" : "100", "PV" : "500"},
              {"id" : "2", "nom" : "Sett", "ATK" : "100", "DEF" : "100", "PV" : "500"},
              {"id" : "3", "nom" : "Mordekaiser", "ATK" : "100", "DEF" : "100", "PV" : "500"},
              {"id" : "4", "nom" : "Olaf", "ATK" : "100", "DEF" : "100", "PV" : "500"},
              {"id" : "5", "nom" : "Dr.Mundo", "ATK" : "100", "DEF" : "100", "PV" : "500"},
              {"id" : "6", "nom" : "Viego", "ATK" : "100", "DEF" : "100", "PV" : "500"},
              {"id" : "7", "nom" : "Smolder", "ATK" : "100", "DEF" : "100", "PV" : "500"},
              {"id" : "8", "nom" : "Caytlin", "ATK" : "100", "DEF" : "100", "PV" : "500"},
              {"id" : "9", "nom" : "Yone", "ATK" : "100", "DEF" : "100", "PV" : "500"},
              {"id" : "10", "nom" : "Jax", "ATK" : "100", "DEF" : "100", "PV" : "500"}]



list_monstres = [{"id" : "1", "nom" : "Drake", "ATK" : "100", "DEF" : "100", "PV" : "500"},
                 {"id" : "2", "nom" : "Nash", "ATK" : "100", "DEF" : "100", "PV" : "500"},
                 {"id" : "3", "nom" : "Elder", "ATK" : "100", "DEF" : "100", "PV" : "500"},
                 {"id" : "4", "nom" : "void grubs", "ATK" : "100", "DEF" : "100", "PV" : "500"},
                 {"id" : "5", "nom" : "Red Buff", "ATK" : "100", "DEF" : "100", "PV" : "500"},
                 {"id" : "6", "nom" : "Blue Buff", "ATK" : "100", "DEF" : "100", "PV" : "500"},
                 {"id" : "7", "nom" : "Herald", "ATK" : "100", "DEF" : "100", "PV" : "500"},
                 {"id" : "8", "nom" : "Rapors", "ATK" : "100", "DEF" : "100", "PV" : "500"},
                 {"id" : "9", "nom" : "Gromp", "ATK" : "100", "DEF" : "100", "PV" : "500"},
                 {"id" : "10", "nom" : "Scarab", "ATK" : "100", "DEF" : "100", "PV" : "500"}]
# inserer les donner dans la table

