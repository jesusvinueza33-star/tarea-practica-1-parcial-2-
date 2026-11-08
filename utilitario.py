import os

def borrar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("  Debe ser un número entero.")

def menu(titulo,opciones):
    print(f"\n========== {titulo} ==========")
    for opcion in opciones:
       print(f"{opcion}")
    lon = len(opciones)-1
    return input(f"Opción[0...{lon}]: ").strip().upper()


if __name__ == "__main__":
    opc = menu("menu principal", ["1) pila" , "2) colas","0) salir "])
    opc1 = menu("menu pilas", ["1) entrar a la pila" , "2) listar" , "3) desapilar", "4)cargar datos de pruebas "])
    opc1 = menu("menu colas", [])