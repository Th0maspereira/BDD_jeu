#     JEU option (1)
from db_init import initialisation_de_la_db, list_heros
from main import mistake

db = initialisation_de_la_db
#       Pseudo du joueur
#           boucle infini
#               demander un pseudo
#               si pseudo valide 
#                   return pseudo
def enterpseudo():
    while True:
        pseudo = input("Veuillez entrer votre pseudo : ")
        if (pseudo):
            is_valide(pseudo)
            return pseudo
#
#       creer une equipe
#       recuperer les heros et leur caracteristique 
#           ouvrir la bdd

    print(list_heros)
#           acceder a la collection heros
#           recuperer les lignes des heros
#       ouvrir la table equipe 
#       on la clear
list_equipe.drop()
def create_team(list_heros, list_equipe):
    while len(list_equipe) < 3:
        print("veillez selectionner un heros parmis ceux disponibles : ")
        choiceheros = input("entrez le nom du heros : ")
        if choiceheros in list_heros:
            list_equipe.append(choiceheros)
        else:
            mistake()
#        une boucle tant que l'equipe < 3   
#           afficher le resultat
#           demander de selectionner un heros dans la table
#               recuperer son choix 
#                   verifier si il est valide
#                       si oui selectionner le heros 
#                           le retirer des choix possible
#                           ajouter a equipe
#                       sinon
#                         lancer la fonction erreur
def showteam(list_equipe):
    print("Votre equipe est : ")

#       afficher l'equipe
#           ouvrir la db equipe
#           recuperer
#
#
#       boucle infini pour les vagues/combats
#              lancer la function monstersrandom
#           while hp monstres > 0
#               les heros attaque
#               boucle par heros vivant
#                   ouvrir la base equipe
#                   repucuperer sont attaque
#                   ouvrir la base monstres
#                   recuperer hp est defense de l'actuel ennemie
#                   retirer att heros a hp mpnstre en fonction de la reductions de la def
#               l'ennemie attaque
#                   ouvrir la base monstres
#                   repucuperer sont attaque
#                   ouvrir la base equipe
#                   recuperer hp est defense des heros 
#                       si heros hp > 0
#                           choisir un des heros en random parmis les vivant
#                           retirer att monstres a hp heros en prenand en compte la rdm du heros avec ca def
#                       sinon 
#                           fin jeu
#           sinon
#               finir jeu
#               recuperer le score
#               le mettre dans la table score
#        
#
#
#fonction is_valid
#   si
#       nom > 3 caractere  
#       nom < 25 caractere
#       nom != de ceux dans la db
#   sinon
#       lancer la fonction erreur
def is_valide(pseudo):
    if 3 < len(pseudo) < 25 and pseudo != db.score.find({"name": pseudo}):
        return True
    else:   
        mistake()

#
#fonction monstersrandom
#   ouvrir table monstre
#   recuperer un monstre au hasard 
#   print votre ennemie sera
#   afficher monstres choisi et stats
#   return ennemie