def ajouter_mangue():
    fruits = ["pomme", "cerise", "orange, Melon"]
    
    # Utilisation de la méthode insert pour ajouter "Mangue" à l'index 2
    fruits.insert(2, "Mangue")
    
    return fruits

# Appel de la fonction et affichage du résultat
resultat = ajouter_mangue()
print(resultat)