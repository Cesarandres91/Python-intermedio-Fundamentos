## 6. 🗄️ Manejo de Archivos Avanzado

En los videojuegos, a veces necesitamos guardar datos en archivos para poder usarlos más tarde. Vamos a aprender cómo leer y escribir archivos CSV y JSON, usar el módulo `pickle` y manejar archivos binarios.

### 6.1 📊 Lectura y Escritura de Archivos CSV

Los archivos CSV (Comma-Separated Values) son como hojas de cálculo donde los datos están separados por comas. Podemos usar estos archivos para guardar y cargar puntuaciones y estadísticas del juego.

**Ejemplo:**

Crear un archivo CSV con las puntuaciones de los jugadores:

```python
import csv

# Datos de puntuaciones
puntuaciones = [
    ["Jugador", "Puntuación"],
    ["Mario", 1000],
    ["Luigi", 800],
    ["Peach", 950]
]

# Escribir datos en un archivo CSV
with open('puntuaciones.csv', 'w', newline='') as archivo_csv:
    escritor = csv.writer(archivo_csv)
    escritor.writerows(puntuaciones)
```

Leer un archivo CSV con las puntuaciones de los jugadores:

```python
import csv

# Leer datos de un archivo CSV
with open('puntuaciones.csv', 'r') as archivo_csv:
    lector = csv.reader(archivo_csv)
    for fila in lector:
        print(fila)
# Salida:
# ['Jugador', 'Puntuación']
# ['Mario', '1000']
# ['Luigi', '800']
# ['Peach', '950']
```

### 6.2 📝 Lectura y Escritura de Archivos JSON

Los archivos JSON (JavaScript Object Notation) se usan para guardar datos estructurados de una manera fácil de leer. Podemos usar JSON para guardar configuraciones y estados del juego.

**Ejemplo:**

Crear un archivo JSON con las configuraciones del juego:

```python
import json

# Datos de configuración del juego
configuracion = {
    "resolucion": "1920x1080",
    "volumen": 75,
    "controles": ["teclado", "ratón"]
}

# Escribir datos en un archivo JSON
with open('configuracion.json', 'w') as archivo_json:
    json.dump(configuracion, archivo_json)
```

Leer un archivo JSON con las configuraciones del juego:

```python
import json

# Leer datos de un archivo JSON
with open('configuracion.json', 'r') as archivo_json:
    configuracion = json.load(archivo_json)
    print(configuracion)
# Salida: {'resolucion': '1920x1080', 'volumen': 75, 'controles': ['teclado', 'ratón']}
```

### 6.3 🥒 Uso del Módulo pickle

El módulo `pickle` se usa para guardar objetos de Python en un archivo y cargarlos más tarde. Es como congelar y descongelar tus juguetes para que estén listos para jugar en cualquier momento.

**Ejemplo:**

Guardar un objeto en un archivo usando `pickle`:

```python
import pickle

# Crear un objeto
personaje = {"nombre": "Mario", "puntos": 1000}

# Guardar el objeto en un archivo
with open('personaje.pkl', 'wb') as archivo_pickle:
    pickle.dump(personaje, archivo_pickle)
```

Leer un objeto de un archivo usando `pickle`:

```python
import pickle

# Leer el objeto de un archivo
with open('personaje.pkl', 'rb') as archivo_pickle:
    personaje = pickle.load(archivo_pickle)
    print(personaje)
# Salida: {'nombre': 'Mario', 'puntos': 1000}
```

### 6.4 🧩 Manejo de Archivos Binarios

A veces necesitamos trabajar con archivos binarios, que son archivos que contienen datos en formato binario (ceros y unos). Esto es útil para trabajar con imágenes y otros tipos de archivos especiales en el juego.

**Ejemplo:**

Escribir datos en un archivo binario:

```python
# Datos binarios (por ejemplo, una secuencia de bytes)
datos = bytes([120, 3, 255, 0, 100])

# Escribir datos en un archivo binario
with open('datos.bin', 'wb') as archivo_binario:
    archivo_binario.write(datos)
```

Leer datos de un archivo binario:

```python
# Leer datos de un archivo binario
with open('datos.bin', 'rb') as archivo_binario:
    datos = archivo_binario.read()
    print(datos)
# Salida: b'xx03xffx00d'
```

Este desarrollo cubre cómo leer y escribir archivos CSV y JSON, usar el módulo `pickle` y manejar archivos binarios en el contexto de un videojuego, explicándolo de manera sencilla y con ejemplos prácticos.
