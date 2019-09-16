#!/bin/python3
import random

# Ejercicio de la ruleta

fichas_recuperadas = 0

plata_ganada = 0

fichas_ganadas = 0

fichas = 6 # Fichas iniciales

negros = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

rojos = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34 ,36]

impares = list(range(1,36,2))

pares = list(range(2,37,2))

falta = list(range(1,19,1))

pasa = list(range(19,37,1))

docena_uno = list(range(1,13,1))

docena_dos = list(range(13,25,1))

docena_tres = list(range(25,37,1))

columna_uno = list(range(1,37,3))

columna_dos = list(range(2,37,3))

columna_tres = list(range(3,37,3))

print(" La apuesta en cada momento sera de 1 ficha")

print("\n")

print(" Le apostara al rojo(1) o al negro(2)?")
apuesta_uno = int(input())

print("\n Le apostara a par(1) o impar(2)?")
apuesta_dos = int(input())

print("\n Apostara a que pasa(1) o falta(2)?")
apuesta_tres = int(input())

print("\n A que docena le apostara? 1, 2, o 3?")
apuesta_cuatro = int(input())

print("\n A que columna apostara? 1, 2, o 3?")
apuesta_cinco = int(input())

print("\n A que numero, entre el 0 al 36, apostara?")
apuesta_seis = int(input())

print("\n")

num = random.randint(0,36) # Se elige un numero al azar entre o y 36.

print("El numero que toco es" ,num, "\n") # Se printea la variale que recibio el valor aleatorio.

if num == 0 or apuesta_seis == 0:
    print("\n Esta apuesta se salteara")
elif apuesta_uno == 1 and num in rojos:
    fichas_ganadas += 1
    fichas_recuperadas += 1
    print("\n La apuesta de colores fue acertada")
elif apuesta_uno == 2 and num in negros:
    fichas_ganadas += 1
    fichas_recuperadas += 1
    print("\n La apuesta de colores fue acertada")
else:
    print("\n La apuesta del color no ha sido acertada")

if num == 0 or apuesta_seis == 0:
    print("\n Esta apuesta se salteara")
else:
    if apuesta_dos == 1 and num in pares:
        fichas_ganadas += 1
        fichas_recuperadas += 1
        print("\n La apuesta de par fue acertada")
    elif apuesta_dos == 2 and num in impares:
        fichas_ganadas += 1
        fichas_recuperadas += 1
        print("\n La apuesta de impar fue acertada")
    else:
        print("\n La apuesta de par o impar no fue acertada")

if num == 0 or apuesta_seis == 0:
    print("\n Esta apuesta se salteara")
elif apuesta_tres == 1 and num in pasa:
    fichas_ganadas += 1
    fichas_recuperadas += 1
    print("\n La apuesta de pasa fue acertada")
elif apuesta_tres == 2 and num in falta:
    fichas_ganadas += 1
    fichas_recuperadas += 1
    print("\n La apuesta de falta fue acertada")
else:
    print("\n La apuesta de falta o pasa no fue acertada")

if num == 0 or apuesta_seis == 0:
    print("\n Esta apuesta se salteara")
elif apuesta_cuatro == 1 and num in docena_uno:
    fichas_ganadas += 1
    fichas_recuperadas += 1
    print("\n La apuesta a la docena uno fue acertada")
elif apuesta_cuatro == 2 and num in docena_dos:
    fichas_ganadas += 1
    fichas_recuperadas += 1
    print("\n La apuesta a la docena dos fue acertada")
elif apuesta_cuatro == 3 and num in docena_tres:
    fichas_ganadas += 1
    fichas_recuperadas += 1
    print("\n La apuesta a la docena tres fue acertada")
else:
    print("\n La apuesta de docenas no fue acertada")

if num == 0 or apuesta_seis == 0:
    print("\n Esta apuesta se salteara")
elif apuesta_cinco == 1 and num in columna_uno:
    fichas_ganadas += 1
    fichas_recuperadas += 1
    print("\n La apuesta a la columna uno fue acertada")
elif apuesta_cinco == 2 and num in columna_dos:
    fichas_ganadas += 1
    fichas_recuperadas += 1
    print("\n La apuesta a la columna dos fue acertada")
elif apuesta_cinco == 3 and num in columna_tres:
    fichas_ganadas += 1
    fichas_recuperadas += 1
    print("\n La apuesta a la columna tres fue acertada")
else:
    print("\n La apuesta de la columna no fue acertada")

if num == apuesta_seis:
    fichas_ganadas += 1
    fichas_recuperadas += 1
    print("\n La apuesta del numero pleno fue acertada")
else:
    print("\n La apuesta del numero pleno no fue acertada")

plata_ganada = (fichas_ganadas + fichas_recuperadas) * 100 * 0.95

print("\nSe han recuperado" ,fichas_recuperadas, "fichas. Y se han ganado" ,fichas_ganadas, "fichas.")
print("\nEl valor total de sus fichas descontando el %5 del valor es de $" ,plata_ganada)
