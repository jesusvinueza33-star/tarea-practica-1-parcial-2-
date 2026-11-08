from pasajero import Pasajero
from pila import MiPila
from cola import MiCola
from utilitario import leer_entero,borrar_pantalla, menu

pila = MiPila(10)
cola = MiCola(10)

def leer_pasajero():
    numero = leer_entero("  N.º de pasajero: ")
    nombre = input("  Nombre: ").strip()
    cedula = input("  Cédula: ").strip()
    edad = leer_entero("  Edad: ")
    fecha = input("  Fecha de vuelo (AAAA-MM-DD): ").strip()
    destino = input("  Destino: ").strip()
    asiento = input("  Asiento: ").strip().upper()
    return Pasajero(numero, nombre, cedula, edad, fecha, destino, asiento)

# FUNCIONES DE AYUDA 
def datos_prueba():
    """Los 5 pasajeros de prueba en ORDEN DE LLEGADA (Diana llega primero, Elena última)."""
    return [
        Pasajero(1005, "Diana", "0923456789", 22, "2026-11-15", "Quito",  "12A"),
        Pasajero(1002, "Ana",   "0912345678", 28, "2026-11-15", "Lima",   "03C"),
        Pasajero(1009, "Luis",  "0987654321", 35, "2026-11-20", "Bogotá", "18F"),
        Pasajero(1004, "Beto",  "0934567890", 16, "2026-11-20", "Quito",  "07B"),
        Pasajero(1001, "Elena", "0901234567", 41, "2026-11-22", "Lima",   "01A"),
    ]

# ---------------------- MENÚ 1 · PILA ----------------------
def menu_pila():
    while True:
        borrar_pantalla()
        op = menu("menu pilas", [
            "1) Apilar", "2) Listar", "3) Desapilar", "4) Ver tope",
            "5) Buscar", "6) Modificar", "7) Eliminar por número", "8) Copiar",
            "9) Longitud / ¿vacía?","10) Cargar datos de prueba", "0) Volver"])
        if op == "1":
            pasajero = leer_pasajero()                       # 1. LEER
            if pila.apilar(pasajero):                        # 2. LLAMAR
                print("  ✓ Apilado: ahora es el tope")       # 3. MOSTRAR
 
        elif op == "2":
            pila.listar()
 
        elif op == "3":
            salio = pila.desapilar()
            if salio is None:
                print("  ⚠ La pila está vacía")
            else:
                print(f"  ✓ Salió: {salio}")
                if pila.esta_vacia():
                    print("  La pila quedó vacía")
                else:
                    print(f"  Nuevo tope: {pila.ver_tope().nombre}")
 
        elif op == "4":
            tope = pila.ver_tope()
            if tope is None:
                print("  ⚠ La pila está vacía")
            else:
                print(f"  Tope: {tope.nombre} ({tope.numero})")
 
        elif op == "5":
            if pila.esta_vacia():
                print("  ⚠ La pila está vacía")
            else:
                numero = leer_entero("  N.º a buscar: ")
                pos = pila.buscar(numero, True)
                if pos == -1:
                    print("  No existe")
                else:
                    print(f"  Encontrado en [{pos}]: {pila.datos[pos].nombre}")
 
        elif op == "6":
            if pila.esta_vacia():
                print("  ⚠ La pila está vacía")
            else:
                numero = leer_entero("  N.º a modificar: ")
                destino = input("  Nuevo destino: ").strip()
                asiento = input("  Nuevo asiento: ").strip().upper()
                if pila.modificar(numero, destino, asiento):
                    print("  ✓ Pasajero modificado")
                else:
                    print("  No existe")
 
        elif op == "7":
            if pila.esta_vacia():
                print("  ⚠ La pila está vacía")
            else:
                numero = leer_entero("  N.º a eliminar: ")
                if pila.eliminar_por_numero(numero):
                    print("  ✓ Eliminado. Pila actual:")
                    pila.listar()
                else:
                    print("  No existe")
 
        elif op == "8":
            copia = pila.copiar()
            print("  === COPIA ===")
            copia.listar()
            print("  === ORIGINAL ===")
            pila.listar()
 
        elif op == "9":
            print(f"  Longitud: {pila.longitud()}")
            if pila.esta_vacia():
                print("  La pila está vacía")
            else:
                print("  La pila NO está vacía")

        elif op == "10":
            for p in datos_prueba():
                pila.apilar(p)
            print("  ✓ Datos de prueba apilados")
 
        elif op == "0":
            break
        else:
            print("  Opción no válida")
 
        input("\nPresione ENTER para continuar...")


