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
#       afficher l'equipe
#           ouvrir la db equipe
#           recuperer
#
#       choisir un ennemie dans la base en random
#
#       boucle infini pour les vagues/combats
#              lancer la function monstersrandom
#           les heros attaque
#           boucle par heros vivant
#               ouvrir la base equipe
#               repucuperer sont attaque
#               ouvrir la base monstres
#               recuperer hp est defense de l'actuel ennemie
#               retirer att heros a hp mpnstre en fonction de la reductions de la def
#               si hp monstre <= 0 
#                   ajouter 1 au score
#                   quiter boucle et revenir au debut de la boucle combat pour choisir un nouveau monstre 
#           l'ennemie attaque
#               ouvrir la base monstres
#               repucuperer sont attaque
#               ouvrir la base equipe
#               recuperer hp est defense des heros 
#                   si heros hp > 0
#                       choisir un des heros vivant
#                       retirer att monstres a hp heros en prenand en compte la rdm du heros avec ca def
#                   sinon quit
#               retirer att monstres a hp du heros choisi
#
#
#               finir jeu
#           recuperer le score
#           le mettre dans la table score
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
#fonction monstersrandom
#   ouvrir table monstre
#   recuperer un monstre au hasard 
#   print votre ennemie sera
#   afficher monstres choisi et stats
#