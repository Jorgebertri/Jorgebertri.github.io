#Actividad 12


frase = input("Dime una frase y cuent las vocales: ")

contador = 0


for letra in frase:
    if letra.lower() in "aeiou":
        contador +=1

print(f"La cantidad de vocales es:  {contador}")






