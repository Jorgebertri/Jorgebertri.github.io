# Actividad 11



materias = ["Griego" , "Latin" , "Informatica"]
asignatura = input("Dime una asignatura: ")


if asignatura in materias:
    print(f"Asignatura elegida: {asignatura}")
else :
    print(f"La asignatura {asignatura} no está contemplada")