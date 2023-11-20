montant_initial = 10000
taux_rendement_annuel = 5

gain_annuel = (taux_rendement_annuel / 100) * montant_initial
print(f"Gain annuel initial : {gain_annuel} euros")

montant_initial += 5000
taux_rendement_annuel += 2

nouveau_gain_annuel = (taux_rendement_annuel / 100) * montant_initial
print(f"Nouveau gain annuel : {nouveau_gain_annuel} euros")

retrait = 0.10 * montant_initial
montant_initial -= retrait
taux_rendement_annuel -= 1

montant_final = montant_initial + nouveau_gain_annuel

nouveau_gain = (taux_rendement_annuel / 100) * montant_final
print(f"Nouveau gain après retrait : {nouveau_gain} euros")