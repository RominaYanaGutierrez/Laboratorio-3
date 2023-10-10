def calcular_porcentaje(fraction):
    try:
        numerador, denominador = map(int, fraction.split('/'))
        if numerador <= 0 or denominador <= 0:
            raise ValueError
        if numerador > denominador:
            raise ValueError
        porcentaje = (numerador / denominador) * 100
        if porcentaje < 1:
            return 'E'
        elif porcentaje > 99:
            return 'F'
        else:
            return f'{round(porcentaje)}%'
    except ValueError:
        print('Error: La fracción debe tener formato X/Y, donde X e Y son números enteros positivos y X <= Y.')
        return None
    except ZeroDivisionError:
        print('Error: El denominador no puede ser cero.')
        return None

if __name__ == '__main__':
    while True:
        fraction = input('Ingrese una fracción en formato X/Y: ')
        porcentaje = calcular_porcentaje(fraction)
        if porcentaje is not None:
            print('Porcentaje:', porcentaje)
            break
