import random

def generar_numeros_aleatorios(n, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(n)]

def mostrar_lista(lista):
    print("Lista de números:")
    for numero in lista:
        print(numero, end=" ")
    print()

def ordenar_lista(lista):
    lista.sort()
    print("Lista ordenada:")
    for numero in lista:
        print(numero, end=" ")
    print()
