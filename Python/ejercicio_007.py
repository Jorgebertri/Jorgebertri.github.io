# Actividad 7


anno = int(input("Dime un año y digo si es bisiesto o no: "))
es_bisiesto = False

if (anno % 4 == 0 and anno % 100 != 0) or (anno % 400 == 0):
    es_bisiesto = True


if es_bisiesto :
    print(f"cadena El año {anno} es bisiesto")
else :
    print(f"cadena El año {anno} no es bisiesto")

