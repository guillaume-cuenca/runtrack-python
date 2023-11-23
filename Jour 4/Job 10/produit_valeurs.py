def produit_dans_intervalle(liste, borne_min, borne_max):
    produit = 1

    for nombre in liste:
        if borne_min <= nombre <= borne_max:
            produit *= nombre

    return produit

# Liste donnée
L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

# Borne minimale et maximale
borne_min = 25
borne_max = 90

# Appeler la fonction pour calculer le produit dans l'intervalle [25, 90]
resultat = produit_dans_intervalle(L, borne_min, borne_max)

# Afficher le résultat
print(f"Le produit des valeurs dans l'intervalle [{borne_min}, {borne_max}] est :", resultat)