class persona():
    def __init__(self,nombre,edad):
        self.nombre = nombre 
        self.edad = edad 
    def __str__(self):
        return "nombre {}, {} edad".format( self.nombre, self.edad )

class estudiante(persona):
    def __init__(self, nombre,edad,carrera,curso):
        persona.__init__(self,nombre,edad)
        self.carrera = carrera
        self.curso = curso
    def __str__(self):
        return "nombre {}, {} edad, {} carrera, {} curso".format( self.nombre, self.edad,self.carrera,self.curso)


class delegado(persona):
    def __init__(self,carrera,curso,asignatura):
        estudiante.__init__(self,carrera,curso)
        self.asignatura = asignatura
    def __str__(self):
        return "{} carrera, {} curso, {} asignatura".format( self.nombre, self.edad,self.asignatura)


class empleado():
    def __init__(self,nombre,edad,dni,salario):
        persona.__init__(self,nombre,edad)
        self.salario = salario
        self.dni = dni
    def __str__(self):
        return "{} nombre, {} edad, {} dni, {} salario".format(self.nombre,self.edad,self.dni,self.salario)

 
class profesor():
    def __init__(self,dni,salario,asignatura,oficina):
        empleado.__init__(self,dni,salario)
        self.oficina = oficina
        self.asignatura = asignatura
    def __str__(self):
        return "{} dni, {} salario, {} asignatura, {} oficina".format(self.dni,self.salario,self.asignatura,self.oficina)


persona1 = persona("Hugo","18")
persona2 = estudiante("Alicia", "20","Biología","tercero")
persona3 = delegado("derecho","cuarto","laboralista")
persona4 = empleado("Neo","45","503417R","2300")
persona5 = profesor("265437L","1700","mates","CEU")
personas =[persona1, persona2, persona3]
def contador():
    for i in persona:
        print((i.nombre)))
    print(contador(personas))