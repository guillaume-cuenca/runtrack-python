def type_triangle(a, b, c):
    # Vérification si les longueurs forment un triangle
    if a + b > c and b + c > a and c + a > b:
        # Vérification du type de triangle
        if a == b == c:
            return "Equilatéral"
        elif a == b or b == c or c == a:
            return "Isocèle"
        elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
            return "Rectangle"
        else:
            return "Quelconque"
    else:
        return "Impossible de former un triangle"

# Demander à l'utilisateur les longueurs
a = float(input("Entrez la longueur a : "))
b = float(input("Entrez la longueur b : "))
c = float(input("Entrez la longueur c : "))

# Appeler la fonction et afficher le résultat
resultat = type_triangle(a, b, c)
print(f"Le triangle est de type : {resultat}")