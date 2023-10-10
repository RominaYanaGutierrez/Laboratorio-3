def convertir_calificaciones(cadena):
    try:
        calificaciones = cadena.split(',')
        calificaciones_enteras = [int(calificacion) for calificacion in calificaciones]
        return calificaciones_enteras
    except ValueError:
        print('Error: Los valores introducidos no son números enteros.')
        return None

if __name__ == '__main__':
    while True:
        cadena = input('Ingrese una lista de calificaciones separadas por comas: ')
        calificaciones = convertir_calificaciones(cadena)
        if calificaciones is not None:
            print('Calificaciones:', calificaciones)
            break
