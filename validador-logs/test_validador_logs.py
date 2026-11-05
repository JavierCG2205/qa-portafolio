from validador_logs import contar_errores

def test_contar_errores():
    lineas = [
        "INFO: Servidor iniciado",
        "ERROR: No se pudo conectar",
        "INFO: Usuario entró",
        "ERROR: Archivo no encontrado",
    ]
    assert contar_errores(lineas) == 2

def test_lineas_vacias():
    lineas_vacias = []
    assert contar_errores(lineas_vacias) == 0

def test_lineas_sin_errores():
    lineas_sin_errores = [
        "INFO: Servidor iniciado",
        "INFO: Usuario entró",
    ]
    assert contar_errores(lineas_sin_errores) == 0

  