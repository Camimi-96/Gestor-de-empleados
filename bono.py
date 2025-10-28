#calcular_bono(sueldo, porcentaje) calcula el bono y devuelve el total
#variables sueldo int y porcentaje del bono
def ingresar_datos():
        
    nombre = str(input("Ingresa tu nombre: "))
    edad = int(input("Ingresa tu edad: "))
    cargo = str(input("Ingresa tu cargo: "))
    sueldo = int(input("Ingresa tu sueldo: "))
    porcentaje = float(input("Ingresa el porcentaje de aumento: "))

    return nombre, edad, cargo, sueldo, porcentaje

nombre, edad, cargo, sueldo, porcentaje = ingresar_datos()
print(f"Un gusto {nombre}, tus datos han sido ingresados correctamente.")

sueldo = int(input("Ingrese sueldo: "))
porcentaje = float(input("Ingrese porcentaje de bono: "))

def calcular_bono(sueldo,porcentaje):
    
    if porcentaje < 0 or sueldo < 0:
        return "Los valores deben ser mayores que cero"

    bono = (sueldo * porcentaje)/100
    sueldo_total = sueldo + bono

    return sueldo_total 

def mostrar_resumen(nombre, edad, cargo, sueldo_total):
    print("RESUMEN DEL EMPLEADO")
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad} años")
    print(f"Cargo: {cargo}")
    print(f"Sueldo total con bono: {sueldo_total:.2f}")




print(calcular_bono(sueldo, porcentaje))



