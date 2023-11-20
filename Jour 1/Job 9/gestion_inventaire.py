class Produit:
    def __init__(self, nom, prix_unitaire, quantite_en_stock):
        self.nom = nom
        self.prix_unitaire = prix_unitaire
        self.quantite_en_stock = quantite_en_stock

    def afficher_informations(self):
        print(f"Produit : {self.nom}")
        print(f"Prix unitaire : {self.prix_unitaire} euros")
        print(f"Quantité en stock : {self.quantite_en_stock}")

    def ajouter_stock(self, quantite_achetee):
        self.quantite_en_stock += quantite_achetee
        print(f"{quantite_achetee} {self.nom}(s) ajouté(s) au stock.")
        print(f"Nouvelle quantité en stock : {self.quantite_en_stock}")

    def mise_a_jour_prix(self):
        self.prix_unitaire *= 1.1  # Augmentation de 10%
        print(f"Le prix unitaire a été mis à jour. Nouveau prix : {self.prix_unitaire} euros")

produit_initial = Produit("Ordinateur portable", 800, 50)

print("Informations initiales du produit :")
produit_initial.afficher_informations()

quantite_achetee = int(input("Combien d'unités souhaitez-vous acheter ? "))
produit_initial.ajouter_stock(quantite_achetee)

produit_initial.mise_a_jour_prix()

print("\nInformations mises à jour du produit :")
produit_initial.afficher_informations()