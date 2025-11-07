def resultats_equipe():
    global toutes_les_equipes

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
