def augmenter_elements_liste(liste):
    for i in range(len(liste)):
        liste[i] += 1

# Créer la liste d'entiers
L = [7, 11, 42, 39, 2]

# Afficher la liste avant la modification
print("Liste avant la modification :", L)

# Appeler la fonction pour augmenter de 1 chaque élément de la liste
augmenter_elements_liste(L)

# Afficher la liste après la modification
print("Liste après la modification :", L)