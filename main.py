#importer de game.py le score
from game import startgame


# MENU = [
#   "Lancer Jeu",
#   "Afficher les scores",
#   "Quitter",
#    ]
# Menu
def showmenu():
    print("Voici le menu principale "
          "\n   vous avez le choix entre")
    print("1. Lancer le jeu")
    print("2. Afficher les scores")
    print("3. Quitter")
def choix_menu(startgame, showleaderboard, quitgame, mistake):
    while True:
        choix = input("Veuillez entrer votre choix : ")
        if choix == "1":
            startgame()
            break
        elif choix == "2":
            showleaderboard()
            break
        elif choix == "3":
            quitgame()
            break
        else:
            mistake()
#   Boucle sur tout element de MENU
#       afficher numero element et texte element
# Choix (options, mistake)
#    while True:
#        Recuperer choix utilisateur
#        Verifier si choix est valide
#        Si valide
#             return choix
#        Sinon
#             Lancer fonction mistake
#
#    Afficher les scores option (2)
def showleaderboard():
    pass
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
#    Quitter option (3)
#       sys.exit()
def quitgame ():
    exit()

def mistake():
    print("Votre choix n'est pas valide veuillez en entrer un qui le soit")
    pass

showmenu()
