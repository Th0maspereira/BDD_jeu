#importer de game.py le score 
#
# MENU = [
#   "Lancer Jeu",
#   "Afficher les scores",
#   "Quitter",
#    ]
# Menu
#   Boucle sur tout element de MENU
#       afficher numero element et texte element
# Choix (options, erreur)
#    while True:
#        Recuperer choix utilisateur
#        Verifier si choix est valide
#        Si valide
#             return choix
#        Sinon
#             Lancer fonction erreur
#
#    Afficher les scores
#        Recuperer scores base
#            ouvrir base
#            acceder a collection score
#            find
#            convertir curseur en list
#        filtrer les 3 meilleurs
#             trie le tableau sur element.waves
#             prendre 3 derniers elements
#                    array[-3:-1]
#        Affiche les score
#               si le score n'est pas dans le leaderboard
#                   afficher score du joueur 
#
#    Quitter
#       sys.exit()


#fonction is_valid
#   si
#       nom > 3 caractere  
#       nom < 25 caractere
#       nom != de ceux dans la db
#   sinon
#       lancer la fonction erreur 
#
