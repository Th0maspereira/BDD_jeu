#importer de game.py le score
from random import choice
#from game import startgame


# MENU = [
#   "Lancer Jeu",
#   "Afficher les scores",
#   "Quitter",
#    ]
# Menu
#   Boucle sur tout element de MENU
#       afficher numero element et texte element
def showmenu():
    print("Voici le menu principale "
          "\n   vous avez le choix entre")
    print("1. Lancer le jeu")
    print("2. Afficher les scores")
    print("3. Quitter")

# Choix (options, mistake)
#    while True:
#        Recuperer choix utilisateur
#        Verifier si choix est valide
#        Si valide
#             return choix
#        Sinon
#             Lancer fonction mistake
def isvalide(choice):
    if choice in ["1", "2", "3"]:
        return True
    else:
        mistake()


def getchoice():
    while True :
        choiceuser = input("Veuillez entrer votre choix : ")
        if isvalide(choiceuser):
            return int(choiceuser)

def choice_menu():
    choice = getchoice()
    if choice == 1:
        print("le jeu va commencer")
        startgame()
    elif choice == 2:
        print("Voici le leaderboard")
        showleaderboard()
    elif choice == 3:
        print("fermeture du jeu")
        quitgame()


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
    showmenu()


showmenu()
choice_menu()

