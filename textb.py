def resultats_equipe():
    global equipe

    if equipe == {}:
        print("Aucune donnée enregistrée. Choisis A d'abord.")
        return

    print("\n--- Résultats de l'équipe", equipe["nom"], "---")

    h = equipe["hauteur"]
    temps = equipe["temps"]
    n = equipe["nb_essais"]

    # Calcul des accélérations
    accelerations = []
    for t in temps:
        a = 2 * h / (t ** 2)
        accelerations.append(a)

    # Stocker dans le dictionnaire si tu veux réutiliser ailleurs
    equipe["accelerations"] = accelerations

    # Moyenne
    a_moy = sum(accelerations) / len(accelerations)

    # Incertitudes
    inc_absolue = max(accelerations) - min(accelerations)
    inc_relative = (inc_absolue / a_moy) * 100

    # % écart avec théorie
    ecart = abs(a_moy - VALEUR_THEORIQUE) / VALEUR_THEORIQUE * 100

    print("\nTemps   | Accélération (m/s^2)")
    print("-------------------------------")
    for i in range(n):
        print(f"{temps[i]:>6} | {accelerations[i]:.3f}")

    print("\nAccélération moyenne :", round(a_moy, 3))
    print("Incertitude absolue  :", round(inc_absolue, 3))
    print("Incertitude relative :", round(inc_relative, 2), "%")
    print("Pourcentage d'écart  :", round(ecart, 2), "%")
