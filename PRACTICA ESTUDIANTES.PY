class Alumnos: 
    def_init_(self):
    self.notas=(  )
    self.nombre= ("")
    self.edad=(  )
    self.carrera=("")
def menu():
    while selección!=4:
    print("Sección A de Ingeniería ciclo básico")
    print("elegir una opción")
    print("........")
    print("1.buscar al alumno")
    print("2..mostrar los alumnos registrados")
    print("3.Salir")
    selección = int(input("elegir una opción: "))
    if selección ==1:
        buscar()
    if selección==2:
        mostrar()
    if selección ==3:
        Salir()
def buscar():
    print("esta es la función de buscar")
def mostrar():
    print("esta es la función de mostrar")
def Salir():
    print("salir")
