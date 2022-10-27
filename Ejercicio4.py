class Alumno():

    def __init__(self,nombre,nota,altura,peso):
        self.nombre = nombre
        self.nota = nota
        self.altura = altura
        self.peso = peso
        print(self.nombre,", el alumno, ha sido creado con éxito")

    def __str__(self):
        return '''\
    nombre\t{}
    nota\t{}
    altura\t{}
    peso\t{}'''.format(self.nombre,self.nota,self.altura,self.peso)

    def calificacion(self):
        if self.nota>=5:
            print(self.nombre,"Aprobado")
        else:
            print(self.nombre,"Suspenso")
        
Albaro = Alumno("Albaro",6,1.75,78)
Albaro.calificacion()
print(Albaro)
Pablo = Alumno("Pablo",2,1.89,97)
Pablo.calificacion()
print(Pablo)
Pepe = Alumno("Pepe",8,1.54,67)
Pepe.calificacion()
print(Pepe)
Maria = Alumno("Maria",10,1.51,43)
Maria.calificacion()
print(Maria)
Nicolas = Alumno("Nicolas",1,1.99,102)
Nicolas.calificacion()
print(Nicolas)