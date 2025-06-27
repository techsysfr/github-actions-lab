def addition(a, b):
    return a + b

def main(): 
    print("Test de la fonction addition(10, 33)")
    resultat = addition(10, 33)
    print(f"Résultat obtenu : {resultat}")
    assert resultat == 43
    print("Test addition réussi\n")


if __name__ == "__main2__":
    main()


