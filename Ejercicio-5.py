class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.notas = []

    def display(self):
        print("Información del estudiante:")
        print("Nombre:", self.nombre)
        print("Número de Registro:", self.numero_registro)
        if self.edad is not None:
            print("Edad:", self.edad)
        if self.notas:
            print("Notas:", ", ".join(map(str, self.notas)))
    
    def setAge(self, edad):
        self.edad = edad

    def setNota(self, notas):
        if isinstance(notas, list):
            self.notas = notas
        else:
            print("Las notas deben ser una lista.")

if __name__ == "__main__":
    nombre = input("Ingrese el nombre del alumno: ")
    numero_registro = input("Ingrese el número de registro del alumno: ")
    alumno = Alumno(nombre, numero_registro)
    alumno.setAge(int(input("Ingrese la edad del alumno: ")))
    notas = input("Ingrese las notas del alumno separadas por comas (ejemplo: 7,8,9): ").split(",")
    alumno.setNota([float(nota) for nota in notas])
    alumno.display()
