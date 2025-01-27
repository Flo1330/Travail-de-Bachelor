from Verifications.Verification_mission_2A import verifier_mdp, verifier_couleur_cle


def ouvrir_porte(torche: bool):
    couleur_cle: str = input("Quelle est la couleur de la clé ? ")
    if verifier_couleur_cle(couleur_cle) and torche:
        mot_utilisateur: str = input("Entre le mot de passe : ")
        if verifier_mdp(mot_utilisateur):  # Vérifie le mot de passe
            print("La porte s'ouvre. Bonne ascension, pirate !")
        else:
            print("Mot de passe incorrect. La porte reste fermée.")
    else:
        print("Tu n'as pas la bonne clé ou la torche allumée. La porte reste fermée.")


if __name__ == '__main__':

    etat_torche: bool = True  # La torche du joueur est allumée
    ouvrir_porte(etat_torche)
