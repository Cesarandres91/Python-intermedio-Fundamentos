## 2. 🚨 Manejo de Excepciones Avanzado

El manejo de excepciones es como poner un escudo en tu videojuego para que, si algo sale mal, puedas arreglarlo sin que el juego se rompa. Vamos a aprender cómo crear excepciones personalizadas, manejar varias excepciones y usar las cláusulas `else` y `finally`.

### 2.1 🛠️ Crear Excepciones Personalizadas

A veces, en tu juego, necesitas crear tus propias excepciones para situaciones especiales. Es como crear un monstruo único que solo aparece en ciertas condiciones.

**Ejemplo:**

```python
# Crear una excepción personalizada
class VidaInsuficienteError(Exception):
    pass

# Definir una función que use la excepción personalizada
def atacar(enemigo, daño):
    if enemigo.salud < daño:
        raise VidaInsuficienteError(f"La salud de {enemigo.nombre} es insuficiente para recibir {daño} puntos de daño.")
    else:
        enemigo.salud -= daño
        print(f"{enemigo.nombre} ha recibido {daño} puntos de daño.")

# Definir la clase Enemigo
class Enemigo:
    def __init__(self, nombre, salud):
        self.nombre = nombre
        self.salud = salud

# Crear un objeto Enemigo
goomba = Enemigo("Goomba", 10)

# Intentar atacar al enemigo
try:
    atacar(goomba, 20)
except VidaInsuficienteError as e:
    print(e)  # Salida: La salud de Goomba es insuficiente para recibir 20 puntos de daño.
```

### 2.2 ⚖️ Manejo de Excepciones Múltiples

En tu juego, pueden ocurrir diferentes tipos de problemas. Puedes prepararte para varios problemas al mismo tiempo, como tener diferentes tipos de pociones para diferentes efectos.

**Ejemplo:**

```python
# Definir funciones que pueden lanzar diferentes excepciones
def dividir(a, b):
    return a / b

def abrir_archivo(nombre):
    with open(nombre, 'r') as archivo:
        return archivo.read()

# Manejo de excepciones múltiples
try:
    resultado = dividir(10, 0)
    contenido = abrir_archivo("juego.txt")
except ZeroDivisionError:
    print("No puedes dividir por cero.")  # Salida: No puedes dividir por cero.
except FileNotFoundError:
    print("El archivo no fue encontrado.")  # Salida si el archivo no existe: El archivo no fue encontrado.
```

### 2.3 ➕ Cláusulas else y finally

En tu juego, a veces necesitas hacer algo si todo sale bien (`else`) o siempre hacer algo al final sin importar si hubo problemas o no (`finally`).

**Ejemplo:**

```python
# Definir una función que use else y finally
def jugar(jugador, puntos):
    try:
        jugador['puntuacion'] += puntos
    except KeyError:
        print("El jugador no tiene una puntuación.")
    else:
        print(f"{jugador['nombre']} ha ganado {puntos} puntos.")  # Se ejecuta si no hubo excepciones
    finally:
        print("Fin del turno.")  # Se ejecuta siempre

# Crear un jugador
jugador1 = {'nombre': 'Mario', 'puntuacion': 100}

# Llamar a la función
jugar(jugador1, 50)
# Salida:
# Mario ha ganado 50 puntos.
# Fin del turno.
```
