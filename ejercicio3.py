# Escribir un programa en Python que puede determinar si una matriz es simétrica. 
# Una matriz es simétrica si se ve igual si está invertida. 
# Por ejemplo ('a', 'b', 'c', 'd', 'd', 'c', 'b', 'a') es simétrica 
# y ('a', 'b', 'c', 'd', 'd', 'b', 'c', 'a') no lo es. 
# Suponga que n será siempre un número par entre 2 y 10 (No hay necesidad de validar esto).
# Si es simétrico su programa debe imprimir 'Symmetric', de lo contrario imprimir 'Asymmetric'

symArray = ['a', 'b', 'c', 'd', 'd', 'c', 'b', 'a']
asymArray = ['a', 'b', 'c', 'd', 'd', 'c', 'b', 'b']

def isSymmetric(array):
    auxArray = [i for i in reversed(array)]
    if auxArray == array:
        print("Symmetric")
    else:
        print("Asymmetric")

isSymmetric(symArray)
isSymmetric(asymArray)