class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"
    def distancia(self, otro_punto):
        """
        Calcula la distancia entre este punto y otro punto dado.
        """
        dx = self.x - otro_punto.x
        dy = self.y - otro_punto.y
        return (dx**2 + dy**2)**0.5


if __name__ == '__main__':
    try:
        x1 = float(input("Ingrese la coordenada X del primer punto: "))
        y1 = float(input("Ingrese la coordenada Y del primer punto: "))
        x2 = float(input("Ingrese la coordenada X del segundo punto: "))
        y2 = float(input("Ingrese la coordenada Y del segundo punto: "))
        
        punto1 = Punto(x1, y1)
        punto2 = Punto(x2, y2)

        print("Punto 1:", punto1)
        print("Punto 2:", punto2)

        distancia = punto1.distancia(punto2)
        print(f"Distancia entre Punto 1 y Punto 2: {distancia:.2f}")
    
    except ValueError as ve:
        print(f"Error: {ve}. Por favor, ingrese coordenadas válidas (números).")
