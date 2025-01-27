def verifier_taxes(valeur, taxe_calculee):
    indice: bool = True
    with open("../Verifications/taxes.txt", "r") as f:
        taxes_attendues = f.readlines()
        for i in range(len(taxe_calculee)):
            if taxe_calculee[i] != float(taxes_attendues[i]):
                indice = False
                print("La taxe calculée pour la marchandise de valeur", valeur[i], "est incorrecte")
                print("La taxe attendue est de", taxes_attendues[i], "alors que la taxe calculée est de", taxe_calculee[i])
            else:
                print("La taxe calculée pour la marchandise de valeur", valeur[i], "est correcte")

    if indice:
        print("Voici la clé rouge, gardienne des montagne, que je te donne pour m'avoir aider a résoudre mon "
              "problème. Mets la dans ton inventaire "
              "et garde la bien")
    else:
        print("Je suis désolé, je ne peux pas te donner de clé car tu as mal résolu mon problème. Reessaye")
