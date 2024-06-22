# 🐍 Fundamentos de Python Nivel Intermedio

# 1. 👨‍💻 Programación Orientada a Objetos (POO)

# 1.1 📦 Clases y Objetos
class Personaje:
    def __init__(self, nombre, salud):
        self.nombre = nombre
        self.salud = salud

mario = Personaje("Mario", 100)

# 1.2 🔧 Métodos
class Personaje:
    def __init__(self, nombre, salud):
        self.nombre = nombre
        self.salud = salud

    def saludar(self):
        print(f"Hola, soy {self.nombre}")

mario = Personaje("Mario", 100)
mario.saludar()  # Salida: Hola, soy Mario

# 1.3 🧬 Herencia
class Heroe(Personaje):
    def __init__(self, nombre, salud, poder):
        super().__init__(nombre, salud)
        self.poder = poder

luigi = Heroe("Luigi", 100, "Salto Alto")

# 1.4 🌀 Polimorfismo
class Villano(Personaje):
    def saludar(self):
        print(f"Soy el malvado {self.nombre}")

bowser = Villano("Bowser", 150)
bowser.saludar()  # Salida: Soy el malvado Bowser

# 1.5 🔒 Encapsulamiento
class Personaje:
    def __init__(self, nombre, salud):
        self._nombre = nombre  # atributo protegido
        self._salud = salud

    def obtener_salud(self):
        return self._salud

mario = Personaje("Mario", 100)
print(mario.obtener_salud())  # Salida: 100

# 1.6 📌 Métodos y Atributos de Clase
class Personaje:
    numero_de_personajes = 0

    def __init__(self, nombre, salud):
        self.nombre = nombre
        self.salud = salud
        Personaje.numero_de_personajes += 1

mario = Personaje("Mario", 100)
luigi = Personaje("Luigi", 100)
print(Personaje.numero_de_personajes)  # Salida: 2

# 2. 🚨 Manejo de Excepciones Avanzado

# 2.1 🛠️ Crear Excepciones Personalizadas
class VidaInsuficienteError(Exception):
    pass

def atacar(enemigo, daño):
    if enemigo.salud < daño:
        raise VidaInsuficienteError(f"Salud insuficiente para recibir {daño} de daño")
    enemigo.salud -= daño

# 2.2 ⚖️ Manejo de Excepciones Múltiples
try:
    atacar(bowser, 200)
except VidaInsuficienteError as e:
    print(e)  # Salida: Salud insuficiente para recibir 200 de daño
except Exception as e:
    print("Ocurrió un error")

# 2.3 ➕ Clausulas else y finally
try:
    atacar(bowser, 50)
except VidaInsuficienteError:
    print("Salud insuficiente")
else:
    print("Ataque exitoso")
finally:
    print("Fin del turno")

# 3. 🧩 Funciones y Decoradores

# 3.1 🏗️ Funciones Anidadas
def crear_personaje(nombre):
    def mostrar_saludo():
        print(f"¡Hola, soy {nombre}!")
    mostrar_saludo()

crear_personaje("Mario")

# 3.2 🌐 Closures
def potenciador(factor):
    def potenciar(nivel):
        return nivel * factor
    return potenciar

super_potenciador = potenciador(10)
print(super_potenciador(5))  # Salida: 50

# 3.3 🎨 Decoradores
def añadir_poder(func):
    def envoltura():
        print("¡Poder aumentado!")
        func()
        print("¡Poder máximo alcanzado!")
    return envoltura

@añadir_poder
def lanzar_fuego():
    print("Lanzando bola de fuego...")

lanzar_fuego()

# 3.4 ⚡ Funciones Lambda
sumar_puntos = lambda puntos, bonus: puntos + bonus
print(sumar_puntos(100, 50))  # Salida: 150

# 3.5 🌟 Argumentos Variables (*args y **kwargs)
def mostrar_puntuaciones(*args):
    for puntuacion in args:
        print(f"Puntuación: {puntuacion}")

mostrar_puntuaciones(100, 200, 300)

