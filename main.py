import Ejercicio8

if __name__ == '__main__':
    n = 20
    min_value = 0
    max_value = 100

    numeros = random_numbers.generar_numeros_aleatorios(n, min_value, max_value)
    random_numbers.mostrar_lista(numeros)
    random_numbers.ordenar_lista(numeros)
