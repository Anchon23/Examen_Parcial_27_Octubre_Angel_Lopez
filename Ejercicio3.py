class Alumno():

    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
        print(self.nombre,", el alumno, ha sido creado con éxito")

    def calificacion(self):
        if self.nota>=5:
            print("aprobar")
        else:
            print("suspender")
    
Albaro = Alumno("Albaro",16)