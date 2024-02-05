# ESTA ES MI RESOLUCIÓN AL RESOLVER LA PRUEBA TÉCNICA ORIGINALMENTE
# Escribir un programa en Python que recorra un arreglo y genere un histograma en base a los números de este.
# El arreglo se llama myArray y contiene 10 elementos que corresponden a números enteros del 1 al 5. 
# Un histograma representa que tanto un elemento aparece en un conjunto de datos 
# (Debe mostrar la frecuencia para todos los números del 1 al 5, incluso si no están presentes en el arreglo).
# Por ejemplo, para el arreglo: myArray:=(1,2,1,3,3,1,2,1,5,1) el histograma se vería así:
# 1: *****
# 2: **
# 3: **
# 4:
# 5: *

myArray = [1, 2, 1, 3, 3, 1, 2, 1, 5, 1]

for i in range(1, 6):
    printAsterisk = ""
    for j in myArray:
        if i == j:
            printAsterisk += "*"
    print(f"{i}: {printAsterisk}")
