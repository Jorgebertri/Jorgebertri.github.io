# Actividad 5


peso = float(input("Dime tu peso en metros: "))
estatura = float(input("Dime tu estatura en metros: "))

imc = peso / estatura ** 2

if imc < 18.5:
    categoria = "Bajo peso"

elif imc < 24.9:
    categoria = "Peso normal"

elif imc < 29.9:
    categoria = "Sobrepeso"

elif imc < 34.9:
    categoria = "Obesidad tipo I (leve)"

elif imc < 39.9:
    categoria = "Obesidad tipo II (moderada)"

else:
    categoria = "Obesidad tipo III (mórbida)"


print(f"De acuerdo a tu {imc}, está en la categoría {categoria}")
