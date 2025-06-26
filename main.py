def addition(a, b):
    return a + b


def main(): 
    print("Test de la fonction addition(2, 3)")
    resultat = addition(2, 3)
    print(f"Résultat obtenu : {resultat}")
    assert resultat == 5
    print("Test addition réussi\n")


if __name__ == "__main__":
    main()


