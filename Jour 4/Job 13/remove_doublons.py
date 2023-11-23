def supprimer_doublons(liste):
    liste_sans_doublons = []

    for element in liste:
        if element not in liste_sans_doublons:
            liste_sans_doublons.append(element)

    return liste_sans_doublons

# Exemple d'utilisation
ma_liste = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

# Afficher la liste avant la suppression des doublons
print("Liste avant la suppression des doublons :", ma_liste)

# Appeler la fonction pour supprimer les doublons
resultat = supprimer_doublons(ma_liste)

# Afficher la liste après la suppression des doublons
print("Liste après la suppression des doublons :", resultat)