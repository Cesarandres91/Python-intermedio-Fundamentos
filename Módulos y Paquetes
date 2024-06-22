## 5. 📦 Módulos y Paquetes

En un videojuego, podemos tener diferentes partes del código separadas en módulos y paquetes para mantener todo organizado. Esto es como tener diferentes cajas y estanterías para tus juguetes y juegos.

### 5.1 📥 Importación de Módulos

Un módulo es un archivo que contiene código de Python. Podemos importar funciones y variables de un módulo para usarlas en otro archivo.

**Ejemplo:**

Imagina que tienes un archivo llamado `personajes.py` con la siguiente función:

```python
# Archivo: personajes.py
def saludar_personaje(nombre):
    print(f"¡Hola, {nombre}! Bienvenido al juego.")
```

Puedes importar esta función y usarla en otro archivo:

```python
# Archivo: juego.py
import personajes

# Usar la función importada
personajes.saludar_personaje("Mario")
# Salida: ¡Hola, Mario! Bienvenido al juego.
```

### 5.2 🛠️ Creación de Módulos

Crear un módulo es simplemente escribir funciones y variables en un archivo `.py`. Es como crear una nueva caja para tus juguetes.

**Ejemplo:**

Crea un archivo llamado `enemigos.py` con el siguiente contenido:

```python
# Archivo: enemigos.py
def atacar_enemigo(enemigo, daño):
    print(f"Atacaste a {enemigo} e infligiste {daño} puntos de daño.")
```

Ahora puedes usar este módulo en otro archivo:

```python
# Archivo: juego.py
import enemigos

# Usar la función del módulo enemigos
enemigos.atacar_enemigo("Goomba", 10)
# Salida: Atacaste a Goomba e infligiste 10 puntos de daño.
```

### 5.3 📚 Uso de Paquetes

Un paquete es una colección de módulos organizados en directorios. Es como tener una estantería con varias cajas de juguetes.

**Ejemplo:**

Imagina que tienes la siguiente estructura de archivos:

```
mi_juego/
    __init__.py
    personajes.py
    enemigos.py
```

El archivo `__init__.py` puede estar vacío, pero indica que `mi_juego` es un paquete. Ahora puedes importar módulos de este paquete:

```python
# Archivo: juego.py
from mi_juego import personajes, enemigos

# Usar funciones de los módulos importados
personajes.saludar_personaje("Luigi")
enemigos.atacar_enemigo("Bowser", 20)
# Salida:
# ¡Hola, Luigi! Bienvenido al juego.
# Atacaste a Bowser e infligiste 20 puntos de daño.
```

### 5.4 🔗 Importaciones Relativas y Absolutas

Las importaciones pueden ser absolutas (usando la ruta completa) o relativas (usando la ruta relativa al archivo actual).

**Importación Absoluta:**

```python
# Importación absoluta
import mi_juego.personajes

mi_juego.personajes.saludar_personaje("Peach")
# Salida: ¡Hola, Peach! Bienvenido al juego.
```

**Importación Relativa:**

```python
# Archivo: mi_juego/juego.py

# Importación relativa
from . import personajes

personajes.saludar_personaje("Toad")
# Salida: ¡Hola, Toad! Bienvenido al juego.
```

Este desarrollo cubre cómo importar módulos, crear módulos, usar paquetes y hacer importaciones relativas y absolutas en el contexto de un videojuego, explicándolo de manera sencilla y con ejemplos prácticos.
