def trier_pierres(pierres) -> str:
    # Initialiser les compteurs pour chaque catégorie
    rubis: int = 0
    grenat: int = 0
    quartz: int = 0
    amethyste: int = 0
    saphir: int = 0

    # Parcourir chaque pierre
    for pierre in pierres:
        couleur, eclat, taille, transparence, poids = pierre  # Décomposer les attributs

        # Ajouter votre code ici
        if couleur == "rouge" and eclat == "brillant":
            if transparence == "élevée":
                if taille > 50:
                    rubis += 1
                else:
                    grenat += 1
            elif transparence == "faible":
                if poids > 30:
                    grenat += 1
                else:
                    amethyste += 1
        elif couleur == "bleu" and eclat == "brillant":
            if transparence == "moyenne":
                if taille == 40:
                    quartz += 1
                elif poids > 20:
                    saphir += 1
                else:
                    amethyste += 1
            else:
                if taille > 50:
                    saphir += 1
                else:
                    amethyste += 1
        else:
            if transparence == "faible" or poids < 10:
                amethyste += 1
            else:
                quartz += 1

    # Générer le code secret
    mot_de_passe = f"{rubis}R{grenat}G{quartz}Q{amethyste}A{saphir}S"
    return mot_de_passe


if __name__ == '__main__':
    pierres = [
        ("rouge", "brillant", 55, "élevée", 35),  # Rubis
        ("rouge", "brillant", 45, "élevée", 25),  # Grenat
        ("rouge", "brillant", 45, "faible", 40),  # Grenat
        ("bleu", "brillant", 40, "moyenne", 18),  # Quartz
        ("bleu", "brillant", 35, "moyenne", 25),  # Saphir
        ("bleu", "brillant", 60, "faible", 50),  # Saphir
        ("vert", "mat", 20, "faible", 8),  # Améthyste
        ("rouge", "brillant", 50, "élevée", 30),  # Grenat
        ("bleu", "brillant", 50, "élevée", 30),  # Améthyste
        ("bleu", "brillant", 50, "moyenne", 15),  # Améthyste
        ("rouge", "brillant", 55, "faible", 20),  # Améthyste
        ("rouge", "brillant", 60, "élevée", 40),  # Rubis
        ("bleu", "brillant", 55, "faible", 35),  # Saphir
        ("vert", "brillant", 30, "faible", 10),  # Améthyste
        ("rouge", "mat", 50, "moyenne", 12),  # Quartz
    ]

    code_secret = trier_pierres(pierres)
    print(f"Le code secret est : {code_secret}")
