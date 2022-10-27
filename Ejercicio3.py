class Alumno():

    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
        print(self.nombre,", el alumno, ha sido creado con éxito")

    def __str__(self):
        if self.nota>=5:
            print(self.nombre,"Aprobado")
        else:
            print(self.nombre,"Suspenso")
        return '''\
    nombre\t{}
    nota\t{}'''.format(self.nombre,self.nota)
    
Albaro = Alumno("Albaro",6)
print(Albaro)
Pablo = Alumno("Pablo",2)
print(Pablo)
Pepe = Alumno("Pepe",8)
print(Pepe)
Maria = Alumno("Maria",10)
print(Maria)
Nicolas = Alumno("Nicolas",1)
print(Nicolas)