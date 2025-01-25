from Verifications.Verification_ex_1 import verifier_taxes


# Ajoute les conditions pour calculer la taxe et retourne cette valeur
def calculer_taxe(val: int) -> float:
    taxe: float = 0
    if val <= 100:
        taxe = val * 0.05
    elif 101 <= val <= 1000:
        taxe = val * 0.1
    else:
        taxe = val * 0.15
    return taxe


if __name__ == '__main__':

    # Permet de tester le code automatiquement
    # NE PAS TOUCHER !
    marchandises: list = [50, 200, 1500, 75, 100]
    valeur_taxe: list = []

    # Crée une liste de valeur_taxe en utilisant la fonction calculer_taxe
    for valeur in marchandises:
        valeur_taxe.append(calculer_taxe(valeur))

    # Vérifie si les valeurs de valeur_taxe sont correctes
    verifier_taxes(marchandises, valeur_taxe)
