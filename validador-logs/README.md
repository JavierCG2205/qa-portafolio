# Validador de logs

Mini-proyecto en Python que cuenta cuántas líneas de un log son errores.

## ¿Qué hace?

La función `contar_errores(lineas)` recibe una lista de líneas de log y devuelve
cuántas empiezan con `ERROR`.

Ejemplo:

```python
from validador_logs import contar_errores

logs = [
    "INFO: Servidor iniciado",
    "ERROR: No se pudo conectar",
    "INFO: Usuario entró",
    "ERROR: Archivo no encontrado",
]

print(contar_errores(logs))  # 2
```

## Archivos

| Archivo | Para qué sirve |
|---|---|
| `validador_logs.py` | La función `contar_errores` |
| `test_validador_logs.py` | Los tests con pytest |
| `README.md` | Esta explicación |

## Cómo correrlo

1. Ten Python instalado.
2. Abre una terminal dentro de esta carpeta.
3. Corre:

```
py validador_logs.py
```

Debe imprimir `2`.

## Cómo correr los tests

1. Instala pytest (solo la primera vez):

```
py -m pip install pytest
```

2. Corre los tests:

```
py -m pytest
```

Debe decir `3 passed`.

## Casos de prueba

| Test | Qué prueba | Resultado esperado |
|---|---|---|
| `test_contar_errores` | Lista con 2 errores y 2 líneas INFO | 2 |
| `test_lineas_sin_errores` | Lista solo con líneas INFO | 0 |
| `test_lineas_vacias` | Lista vacía | 0 |

## Lo que aprendí

- La diferencia entre print y return es que print solo te muestra el resultado y return te permite usar ese resultado en algún otro código.
- Logré moverme entre carpetas en la terminal con los comandos dir (ver qué hay), cd nombre-de-carpeta (entrar) y cd .. (subir una carpeta). Con eso resolví el error de pytest “file or directory not found”, que pasaba porque la terminal estaba en una carpeta distinta a la de mis archivos.

## Autor

Javier Angel Cedillo González · Estudiante de QA Engineer · https://github.com/JavierCG2205
