while True:
    try:
        N = int(input("Veuillez entrer un entier N supérieur à zéro : "))
        if N > 0:
            break
        else:
            print("Veuillez entrer un entier supérieur à zéro.")
    except ValueError:
        print("Veuillez entrer un nombre entier valide.")

for i in range(1, N + 1):
    print(f"\nTable de multiplication pour {i} :")
    for j in range(1, 11):
        result = i * j
        print(f"{i} * {j} = {result}")