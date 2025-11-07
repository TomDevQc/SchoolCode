def statistiques_completes():
    global toutes_les_equipes

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
