def verifier_mdp(mdp_essai: str) -> bool:
    mdp_vrai = "2R3G2Q5A3S"

    if mdp_essai == mdp_vrai:
        print("Le mot de passe est correct, prends cette carte elle te sera utile pour la suite !")
        return True
    else:
        print("Demande de  l'aide sur la plage, je crois que quelqu'un connait le code secret.")
        return False


def verifier_couleur_cle(couleur: str) -> bool:
    if couleur.lower() == "rouge":
        print("Bonne couleur de clé, continue")
        return True
    else:
        return False
