def my_sort(lst):
    n = len(lst)
    coups = 0  # Initialiser le compteur de coups à 0
    trie = False  # Un indicateur pour savoir si la liste est triée

    while not trie:
        trie = True  # Supposons que la liste est triée
        for i in range(n - 1):
            if lst[i] > lst[i + 1]:
                # Échange d'éléments si l'élément actuel est plus grand que l'élément suivant
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                coups += 1  # Incrémenter le compteur de coups
                trie = False  # La liste n'est pas triée, continuez le tri

    # Afficher le nombre total de coups nécessaires pour trier la liste
    print("Nombre total de coups nécessaires :", coups)

    return lst  # Retourner la liste triée

# Exemple d'utilisation
ma_liste = [5, 3, 8, 2, 1, 7, 4, 6]
liste_triee = my_sort(ma_liste)

# Affichage du résultat
print("Liste triée :", liste_triee)