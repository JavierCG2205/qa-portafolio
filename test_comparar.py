def comparar(esperado, obtenido):
    if esperado == obtenido:
        return "PASS"
    else:
        return "FAIL"


def test_cuando_son_iguales():
    assert comparar("ok", "ok") == "PASS"


def test_cuando_son_diferentes():
    assert comparar("ok", "error") == "FAIL"


def test_con_numeros():
    assert comparar(5, 5) == "PASS"
    
def test_con_numeros_diferentes():
    assert comparar(5, 6) == "FAIL"
    