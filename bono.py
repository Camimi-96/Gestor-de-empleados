#calcular_bono(sueldo, porcentaje) calcula el bono y devuelve el total
#variables sueldo int y porcentaje del bono

sueldo = int(input("Ingrese sueldo: "))
porcentaje = float(input("Ingrese porcentaje de bono: "))

def calcular_bono(sueldo,porcentaje):
    
    if porcentaje < 0 or sueldo < 0:
        return "Los valores deben ser mayores que cero"

    bono = (sueldo * porcentaje)/100
    sueldo_total = sueldo + bono

    return sueldo_total 


print(calcular_bono(sueldo, porcentaje))