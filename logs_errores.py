logs = ["INFO: login ok", "WARNING: lento", "ERROR: timeout", "INFO: pago ok", "ERROR: 500", "WARNING: poca memoria"]
errores = 0
warnings = 0

for linea in logs:
    if linea.startswith("ERROR"):
        print(linea)
        errores += 1
    elif linea.startswith("WARNING"):
        warnings += 1

print(f"Total de errores: {errores}")
print(f"Total de warnings: {warnings}")
