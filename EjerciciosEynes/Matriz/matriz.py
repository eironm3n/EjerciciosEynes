import random

def crear_matriz(n):
    matriz = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(random.randint(0, 9))
        matriz.append(row)
    return matriz

def encuentra_consecutivo(matriz):
    n = len(matriz)
    for i in range(n):
        for j in range(n-3):
            if matriz[i][j] == matriz[i][j+1] == matriz[i][j+2] == matriz[i][j+3]:
                print(f"Secuencia horizontal encontrada en ({i}, {j})-({i}, {j+3})")
            if matriz[j][i] == matriz[j+1][i] == matriz[j+2][i] == matriz[j+3][i]:
                print(f"Secuencia vertical encontrada en ({j}, {i})-({j+3}, {i})")

matriz = crear_matriz(5)
print("Matriz: ")

for row in matriz:
    print(row)
encuentra_consecutivo(matriz)
