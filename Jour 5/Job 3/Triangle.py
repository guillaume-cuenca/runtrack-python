def afficher_triangle(hauteur):
    for i in range(hauteur):
        # Affiche les espaces à gauche du triangle
        for j in range(hauteur - i - 1):
            print(" ", end="")
        
        # Affiche les caractères du côté gauche du triangle
        print("/", end="")
        for j in range(2 * i):
            print("_", end="")
        print("\\")
        
# Demander à l'utilisateur d'entrer la hauteur du triangle
hauteur = int(input("Entrez la hauteur du triangle : "))

# Appeler la fonction pour afficher le triangle
afficher_triangle(hauteur)