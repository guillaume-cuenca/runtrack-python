def remplacer_element_par_somme(L, index):
    L[index] = L[index - 1] + L[index + 1]

# Création d'une liste d'au moins 5 entiers
L = [1, 2, 3, 4, 5]

# Afficher la deuxième valeur de la liste
deuxieme_valeur = L[1]
print("Deuxième valeur de la liste :", deuxieme_valeur)

# Appeler la fonction pour remplacer L[3] par la somme des cases voisines L[2] et L[4]
remplacer_element_par_somme(L, 3)
print("Liste après la modification :", L)

# Afficher la dernière valeur de la liste
derniere_valeur = L[-1]
print("Dernière valeur de la liste :", derniere_valeur)