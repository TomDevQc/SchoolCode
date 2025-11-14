## Thomas Power et Zack-Antoine Grenier
## TP2 - Programme de laboratoire de physique
## 2025-11-07






def menu():                                                             ## -- MENU D'ACCUEIL --
    """
    la fonction va demander à l'utilisateur le choix de ce qu'il veut faire avec le programme

    parameters
    ----------
    choix a
        entrer données
    choix b
        résultats équipes
    choix c
        statistique complète
    choix d
        quitter le programme
    """
    choix = ""
    while True:
        print("======== MENU ========")
        print("a. Entrer des données.")
        print("b. Voir les résultats pour un laboratoire.")
        print("c. Statistique complète")
        print("d. Quitter le programme")
        print("======================")
        choix = str(input("Quelle action souhaitez-vous faire? "))
    
        if choix == "a":
            entrer_donnees()
        elif choix == "b":
            resultats_equipe()
        elif choix == "c":
            statistiques_completes()
        elif choix == "d":
            break
        else:
            print("Choix invalide: Réessayez")


def entrer_donnees():                                                   ## -- Entrer données --
    """
    lorsque choix a est choisi, le programme va demander les informations à l'utilisateur.
    Le programme va ensuite enregistrer les données afin de potentiellement les utiliser plus tard
    """
    
    

    while True:
        nom = input("Nom de l'équipe: ")
        if nom.isalpha():
            equipe["nom"] = nom
            break
        else:
            print("Le nom doit seulement contenir des lettres.")

    while True:
        try:
            h= float(input("Hauteur de l'expérience (1 à 5 m): "))
            if 1 <= h <= 5:
                equipe["hauteur"] = h
                break
            else:
                print("La hautuer doit être entre 1 et 5 m")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

    while True:
        try:
            nb= int(input("Nombre d'essais (5 à 10): "))
            if 5 <= nb <= 10:
                equipe["nb_essais"] = nb
                break
            else:
                print("Le nombre d'essais doit être entre 5 et 10")
        except ValueError:
            print("Veuillez entrer un entier valide.")

    temps = []
    for i in range(equipe["nb_essais"]):
        while True:
            try:
                t = float(input(f"Temps de chute #{i + 1} (> 0) : "))
                if t > 0:
                    temps.append(t)
                    break
                else:
                    print("le temps dois être positif.")
            except ValueError:
                print("Entrez un temps valide.")
    equipe["temps"] = temps

    print("Données enregistrées au registre pour l'équip: ", equipe["nom"])
    toutes_les_equipes.append(equipe.copy())

def resultats_equipe():                                           ## -- Afficher Résultats Equipe --
    """
    Le programme va premièrement afficher les résultats des équipes, ensuite va calculer toutes les données entrées par l'utilisateur.
    Finalement, le programme va afficher les données de l'équipe

    parameters
    ----------
    pour chaque données dans toutes_les_equipes
        afficher le nom de l'équipe et leurs données
    """

    if len(toutes_les_equipes) == 0:
        print("Aucune équipe enregistrée.")
        return

    print("\n--- Liste des équipes enregistrées ---")
    for i, eq in enumerate(toutes_les_equipes):
        print(f"{i+1}. {eq['nom']}")

    # Choisir l'équipe
    while True:
        try:
            choix = int(input("Numéro de l'équipe à afficher : "))
            if 1 <= choix <= len(toutes_les_equipes):
                break
            else:
                print("Numéro invalide.")
        except ValueError:
            print("Entre un NUMÉRO valide.")

    equipe = toutes_les_equipes[choix - 1]

    # ----- CALCULS -----
    h = equipe["hauteur"]
    temps = equipe["temps"]
    n = equipe["nb_essais"]

    # accélérations
    accelerations = [2 * h / (t**2) for t in temps]
    a_moy = sum(accelerations) / len(accelerations)
    inc_abs = max(accelerations) - min(accelerations)
    inc_rel = (inc_abs / a_moy) * 100
    ecart = abs(a_moy - VALEUR_THEORIQUE) / VALEUR_THEORIQUE * 100

    # ----- AFFICHAGE -----
    print(f"\n=== Résultats pour l'équipe : {equipe['nom']} ===")
    print("Hauteur réelle :", h, "m")

    print("\nTemps   | Accélération (m/s²)")
    print("------------------------------")
    for i in range(n):
        print(f"{temps[i]:>6} | {accelerations[i]:.3f}")

    print("\nAccélération moyenne :", round(a_moy, 3))
    print("Incertitude absolue  :", round(inc_abs, 3))
    print("Incertitude relative :", round(inc_rel, 2), "%")
    print("Pourcentage d'écart  :", round(ecart, 2), "%")

def statistiques_completes():                                     ## -- Afficher Résultats Completes --
    """
    Le programme va calculer encore certaine données tel que l'acclélération, va ensuite stocker les données avant d'afficher les statistiques complètes
    des équipes à l'aide des données tout fraichement calculées ou encoretoutes les données précédemment calculées.
  """
  

    if len(toutes_les_equipes) == 0:
        print("Aucune équipe enregistrée.")
        return

    print("\n===== STATISTIQUES DE TOUTES LES ÉQUIPES =====")

    liste_a_moy = []
    liste_h = []
    liste_inc_abs = []
    liste_inc_rel = []
    liste_ecarts = []

    for eq in toutes_les_equipes:
        h = eq["hauteur"]
        temps = eq["temps"]

        # calcul accélérations
        accelerations = [2 * h / (t**2) for t in temps]

        a_moy = sum(accelerations) / len(accelerations)
        inc_abs = max(accelerations) - min(accelerations)
        inc_rel = (inc_abs / a_moy) * 100
        ecart = abs(a_moy - VALEUR_THEORIQUE) / VALEUR_THEORIQUE * 100

        # afficher résultats de l'équipe
        print("\n---", eq["nom"], "---")
        print("Hauteur réelle :", h)
        print("Accélération moyenne :", round(a_moy, 3))
        print("Incertitude absolue :", round(inc_abs, 3))
        print("Incertitude relative :", round(inc_rel, 2), "%")
        print("% écart :", round(ecart, 2), "%")

        # stocker pour statistiques globales
        liste_a_moy.append(a_moy)
        liste_h.append(h)
        liste_inc_abs.append(inc_abs)
        liste_inc_rel.append(inc_rel)
        liste_ecarts.append(ecart)

    # ---- Statistiques Globales ----
    print("\n===== RÉSUMÉ GLOBAL =====")
    print("Hauteur moyenne globale :", round(sum(liste_h) / len(liste_h), 3))
    print("Accélération moyenne globale :", round(sum(liste_a_moy)/len(liste_a_moy), 3))
    print("Plus grande incertitude absolue :", round(max(liste_inc_abs), 3))
    print("Plus grande incertitude relative :", round(max(liste_inc_rel), 2), "%")
    print("% d'écart moyen :", round(sum(liste_ecarts)/len(liste_ecarts), 2), "%")




# Début programme

# Constante
VALEUR_THEORIQUE = 9.8 #m/s^2

# Dictionnaire
equipe = {}
toutes_les_equipes = []

menu()
