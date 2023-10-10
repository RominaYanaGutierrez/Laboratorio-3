class Producto:
    def __init__(self, codigo, nombre, precio, existencia):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.existencia = existencia
    def __str__(self):
        return f"Código: {self.codigo} - {self.nombre} - Precio: ${self.precio:.2f} - Existencia: {self.existencia} unidades"
class Catalogo:
    def __init__(self):
        self.productos = []
    def agregar_producto(self, producto):
        self.productos.append(producto)
    def mostrar_productos(self):
        for producto in self.productos:
            print(producto)
    def buscar_por_precio(self, precio_maximo):
        productos_encontrados = [p for p in self.productos if p.precio <= precio_maximo]
        if productos_encontrados:
            print(f"Productos con precio igual o inferior a ${precio_maximo:.2f}:")
            for producto in productos_encontrados:
                print(producto)
        else:
            print(f"No se encontraron productos con precio igual o inferior a ${precio_maximo:.2f}.")

    def buscar_por_codigo(self, codigo):
        producto_encontrado = next((p for p in self.productos if p.codigo == codigo), None)
        if producto_encontrado:
            print(f"Producto con código {codigo}:")
            print(producto_encontrado)
        else:
            print(f"No se encontró ningún producto con código {codigo}.")


if __name__ == "__main__":
    catalogo = Catalogo()

    producto1 = Producto("P001", "Aceite de motor", 25.99, 50)
    producto2 = Producto("P002", "Filtro de aire", 9.95, 100)
    producto3 = Producto("P003", "Batería de arranque", 89.95, 20)
    producto4 = Producto("P004", "Pastillas de freno", 35.75, 30)

    catalogo.agregar_producto(producto1)
    catalogo.agregar_producto(producto2)
    catalogo.agregar_producto(producto3)
    catalogo.agregar_producto(producto4)

    print("Catálogo de productos:")
    catalogo.mostrar_productos()

    precio_maximo_busqueda = 30.0
    print("\nBuscar productos con precio igual o inferior a $", precio_maximo_busqueda)
    catalogo.buscar_por_precio(precio_maximo_busqueda)

    codigo_busqueda = "P002"
    print(f"\nBuscar producto con código {codigo_busqueda}:")
    catalogo.buscar_por_codigo(codigo_busqueda)