# ---------------------- MENÚ 2 · COLA ----------------------
def menu_cola():
    while True:
        borrar_pantalla()
        op = menu("menu colas", ["1) encolar", "2) listar", "3) desencolar", "4) ver frente",
                    "5) buscar", "6) modificar", "7) eliminar", "8) copiar",
                    "9) longitud / ¿vacía?", "10) ordenar ascendente",
                    "11) ordenar descendente", "12) búsqueda binaria",
                    "13) cargar datos de prueba", "0) volver"])
        if op == "1":                                  # ✅ ejemplo resuelto
            pasajero = leer_pasajero()                 # 1. LEER
            if cola.encolar(pasajero):                 # 2. LLAMAR
                print("  ✓ Encolado: está al final")   # 3. MOSTRAR
        elif op == "2":
            cola.listar()
        elif op == "3":
            salio = cola.desencolar()
            if salio is None:
                print("  La cola está vacía")
            else:
                print(f"   Salió: {salio}")
                if cola.esta_vacia():
                    print("  La cola quedó vacía")
                else:
                    print(f"  Nuevo frente: {cola.ver_frente().nombre}")
        elif op == "4":
            frente = cola.ver_frente()
            if frente is None:
                print("  La cola está vacía")
            else:
                print(f"  Frente: {frente.nombre} ({frente.numero})")
        elif op == "5":
            if cola.esta_vacia():
                print("  La cola está vacía")
            else:
                numero = leer_entero("  N.º a buscar: ")
                pos = cola.buscar(numero, True)
                if pos == -1:
                    print("  No existe")
                else:
                    print(f"  Encontrado en [{pos}]: {cola.datos[pos].nombre}")
        elif op == "6":
            if cola.esta_vacia():
                print("  La cola está vacía")
            else:
                numero = leer_entero("  N.º a modificar: ")
                destino = input("  Nuevo destino: ").strip()
                asiento = input("  Nuevo asiento: ").strip().upper()
                if cola.modificar(numero, destino, asiento):
                    print("  Pasajero modificado con exito ")
                else:
                    print("  No existe")
        elif op == "7":
            if cola.esta_vacia():
                print("  La cola está vacía")
            else:
                numero = leer_entero("  N.º a eliminar: ")
                if cola.eliminar_por_numero(numero):
                    print("  Eliminado. Cola actual:")
                    cola.listar()
                else:
                    print("  No existe")
        elif op == "8":
            copia = cola.copiar()
            print("  === COPIA ===")
            copia.listar()
            print("  === ORIGINAL ===")
            cola.listar()
        elif op == "9":
            print(f"  Longitud: {cola.longitud()}")
            if cola.esta_vacia():
                print("  La cola está vacía")
            else:
                print("  La cola NO está vacía")
        elif op == "10":
            cola.ordenar_acs()
            print("  Cola ordenada de menor a mayor por número")
            cola.listar()

        elif op == "11":
            cola.ordenar_des()
            print("  Cola ordenada de mayor a menor por número")
            cola.listar()

        elif op == "12":
            if cola.esta_vacia():
                print("  La cola está vacía")
            else:
                print("  Recuerda ordenar primero (opción 10)")
                numero = leer_entero("  N.º a buscar: ")
                pos = cola.busqueda_binaria(numero)
                if pos == -1:
                    print("  No existe")
                else:
                    print(f"  Encontrado en [{pos}]: {cola.datos[pos].nombre}")
        elif op == "13":
            for p in datos_prueba():
                cola.encolar(p)
            print("   Datos de prueba encolados")

        elif op == "0":
            break
        else:
            print("  Opción no válida")
        input("\nPresione ENTER para continuar...")

def main():
    while True:
        borrar_pantalla()
        op = menu("menu principal", ["1) pila" , "2) colas","0) salir "])
        if op == "1":
            menu_pila()
        elif op == "2":
            menu_cola()
        elif op == "0":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()