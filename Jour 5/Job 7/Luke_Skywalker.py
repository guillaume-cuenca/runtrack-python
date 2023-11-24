def arrondir_notes(liste_notes):
    notes_arrondies = []

    for note in liste_notes:
        if note < 40:
            notes_arrondies.append(note)  # Les étudiants ayant moins de 40 échouent sans arrondi
        else:
            difference = 5 - (note % 5)
            if difference < 3:
                notes_arrondies.append(note + difference)
            else:
                notes_arrondies.append(note)

    return notes_arrondies

# Exemple d'utilisation
notes_etudiants = [37, 42, 83, 78, 95]
notes_arrondies = arrondir_notes(notes_etudiants)

# Affichage du résultat
print("Notes des étudiants :", notes_etudiants)
print("Notes arrondies :", notes_arrondies)