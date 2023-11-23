def tri_insertion_croissant(liste):
    for i in range(1, len(liste)):
        cle = liste[i]
        j = i - 1
        while j >= 0 and cle < liste[j]:
            liste[j + 1] = liste[j]
            j -= 1
        liste[j + 1] = cle

def arrondir_et_trier(liste):
    for i in range(len(liste)):
        # Convertir chaque élément en entier après l'arrondi
        liste[i] = int(liste[i] + 0.5)

    tri_insertion_croissant(liste)

# Liste donnée
ma_liste = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

# Afficher la liste avant l'arrondi et le tri
print("Liste avant l'arrondi et le tri :", ma_liste)

# Appeler la fonction pour arrondir les nombres et les trier
arrondir_et_trier(ma_liste)

# Afficher la liste après l'arrondi et le tri
print("Liste après l'arrondi et le tri croissant :", ma_liste)