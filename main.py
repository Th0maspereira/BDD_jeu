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
# Process
#    JEU
#       Pseudo du joueur
#           boucle infini
#               demander un pseudo
#               si pseudo valide 
#                   return pseudo
#
#       creer une equipe
#       recuperer les heros et leur caracteristique 
#           ouvrir la bdd
#           acceder a la collection heros
#           recuperer les lignes des heros
#       ouvrir la table equipe 
#       on la clear
#        une boucle tant que l'equipe < 3   
#           afficher le resultat
#           demander de selectionner un heros dans la table
#               recuperer son choix 
#                   verifier si il est valide
#                       si oui selectionner le heros 
#                           le retirer des choix possible
#                           ajouter a equipe
#                       sinon
#                           lancer la fonction erreur
#
#       boucle infini pour les vagues/combats
#           recuperer l'equipe du joueur
#           choisir un ennemie dans la base en random
#           
#
#
#
#
#
#
#
#
#       afficher l'equipe
#           ouvrir la db equipe
#           recuperer
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
#    Quitter
#       sys.exit()


#fonction is_valid
#   si
#       nom > 3 caractere  
#       nom < 25 caractere
#       nom != de ceux dans la db
#   sinon
#       lancer la fonction erreur 