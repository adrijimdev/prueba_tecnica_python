# Tienes un arreglo (llamado myArray) con 10 elementos (enteros en el rango de 1 a 9). 
# Escribe un programa en Python que imprima el número que tiene más ocurrencias seguidas 
# en el arreglo y también imprimir la cantidad de veces que aparece en la secuencia.
# Su programa debe analizar el arreglo de izquierda a derecha para que en caso de que
# dos números cumplan la condición, el que aparece por primera vez de izquierda a derecha
# será el que se imprima. La salida de los datos para el arreglo en el ejemplo (1,2,2,5,4,6,7,8,8,8) sería la siguiente:
# Longest: 3
# Number: 8
# En el ejemplo, la secuencia más larga la tiene el número 8 con una secuencia de 
# tres ochos seguidos. Tenga en cuenta que el código que escriba debe imprimir los resultados
# exactamente como se muestra con el fin de que la pregunta sea considerada válida.

myArray = [1, 2, 2, 5, 4, 6, 7, 8, 8, 8]
longest = 0
number = 0
numbersChecked = []

for i in range(len(myArray)):
    count = 0
    if i not in numbersChecked:
        numbersChecked += [i]
        count += 1
        for j in range(i + 1, len(myArray)):
            if myArray[i] == myArray[j]:
                count += 1
    if count > longest:
        longest = count
        number = myArray[i]

print(f"Longest: {longest}")
print(f"Number: {number}")
