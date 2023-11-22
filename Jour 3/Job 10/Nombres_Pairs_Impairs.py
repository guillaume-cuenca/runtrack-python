def verifier_pair_impair(nombre):
    # Vérifier si le nombre est un entier positif
    if isinstance(nombre, int) and nombre >= 0:
        # Vérifier si le nombre est pair ou impair
        if nombre % 2 == 0:
            return f"{nombre} est un nombre pair."
        else:
            return f"{nombre} est un nombre impair."
    else:
        return "Veuillez entrer un nombre entier positif."

# Appeler la fonction avec différentes valeurs
resultat1 = verifier_pair_impair(10)
resultat2 = verifier_pair_impair(7)
resultat3 = verifier_pair_impair(25)
resultat4 = verifier_pair_impair(-3)
resultat5 = verifier_pair_impair(15.5)

# Afficher les résultats
print(resultat1)
print(resultat2)
print(resultat3)
print(resultat4)
print(resultat5)