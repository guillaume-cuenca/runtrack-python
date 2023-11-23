def tri_insertion_croissant(liste):
    for i in range(1, len(liste)):
        cle = liste[i]
        j = i - 1
        while j >= 0 and cle < liste[j]:
            liste[j + 1] = liste[j]
            j -= 1
        liste[j + 1] = cle

# Exemple d'utilisation
ma_liste = [7, 11, 42, 39, 2]

# Afficher la liste avant le tri
print("Liste avant le tri :", ma_liste)

# Appeler la fonction pour trier la liste dans l'ordre croissant
tri_insertion_croissant(ma_liste)

# Afficher la liste après le tri
print("Liste après le tri croissant :", ma_liste)