def recuperer_info_liste(liste):
    if not liste:  # Vérifier si la liste est vide
        return None, None, None

    valeur = liste[0]
    maximum = minimum = valeur

    for nombre in liste[1:]:
        if nombre > maximum:
            maximum = nombre
        elif nombre < minimum:
            minimum = nombre

    return valeur, maximum, minimum

# Liste donnée
L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

# Appeler la fonction pour récupérer la valeur, le maximum et le minimum
valeur, maximum, minimum = recuperer_info_liste(L)

# Afficher les résultats
print("Valeur :", valeur)
print("Maximum :", maximum)
print("Minimum :", minimum)