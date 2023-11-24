def chiffrement_cesar(message, decalage):
    resultat = ""

    for caractere in message:
        if caractere.isalpha():  # Vérifie si le caractère est une lettre
            if caractere.isupper():  # Si c'est une lettre majuscule
                resultat += chr((ord(caractere) - ord('A') + decalage) % 26 + ord('A'))
            else:  # Si c'est une lettre minuscule
                resultat += chr((ord(caractere) - ord('a') + decalage) % 26 + ord('a'))
        else:
            resultat += caractere  # Ajoute le caractère tel quel s'il n'est pas une lettre

    return resultat

# Exemple d'utilisation avec un message et un décalage de 3
message_original = "Bonjour, Jules Cesar"
decalage = 3
message_chiffre = chiffrement_cesar(message_original, decalage)

print("Message original:", message_original)
print("Message chiffré:", message_chiffre)