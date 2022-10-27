def __str__(self):
        if self.nota>=5:
            print(self.nombre,"Aprobado")
        else:
            print(self.nombre,"Suspenso")
        return '''\
    nombre\t{}
    nota\t{}'''.format(self.nombre,self.nota)