from peewee import *

db = SqliteDatabase('Universidad.db')
class Facultad(Model):
    nombre = CharField()
    class Meta:
        database = db

class Alumno(Model):
    nombre = CharField()
    matricula = CharField() 
    facultad = ForeignKeyField(Facultad, backref='alumnos')
    class Meta:
        database = db

#database connection
db.connect()
db.create_tables([Alumno, Facultad])

#populating the database

#facultades
facultad1 = Facultad.create(nombre='Facultad de Ciencias Fisico-Matematicas')
facultad2 = Facultad.create(nombre='Facultad de Salud Publica y Nutricion')

#alumnos
alumno1 = Alumno.create(nombre='Abigail Celada', matricula='1863549',facultad=facultad1)
alumno2 = Alumno.create(nombre='Brayan Montoya', matricula='1847284', facultad=facultad1)
alumno3 = Alumno.create(nombre='Janyan Rodriguez', matricula='1941544',facultad=facultad1)
alumno4 = Alumno.create(nombre='Pancho Pantera', matricula='2000001',facultad=facultad2)
alumno5 = Alumno.create(nombre='Alberto Almaguer', matricula='1877448',facultad=facultad1)

#select
print("**SELECT** nombre de alumnos y sus respectivas matriculas")
for alumno in Alumno.select():
    print(alumno.nombre, alumno.matricula, alumno.facultad.nombre)

print("\n**SELECT** nombre de facultades")
for facultad in Facultad.select():
    print(facultad.nombre)

#where
query_where = Alumno.select(Alumno, Facultad).join(Facultad).where(Facultad.nombre == 'Facultad de Salud Publica y Nutricion')
print("\n**WHERE** alumnos que pertenecen a Nutricion")
for alumno in query_where:
    print(alumno.nombre)

#update
print("\n**UPDATE** alumno4\n")
print(alumno4.nombre)
print("\nAhora se llama...\n")
alumno4.nombre='Melvin el Elefante'
alumno4.save()
print(alumno4.nombre)

#order by
query_orderby = Alumno.select(Alumno, Facultad).join(Facultad).where(Facultad.nombre == 'Facultad de Ciencias Fisico-Matematicas').order_by(Alumno.nombre)
print("\n**ORDER BY** alumnos que pertenecen a FCFM ordenados por orden alfabetico")
for alumno in query_orderby:
    print(alumno.nombre)

#delete
try:
    query_delete=alumno4.get(Alumno.nombre=='Melvin el Elefante')
    query_delete_instance()
    print(alumno4.nombre)
except:
    print("\n**DELETE**\nMelvin el Elefante se dio de baja")

#close connection
db.close()
