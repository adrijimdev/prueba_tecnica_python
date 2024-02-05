# Escribir un prograrna en Python que imprirna una X construida a
# base de Ia letra X y utilizar el carácter de subrayado
# El tamaño de la x se basa en una variable n que
# indicará el tarnañ0 de la letra para imprimir (en una matriz de n
# x n). Por ejemplo, para n = 5 se obtiene:
# X___X
# _X_X_
# __X__
# _X_X_
# X___X

n = 5
printX = ""
for i in range(n):
    for j in range(n):
        if j == i or j == n - i - 1:
            printX += "X"
        else:
            printX += "_"
    printX += "\n"
print(printX)
