def time_to_text(minutes):
    # Vérifier si le nombre est un entier positif
    if isinstance(minutes, int) and minutes >= 0:
        # Calculer le nombre d'heures et de minutes
        heures = minutes // 60
        minutes_restantes = minutes % 60

        # Construire la chaîne de caractères avec un format spécifique
        if heures == 1:
            heure_str = "heure"
        else:
            heure_str = "heures"

        if minutes_restantes == 1:
            minute_str = "minute"
        else:
            minute_str = "minutes"

        # Afficher la chaîne de caractères
        resultat = f"{heures} {heure_str} et {minutes_restantes} {minute_str}"
        print(resultat)
    else:
        print("Veuillez entrer un nombre entier positif.")

# Appeler la fonction avec différentes valeurs
time_to_text(160)
time_to_text(75)
time_to_text(45)
time_to_text(120)
time_to_text(-30)
time_to_text(90.5)