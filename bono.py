def ingresar_datos():
    print(" INGRESAR DATOS DEL EMPLEADO")
    nombre = str(input("Ingrese el nombre del empleado: "))
    edad = int(input("Ingrese la edad del empleado: "))
    cargo = str(input("Ingrese el cargo del empleado: "))
    sueldo = int(input("Ingrese el sueldo base del empleado: "))
    porcentaje_bono = float(input("Ingrese el porcentaje de bono (%): "))

    return nombre, edad, cargo, sueldo, porcentaje_bono


def calcular_bono(sueldo,porcentaje):
    
    if porcentaje < 0 or sueldo < 0:
        return "Los valores deben ser mayores que cero"

    bono = (sueldo * porcentaje)/100
    sueldo_total = sueldo + bono

    return sueldo_total 


def mostrar_resumen(nombre, edad, cargo, total):
    print("RESUMEN DEL EMPLEADO")
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad} años")
    print(f"Cargo: {cargo}")
    print(f"Sueldo total con bono: ${total:.2f}")


def mostrar_mensaje_despedida():
    print("Gracias por usar el sistema de PyCompany. ¡Hasta pronto!")



nombre = None
edad = None
cargo = None
sueldo = None
porcentaje = None
total = None
sueldo_total = None

opcion = 0

while opcion != 4:
    
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Ingresar datos del empleado")
    print("2. Calcular bono")
    print("3. Mostrar resumen")
    print("4. Salir")
    
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        nombre, edad, cargo, sueldo, porcentaje = ingresar_datos()

    elif opcion == 2:
        if sueldo is None:
            print("\n Primero debe ingresar los datos del empleado.")
        else:
            total = calcular_bono(sueldo, float(porcentaje))
            print(f"\n EL sueldo con el bono es {total}")

    elif opcion == 3:
        if total is None:
            print("\n Primero debe ingresar los datos del usuario.")
        else:
            mostrar_resumen(nombre, edad, cargo, total)

    elif opcion == 4:
        mostrar_mensaje_despedida()

    else:
        print("\n Opción inválida. Intente nuevamente.")
        



