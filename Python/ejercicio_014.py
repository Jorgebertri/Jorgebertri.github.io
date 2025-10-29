# Actividad 14
segundos_totales = int(input("Dime una cantidad en segundos: "))

horas = segundos_totales // 3600
resto = segundos_totales % 3600
minutos = resto // 60
segundos = resto % 60

print(f"{segundos_totales} segundos son {horas} horas, {minutos} minutos y {segundos} segundos")
