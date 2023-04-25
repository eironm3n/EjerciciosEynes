import random

def generar_lista():
    lista = []
    for i in range(10):
        d = {"id": i+1, "edad": random.randint(1, 100)}
        lista.append(d)
    return lista

def lista_ordenada(lista):
    lista_ordenada = sorted(lista, key=lambda x: x["edad"], reverse=True)
    print("La persona más joven tiene id: ", lista_ordenada[-1]["id"])
    print("La persona más vieja tiene id: ", lista_ordenada[0]["id"])
    return lista_ordenada

lista = generar_lista()
print(lista)
lista_ordenada = lista_ordenada(lista)
print(lista_ordenada)
