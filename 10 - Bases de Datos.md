## 10. 🗄️ Bases de Datos

En el análisis de datos, usamos bases de datos para almacenar y gestionar grandes cantidades de información. Vamos a aprender cómo conectarse a bases de datos SQL, hacer operaciones CRUD, usar un ORM con SQLAlchemy y conectar a bases de datos NoSQL.

### 10.1 🗃️ Conexión a Bases de Datos SQL

Las bases de datos SQL (Structured Query Language) se usan para guardar datos en tablas, como una hoja de cálculo gigante. Para conectarnos a una base de datos SQL, usamos una biblioteca llamada `sqlite3`.

**Ejemplo:**

```python
import sqlite3

# Conectar a la base de datos (o crearla si no existe)
conexion = sqlite3.connect('mi_base_de_datos.db')

# Crear un cursor para ejecutar comandos SQL
cursor = conexion.cursor()

# Crear una tabla
cursor.execute('''
CREATE TABLE IF NOT EXISTS jugadores (
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    puntuacion INTEGER
)
''')

# Confirmar los cambios y cerrar la conexión
conexion.commit()
conexion.close()
```

### 10.2 🖋️ CRUD con SQL

CRUD significa Crear, Leer, Actualizar y Eliminar. Son las operaciones básicas que podemos hacer con los datos en una base de datos.

**Ejemplo:**

```python
import sqlite3

# Conectar a la base de datos
conexion = sqlite3.connect('mi_base_de_datos.db')
cursor = conexion.cursor()

# Crear un jugador (Create)
cursor.execute("INSERT INTO jugadores (nombre, puntuacion) VALUES (?, ?)", ("Mario", 1000))

# Leer jugadores (Read)
cursor.execute("SELECT * FROM jugadores")
jugadores = cursor.fetchall()
print(jugadores)  # Salida: [(1, 'Mario', 1000)]

# Actualizar la puntuación de un jugador (Update)
cursor.execute("UPDATE jugadores SET puntuacion = ? WHERE nombre = ?", (1500, "Mario"))

# Eliminar un jugador (Delete)
cursor.execute("DELETE FROM jugadores WHERE nombre = ?", ("Mario",))

# Confirmar los cambios y cerrar la conexión
conexion.commit()
conexion.close()
```

### 10.3 🔄 ORM con SQLAlchemy

Un ORM (Object-Relational Mapping) como SQLAlchemy facilita trabajar con bases de datos convirtiendo tablas en clases de Python. Es como usar una varita mágica para convertir datos en objetos.

**Ejemplo:**

Primero, instala SQLAlchemy usando pip:

```bash
pip install sqlalchemy
```

```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Crear una conexión a la base de datos
engine = create_engine('sqlite:///mi_base_de_datos.db')
Base = declarative_base()

# Definir una clase para la tabla jugadores
class Jugador(Base):
    __tablename__ = 'jugadores'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    puntuacion = Column(Integer)

# Crear la tabla en la base de datos
Base.metadata.create_all(engine)

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()

# Crear un nuevo jugador
nuevo_jugador = Jugador(nombre="Luigi", puntuacion=800)
session.add(nuevo_jugador)
session.commit()

# Leer jugadores
jugadores = session.query(Jugador).all()
for jugador in jugadores:
    print(jugador.nombre, jugador.puntuacion)  # Salida: Luigi 800
```

### 10.4 📂 Conexión a Bases de Datos NoSQL

Las bases de datos NoSQL almacenan datos de una manera diferente a las bases de datos SQL. Son útiles para trabajar con datos no estructurados como documentos JSON. Usaremos MongoDB como ejemplo.

Primero, instala `pymongo` usando pip:

```bash
pip install pymongo
```

**Ejemplo:**

```python
from pymongo import MongoClient

# Conectar a la base de datos MongoDB
cliente = MongoClient('localhost', 27017)
base_de_datos = cliente['mi_base_de_datos']
coleccion = base_de_datos['jugadores']

# Crear un nuevo jugador (Create)
nuevo_jugador = {"nombre": "Peach", "puntuacion": 900}
coleccion.insert_one(nuevo_jugador)

# Leer jugadores (Read)
jugadores = coleccion.find()
for jugador in jugadores:
    print(jugador)  # Salida: {'_id': ObjectId(...), 'nombre': 'Peach', 'puntuacion': 900}

# Actualizar la puntuación de un jugador (Update)
coleccion.update_one({"nombre": "Peach"}, {"$set": {"puntuacion": 950}})

# Eliminar un jugador (Delete)
coleccion.delete_one({"nombre": "Peach"})
```

Este desarrollo cubre cómo conectarse a bases de datos SQL, hacer operaciones CRUD, usar un ORM con SQLAlchemy y conectar a bases de datos NoSQL en el contexto del análisis de datos, explicándolo de manera sencilla y con ejemplos prácticos.
