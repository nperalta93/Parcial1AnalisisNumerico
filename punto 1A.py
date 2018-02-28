from random import randint
n=int(raw_input('Introduzca el valor de n'))
matriz = []
for i in range(n):
    matriz.append([])
    for j in range(n):
        matriz[i].append(None)
for i in range(n):
    for j in range(n):
	matriz[i][j]=randint(1,10)
suma=0
for x in range (0,n):
    for y in range (x,n):
        suma=suma+matriz[x][y]