def mostrar_detalles_personaje(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_detalles_personaje(nombre="Mario", salud=100, poder="Fuego")

# 4. 📚 Manipulación de Colecciones

# 4.1 🔄 Comprensión de Listas
niveles = [nivel for nivel in range(1, 11)]
print(niveles)

# 4.2 📖 Comprensión de Diccionarios
jugadores = ["Mario", "Luigi", "Peach"]
puntuaciones = {jugador: 0 for jugador in jugadores}
print(puntuaciones)

# 4.3 🧮 Comprensión de Conjuntos
poderes = {poder for poder in ["fuego", "hielo", "fuego", "viento"]}
print(poderes)

# 4.4 🧬 Operaciones Avanzadas con Listas y Diccionarios
niveles_pares = [nivel for nivel in range(1, 11) if nivel % 2 == 0]
print(niveles_pares)

heroes = ["Mario", "Luigi"]
villanos = ["Bowser", "Wario"]
todos = heroes + villanos
print(todos)

puntuaciones_actualizadas = {jugador: puntuaciones[jugador] + 10 for jugador in puntuaciones}
print(puntuaciones_actualizadas)

objetos1 = {"pocion": 5, "espada": 1}
objetos2 = {"escudo": 1, "pocion": 3}
objetos_combinados = {**objetos1, **objetos2}
print(objetos_combinados)

# 5. 📦 Módulos y Paquetes

# 5.1 📥 Importación de Módulos
import math
print(math.sqrt(16))  # Salida: 4.0

# 5.2 🛠️ Creación de Módulos
# En un archivo llamado personajes.py:
def saludar_personaje(nombre):
    print(f"¡Hola, {nombre}! Bienvenido al juego.")

# En otro archivo:
import personajes
personajes.saludar_personaje("Mario")

# 5.3 📚 Uso de Paquetes
# Estructura del paquete:
# mi_juego/
#   __init__.py
#   personajes.py
#   enemigos.py

# En __init__.py:
from .personajes import saludar_personaje

# 5.4 🔗 Importaciones Relativas y Absolutas
# Importación absoluta:
import mi_juego.personajes

# Importación relativa:
from .personajes import saludar_personaje

# 6. 🗄️ Manejo de Archivos Avanzado

# 6.1 📊 Lectura y Escritura de Archivos CSV
import csv
with open('puntuaciones.csv', 'w', newline='') as archivo_csv:
    escritor = csv.writer(archivo_csv)
    escritor.writerows([["Jugador", "Puntuación"], ["Mario", 1000]])

with open('puntuaciones.csv', 'r') as archivo_csv:
    lector = csv.reader(archivo_csv)
    for fila in lector:
        print(fila)

# 6.2 📝 Lectura y Escritura de Archivos JSON
import json
configuracion = {"resolucion": "1920x1080", "volumen": 75, "controles": ["teclado", "ratón"]}
with open('configuracion.json', 'w') as archivo_json:
    json.dump(configuracion, archivo_json)

with open('configuracion.json', 'r') as archivo_json:
    configuracion = json.load(archivo_json)
    print(configuracion)

# 6.3 🥒 Uso del Módulo pickle
import pickle
personaje = {"nombre": "Mario", "puntos": 1000}
with open('personaje.pkl', 'wb') as archivo_pickle:
    pickle.dump(personaje, archivo_pickle)

with open('personaje.pkl', 'rb') as archivo_pickle:
    personaje = pickle.load(archivo_pickle)
    print(personaje)

# 6.4 🧩 Manejo de Archivos Binarios
datos = bytes([120, 3, 255, 0, 100])
with open('datos.bin', 'wb') as archivo_binario:
    archivo_binario.write(datos)

with open('datos.bin', 'rb') as archivo_binario:
    datos = archivo_binario.read()
    print(datos)

# 7. 🧵 Programación Concurrente

# 7.1 🧶 Hilos (Threads)
import threading
def mover_personaje(nombre, pasos):
    for i in range(pasos):
        print(f"{nombre} se movió al paso {i + 1}")

hilo_mario = threading.Thread(target=mover_personaje, args=("Mario", 5))
hilo_luigi = threading.Thread(target=mover_personaje, args=("Luigi", 5))

hilo_mario.start()
hilo_luigi.start()
hilo_mario.join()
hilo_luigi.join()

# 7.2 ⚙️ Procesos (Processes)
import multiprocessing
def atacar_enemigo(nombre, veces):
    for i in range(veces):
        print(f"{nombre} atacó al enemigo {i + 1} veces")

proceso_mario = multiprocessing.Process(target=atacar_enemigo, args=("Mario", 5))
proceso_luigi = multiprocessing.Process(target=atacar_enemigo, args=("Luigi", 5))

proceso_mario.start()
proceso_luigi.start()
proceso_mario.join()
proceso_luigi.join()

# 7.3 🔄 Librería asyncio
import asyncio
async def recolectar_objetos(nombre, objetos):
    for objeto in objetos:
        print(f"{nombre} recolectó {objeto}")
        await asyncio.sleep(1)

async def main():
    mario = recolectar_objetos("Mario", ["moneda", "estrella", "flor"])
    luigi = recolectar_objetos("Luigi", ["hongo", "moneda", "estrella"])
    await asyncio.gather(mario, luigi)

asyncio.run(main())

# 7.4 🔒 Uso de Locks y Semáforos
lock = threading.Lock()
def usar_recurso(nombre):
    lock.acquire()
    try:
        print(f"{nombre} está usando el recurso")
    finally:
        lock.release()

hilo_mario = threading.Thread(target=usar_recurso, args=("Mario",))
hilo_luigi = threading.Thread(target=usar_recurso, args=("Luigi",))
hilo_mario.start()
hilo_luigi.start()
hilo_mario.join()
hilo_luigi.join()

semaforo = threading.Semaphore(2)
def acceder_recurso(nombre):
    semaforo.acquire()
    try:
        print(f"{nombre} está accediendo al recurso")
    finally:
        semaforo.release()

hilo_mario = threading.Thread(target=acceder_recurso, args=("Mario",))
hilo_luigi = threading.Thread(target=acceder_recurso, args=("Luigi",))
hilo_peach = threading.Thread(target=acceder_recurso, args=("Peach",))

hilo_mario.start()
hilo_luigi.start()
hilo_peach.start()
hilo_mario.join()
hilo_luigi.join()
hilo_peach.join()

# 8. 🔍 Expresiones Regulares

# 8.1 📘 Introducción a Expresiones Regulares
import re
patron = r'^a'
palabras = ["apple", "banana", "avocado", "cherry", "apricot"]
palabras_con_a = [palabra for palabra in palabras if re.match(patron, palabra)]
print(palabras_con_a)

# 8.2 🔧 Uso del Módulo re
texto = "Contacta con nosotros en support@example.com o sales@example.org"
patron = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
correos = re.findall(patron, texto)
print(correos)

# 8.3 🧩 Patrones Comunes
texto = "I am reading, writing, and enjoying coding."
patron = r'\b\w+ing\b'
palabras_ing = re.findall(patron, texto)
print(palabras_ing)

# 8.4 ✂️ Reemplazo y División de Cadenas
texto = "Mi número de teléfono es 123-456-7890"
patron = r'\d'
texto_modificado = re.sub(patron, '#', texto)
print(texto_modificado)

texto = "Dividimos este texto en palabras usando espacios."
patron = r'\s+'
palabras = re.split(patron, texto)
print(palabras)

# 9. 📑 Documentación y Pruebas

# 9.1 📜 Documentación con Docstrings
def sumar(a, b):
    """
    Suma dos números y devuelve el resultado.
    """
    return a + b

# 9.2 ✅ Pruebas Unitarias con unittest
import unittest
def restar(a, b):
    return a - b

class TestFuncionesMatematicas(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(sumar(3, 4), 7)
        self.assertEqual(sumar(-1, 1), 0)

    def test_restar(self):
        self.assertEqual(restar(10, 5), 5)
        self.assertEqual(restar(-1, -1), 0)

if __name__ == '__main__':
    unittest.main()

# 9.3 🧪 Uso de pytest
# Archivo: test_funciones.py
def test_sumar():
    assert sumar(3, 4) == 7
    assert sumar(-1, 1) == 0

def test_restar():
    assert restar(10, 5) == 5
    assert restar(-1, -1) == 0

# 9.4 📈 Cobertura de Pruebas
# Ejecutar en la terminal:
# coverage run -m pytest
# coverage report

# 10. 🗄️ Bases de Datos

# 10.1 🗃️ Conexión a Bases de Datos SQL
import sqlite3
conexion = sqlite3.connect('mi_base_de_datos.db')
cursor = conexion.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS jugadores (
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    puntuacion INTEGER
)
''')
conexion.commit()
conexion.close()

# 10.2 🖋️ CRUD con SQL
conexion = sqlite3.connect('mi_base_de_datos.db')
cursor = conexion.cursor()
cursor.execute("INSERT INTO jugadores (nombre, puntuacion) VALUES (?, ?)", ("Mario", 1000))
cursor.execute("SELECT * FROM jugadores")
jugadores = cursor.fetchall()
print(jugadores)
cursor.execute("UPDATE jugadores SET puntuacion = ? WHERE nombre = ?", (1500, "Mario"))
cursor.execute("DELETE FROM jugadores WHERE nombre = ?", ("Mario",))
conexion.commit()
conexion.close()

# 10.3 🔄 ORM con SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///mi_base_de_datos.db')
Base = declarative_base()

class Jugador(Base):
    __tablename__ = 'jugadores'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    puntuacion = Column(Integer)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
nuevo_jugador = Jugador(nombre="Luigi", puntuacion=800)
session.add(nuevo_jugador)
session.commit()
jugadores = session.query(Jugador).all()
for jugador in jugadores:
    print(jugador.nombre, jugador.puntuacion)

# 10.4 📂 Conexión a Bases de Datos NoSQL
from pymongo import MongoClient
cliente = MongoClient('localhost', 27017)
base_de_datos = cliente['mi_base_de_datos']
coleccion = base_de_datos['jugadores']
nuevo_jugador = {"nombre": "Peach", "puntuacion": 900}
coleccion.insert_one(nuevo_jugador)
jugadores = coleccion.find()
for jugador in jugadores:
    print(jugador)
coleccion.update_one({"nombre": "Peach"}, {"$set": {"puntuacion": 950}})
coleccion.delete_one({"nombre": "Peach"})
