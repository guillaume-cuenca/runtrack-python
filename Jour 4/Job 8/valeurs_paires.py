def somme_valeurs_paires(liste):
    somme = 0

    for nombre in liste:
        if nombre % 2 == 0:
            somme += nombre

    return somme

# Liste donnée
L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

# Appeler la fonction pour calculer la somme des valeurs paires dans la liste
resultat = somme_valeurs_paires(L)

# Afficher le résultat
print("La somme des valeurs paires dans la liste est :", resultat)