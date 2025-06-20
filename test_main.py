from main import addition, soustraction

def test_addition():
    print("Test de la fonction addition(2, 3)")
    resultat = addition(2, 3)
    print(f"Résultat obtenu : {resultat}")
    assert resultat == 5
    print("Test addition réussi\n")

def test_soustraction():
    print("Test de la fonction soustraction(5, 3)")
    resultat = soustraction(5, 3)
    print(f"Résultat obtenu : {resultat}")
    assert resultat == 2
    print("Test soustraction réussi\n")
