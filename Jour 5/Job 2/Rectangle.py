def draw_rectangle(width, height):
    for i in range(height):
        if i == 0 or i == height - 1:
            # Première et dernière ligne : ligne horizontale
            print('-' * width)
        else:
            # Lignes internes : côté vertical à chaque extrémité
            print('|' + ' ' * (width - 2) + '|')

# Exemple d'utilisation avec width=10 et height=3
draw_rectangle(10, 3)