def est_separateur(caractere):
    # Fonction pour vérifier si un caractère est un séparateur
    return caractere == ' ' or caractere == ',' or caractere == '.' or caractere == ';' or caractere == ':'

def my_long_word(longueur_min, chaine):
    mot_courant = ""
    result = ""

    for caractere in chaine:
        if est_separateur(caractere):
            if len(mot_courant) > longueur_min:
                result += mot_courant + " "
            mot_courant = ""
        else:
            mot_courant += caractere

    # Vérifier le dernier mot après la boucle
    if len(mot_courant) > longueur_min:
        result += mot_courant

    return result.strip()

# Exemple d'utilisation
longueur_minimale = 3
phrase = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"

# Appeler la fonction et afficher le résultat
resultat = my_long_word(longueur_minimale, phrase)
print(resultat)