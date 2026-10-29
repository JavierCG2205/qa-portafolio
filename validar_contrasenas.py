contraseñas = ["abc", "Segura2026", "12345678", "hola", "MiClave123"]
validas = 0

for contraseña in contraseñas:
    if len(contraseña) >= 8:
        print(f"{contraseña} VALIDA")
        validas += 1
    else:
        print(f"{contraseña} INVALIDA")
        
print(f"Validas {validas} de {len(contraseñas)}")
