# Tienes un arreglo (llamado myArray) con 5 elementos (enteros en el rango de 1 a 100). 
# Escribe un programa en Python que imprima el número más alto del arreglo (Si se repite, solo imprimir una vez).
# El programa solo debe imprimir el número, sin ningún texto.

myArray = [10, 94, 1, 5, 77]
maxNumber = 0

for i in myArray:
    if i > maxNumber:
        maxNumber = i

print(maxNumber)
