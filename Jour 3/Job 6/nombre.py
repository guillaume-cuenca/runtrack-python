def check_sign(nombre):
    if nombre > 0:
        print("positif")
    elif nombre < 0:
        print("negatif")
    else:
        print("nul")

# Appels de la fonction avec des paramètres différents
check_sign(5)
check_sign(-3)
check_sign(0)