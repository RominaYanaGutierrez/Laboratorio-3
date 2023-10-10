class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.14159 * self.radio**2

if __name__ == '__main__':
    circulo = Circulo(5)
    area = circulo.calcular_area()
    print("El área del círculo es:", area)
