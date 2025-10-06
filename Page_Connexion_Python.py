emails = {}
emails['thomas@gmail.com'] = '123'

    
def connexion():
    while True:
        print("Connectez-vous!")
        print("Veuillez entrer votre email")
        global email_utilisateur
        email_utilisateur = input()
        global email_recherché
        email_recherché = email_utilisateur
        for email in emails:
            if email == email_recherché:
                mot_de_passe_connexion()


        if email_recherché not in emails:
            print("#### Créer votre compte ####")
            print("Veuillez entrer votre email")
            nouveau_email = input()
            print("Veuillez entrer votre mot de passe")
            nouveau_mdp = input()
            emails[nouveau_email] = nouveau_mdp
            print("Vous etes connecté")
            menu()
            
    

def mot_de_passe_connexion():
    print("Veuillez entrer votre mot de passe")
    mdp = input()

    for cle in emails:
        if emails[email_utilisateur] == mdp:
                print("Vous etes connecté")
                menu()
        else:
            print("Mauvais mot de passe")
            mot_de_passe_connexion()
  
def menu():
    while True:
        print("##########")
        print("1 - Modifier le mot de passe")
        print("2 - Supprimer le compte")
        print("3 - Se déconnecter")
        print("##########")
        selection = int(input())

        if selection == 1:
            mdp_modifier()
        elif selection == 2:
            compte_supprimer()
        elif selection == 3:
            print("Déconnecté avec succès")
            break

        else:
            print("Entrer une option valide.")
            



def mdp_modifier():
    print("Veuillez entrer votre ancien mot de passe")
    mdp = input()

    for cle in emails:
        if emails[email_utilisateur] == mdp:
                print("Veuillez entrer votre nouveau mot de passe")
                nouveau_mdp = input()
                emails[email_utilisateur] = nouveau_mdp
                print("Mot de passe à été changé")
                print("Nouveau mot de passe =", emails[email_utilisateur])
                menu()
        else:
            print("Mauvais mot de passe")
            mdp_modifier()

def compte_supprimer():
    del emails[email_utilisateur]
    print("Compte supprimé avec succès")
    input()

    

connexion()
