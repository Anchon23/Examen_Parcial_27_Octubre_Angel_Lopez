class Alumno():

    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
        print(self.nombre,", el alumno, ha sido creado con éxito")

    def __str__(self):
        return '''\
    nombre\t{}
    nota\t{}'''.format(self.nombre,self.nota)

    def calificacion(self):
        if self.nota>=5:
            print(self.nombre,"Aprobado")
        else:
            print(self.nombre,"Suspenso")
        
Albaro = Alumno("Albaro",6)
Albaro.calificacion()
print(Albaro)
Pablo = Alumno("Pablo",2)
Pablo.calificacion()
print(Pablo)
Pepe = Alumno("Pepe",8)
Pepe.calificacion()
print(Pepe)
Maria = Alumno("Maria",10)
Maria.calificacion()
print(Maria)
Nicolas = Alumno("Nicolas",1)
Nicolas.calificacion()
print(Nicolas)