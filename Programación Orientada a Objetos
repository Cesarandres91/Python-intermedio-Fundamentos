# 👨‍💻 Programación Orientada a Objetos (POO)

La Programación Orientada a Objetos (POO) es una forma de escribir programas de computadora utilizando "objetos". Estos objetos son como personajes y cosas en un videojuego, y cada uno tiene sus propias características y habilidades.

## 1.1 📦 Clases y Objetos

Una **clase** es como un plano para construir algo. En un videojuego, podemos tener una clase llamada `Personaje`, que describe cómo son los personajes del juego. Un **objeto** es una instancia de una clase, como un personaje específico en el juego.

**Ejemplo:**

```python
# Definir la clase Personaje
class Personaje:
    def __init__(self, nombre, salud):
        self.nombre = nombre  # Nombre del personaje
        self.salud = salud    # Salud del personaje

# Crear objetos (instancias) de la clase Personaje
mario = Personaje("Mario", 100)
luigi = Personaje("Luigi", 100)

# Imprimir detalles de los personajes
print(mario.nombre)  # Salida: Mario
print(luigi.salud)   # Salida: 100
```

## 1.2 🔧 Métodos

Los **métodos** son como las habilidades o acciones que los personajes pueden realizar en el juego. Son funciones que pertenecen a una clase.

**Ejemplo:**

```python
# Definir la clase Personaje con un método
class Personaje:
    def __init__(self, nombre, salud):
        self.nombre = nombre
        self.salud = salud

    def saludar(self):
        print(f"Hola, soy {self.nombre}.")

# Crear un objeto de la clase Personaje
mario = Personaje("Mario", 100)

# Llamar al método saludar
mario.saludar()  # Salida: Hola, soy Mario.
```

## 1.3 🧬 Herencia

La **herencia** permite crear nuevas clases basadas en clases existentes. Es como tener un personaje especial que tiene todas las habilidades de un personaje normal, pero con algo extra.

**Ejemplo:**

```python
# Definir la clase Personaje
class Personaje:
    def __init__(self, nombre, salud):
        self.nombre = nombre
        self.salud = salud

    def saludar(self):
        print(f"Hola, soy {self.nombre}.")

# Definir la clase Heroe que hereda de Personaje
class Heroe(Personaje):
    def __init__(self, nombre, salud, superpoder):
        super().__init__(nombre, salud)
        self.superpoder = superpoder

    def usar_superpoder(self):
        print(f"{self.nombre} usa {self.superpoder}.")

# Crear un objeto de la clase Heroe
super_mario = Heroe("Super Mario", 120, "Salto Alto")

# Llamar a los métodos
super_mario.saludar()        # Salida: Hola, soy Super Mario.
super_mario.usar_superpoder() # Salida: Super Mario usa Salto Alto.
```

## 1.4 🌀 Polimorfismo

El **polimorfismo** permite usar un método en diferentes clases y obtener resultados diferentes. Es como tener personajes que pueden saludar de maneras distintas.

**Ejemplo:**

```python
# Definir la clase Personaje
class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print(f"Hola, soy {self.nombre}.")

# Definir la clase Villano que hereda de Personaje
class Villano(Personaje):
    def saludar(self):
        print(f"Soy el malvado {self.nombre}.")

# Crear objetos de ambas clases
mario = Personaje("Mario")
bowser = Villano("Bowser")

# Llamar al método saludar
mario.saludar()   # Salida: Hola, soy Mario.
bowser.saludar()  # Salida: Soy el malvado Bowser.
```

## 1.5 🔒 Encapsulamiento

El **encapsulamiento** es como proteger las partes internas del personaje para que no puedan ser cambiadas directamente desde fuera. Se hace usando guiones bajos `_`.

**Ejemplo:**

```python
# Definir la clase Personaje con encapsulamiento
class Personaje:
    def __init__(self, nombre, salud):
        self._nombre = nombre  # Nombre protegido
        self._salud = salud    # Salud protegida

    def obtener_salud(self):
        return self._salud

    def establecer_salud(self, nueva_salud):
        if nueva_salud >= 0:
            self._salud = nueva_salud

# Crear un objeto de la clase Personaje
mario = Personaje("Mario", 100)

# Intentar cambiar la salud directamente (no recomendado)
mario._salud = 120

# Cambiar la salud usando métodos (recomendado)
mario.establecer_salud(90)

# Obtener la salud del personaje
print(mario.obtener_salud())  # Salida: 90
```

## 1.6 📌 Métodos y Atributos de Clase

Los **métodos y atributos de clase** son compartidos por todos los objetos de una clase. Son como características y habilidades comunes a todos los personajes de un tipo.

**Ejemplo:**

```python
# Definir la clase Personaje con un atributo de clase
class Personaje:
    numero_de_personajes = 0  # Atributo de clase

    def __init__(self, nombre, salud):
        self.nombre = nombre
        self.salud = salud
        Personaje.numero_de_personajes += 1

    @classmethod
    def obtener_numero_de_personajes(cls):
        return cls.numero_de_personajes

# Crear objetos de la clase Personaje
mario = Personaje("Mario", 100)
luigi = Personaje("Luigi", 100)

# Obtener el número de personajes creados
print(Personaje.obtener_numero_de_personajes())  # Salida: 2
```

Este desarrollo cubre los conceptos de clases y objetos, métodos, herencia, polimorfismo, encapsulamiento y métodos y atributos de clase en el contexto de un videojuego, explicando de manera sencilla y con ejemplos prácticos.
