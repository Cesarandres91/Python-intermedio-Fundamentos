## 3. 🧩 Funciones y Decoradores

Las funciones en programación son como las habilidades especiales que los personajes de un videojuego pueden usar. Vamos a aprender sobre funciones anidadas, closures, decoradores, funciones lambda y argumentos variables.

### 3.1 🏗️ Funciones Anidadas

Las funciones anidadas son funciones dentro de otras funciones. Es como tener una habilidad especial dentro de otra habilidad.

**Ejemplo:**

```python
# Definir una función principal
def crear_personaje(nombre):
    def mostrar_saludo():
        print(f"¡Hola, soy {nombre}!")
    
    # Llamar a la función anidada
    mostrar_saludo()

# Crear un personaje
crear_personaje("Mario")
# Salida: ¡Hola, soy Mario!
```

### 3.2 🌐 Closures

Un closure es una función anidada que recuerda los valores de las variables aunque la función externa haya terminado. Es como un poder especial que un personaje siempre puede usar.

**Ejemplo:**

```python
# Definir una función que genera un closure
def potenciador(factor):
    def potenciar(nivel):
        return nivel * factor
    return potenciar

# Crear un closure
super_potenciador = potenciador(10)

# Usar el closure
print(super_potenciador(5))  # Salida: 50
```

### 3.3 🎨 Decoradores

Los decoradores son funciones que modifican otras funciones. Es como darle un traje especial a un personaje que le da habilidades extra.

**Ejemplo:**

```python
# Definir un decorador
def añadir_poder(func):
    def envoltura():
        print("¡Poder aumentado!")
        func()
        print("¡Poder máximo alcanzado!")
    return envoltura

# Usar el decorador
@añadir_poder
def lanzar_fuego():
    print("Lanzando bola de fuego...")

# Llamar a la función decorada
lanzar_fuego()
# Salida:
# ¡Poder aumentado!
# Lanzando bola de fuego...
# ¡Poder máximo alcanzado!
```

### 3.4 ⚡ Funciones Lambda

Las funciones lambda son pequeñas funciones anónimas que se usan para tareas simples. Es como tener una habilidad rápida que se puede usar en el momento.

**Ejemplo:**

```python
# Definir una función lambda para sumar puntos
sumar_puntos = lambda puntos, bonus: puntos + bonus

# Usar la función lambda
print(sumar_puntos(100, 50))  # Salida: 150
```

### 3.5 🌟 Argumentos Variables (*args y **kwargs)

A veces, una función necesita aceptar una cantidad variable de argumentos. Es como una habilidad que puede afectar a muchos personajes a la vez.

**Ejemplo:**

```python
# Definir una función que usa *args
def mostrar_puntuaciones(*args):
    for puntuacion in args:
        print(f"Puntuación: {puntuacion}")

# Llamar a la función con múltiples argumentos
mostrar_puntuaciones(100, 200, 300)
# Salida:
# Puntuación: 100
# Puntuación: 200
# Puntuación: 300

# Definir una función que usa **kwargs
def mostrar_detalles_personaje(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

# Llamar a la función con argumentos nombrados
mostrar_detalles_personaje(nombre="Mario", salud=100, poder="Fuego")
# Salida:
# nombre: Mario
# salud: 100
# poder: Fuego
```

Este desarrollo cubre cómo usar funciones anidadas, closures, decoradores, funciones lambda y argumentos variables en el contexto de un videojuego, explicándolo de manera sencilla y con ejemplos prácticos.
