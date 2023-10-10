class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        return self.largo * self.ancho

if __name__ == '__main__':
    rectangulo = Rectangulo(5, 3)
    area = rectangulo.calcular_area()
    print("El área del rectángulo es:", area)
