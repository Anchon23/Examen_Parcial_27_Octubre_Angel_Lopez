class Alumno():

    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
        print(self.nombre,", el alumno, ha sido creado con éxito")

    def calificacion(self):
        if self.nota>=5:
            print(self.nombre,"Aprobado")
        else:
            print(self.nombre,"Suspenso")
        
Albaro = Alumno("Albaro",6)
Albaro.calificacion()
Pablo = Alumno("Pablo",2)
Pablo.calificacion()
Pepe = Alumno("Pepe",8)
Pepe.calificacion()
Maria = Alumno("Maria",10)
Maria.calificacion()
Nicolas = Alumno("Nicolas",1)
Nicolas.calificacion()