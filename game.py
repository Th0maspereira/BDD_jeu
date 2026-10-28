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
#fonction monstersrandom
#   ouvrir table monstre
#   recuperer un monstre au hasard 
#   print votre ennemie sera
#   afficher monstres choisi et stats
#