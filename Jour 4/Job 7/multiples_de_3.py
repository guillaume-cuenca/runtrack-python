def compter_multiples_de_trois(liste):
    nombre_multiples_de_trois = 0

    for nombre in liste:
        if nombre % 3 == 0:
            nombre_multiples_de_trois += 1

    return nombre_multiples_de_trois

# Liste donnée
L = [8, 24, 48, 2, 16]

# Appeler la fonction pour compter le nombre de multiples de 3 dans la liste
resultat = compter_multiples_de_trois(L)

# Afficher le résultat
print("Le nombre de multiples de 3 dans la liste est :", resultat)