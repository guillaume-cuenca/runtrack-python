def calcule(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Erreur: Division par zéro"
    elif operator == '%':
        if num2 != 0:
            return num1 % num2
        else:
            return "Erreur: Division par zéro"
    else:
        return "Opérateur non reconnu"

# Exemples d'appels de la fonction
result1 = calcule(5, '+', 3)
result2 = calcule(10, '*', 2)
result3 = calcule(8, '/', 4)
result4 = calcule(15, '%', 7)

# Affichage des résultats
print("Résultat 1:", result1)
print("Résultat 2:", result2)
print("Résultat 3:", result3)
print("Résultat 4:", result4)