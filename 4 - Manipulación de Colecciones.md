## 4. 📚 Manipulación de Colecciones

En los videojuegos, a menudo necesitamos manejar colecciones de datos, como listas de personajes, diccionarios de objetos y conjuntos de habilidades. Vamos a aprender sobre comprensión de listas, diccionarios y conjuntos, así como operaciones avanzadas con listas y diccionarios.

### 4.1 🔄 Comprensión de Listas

La comprensión de listas es una forma rápida de crear listas en Python. Es como tener una herramienta mágica para generar listas de personajes en tu videojuego.

**Ejemplo:**

```python
# Crear una lista de niveles usando comprensión de listas
niveles = [nivel for nivel in range(1, 11)]

# Imprimir la lista de niveles
print(niveles)  # Salida: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

### 4.2 📖 Comprensión de Diccionarios

La comprensión de diccionarios es una forma rápida de crear diccionarios. Es como tener un libro de hechizos para generar diccionarios de objetos en tu juego.

**Ejemplo:**

```python
# Crear un diccionario de puntuaciones usando comprensión de diccionarios
jugadores = ["Mario", "Luigi", "Peach"]
puntuaciones = {jugador: 0 for jugador in jugadores}

# Imprimir el diccionario de puntuaciones
print(puntuaciones)  # Salida: {'Mario': 0, 'Luigi': 0, 'Peach': 0}
```

### 4.3 🧮 Comprensión de Conjuntos

La comprensión de conjuntos es una forma rápida de crear conjuntos. Es como tener una varita mágica para generar conjuntos de habilidades únicas en tu juego.

**Ejemplo:**

```python
# Crear un conjunto de poderes usando comprensión de conjuntos
poderes = {poder for poder in ["fuego", "hielo", "fuego", "viento"]}

# Imprimir el conjunto de poderes
print(poderes)  # Salida: {'fuego', 'hielo', 'viento'}
```

### 4.4 🧬 Operaciones Avanzadas con Listas y Diccionarios

A veces necesitamos hacer cosas más complicadas con listas y diccionarios, como filtrar elementos o combinar diccionarios. Es como tener habilidades especiales para manejar tus colecciones de datos.

**Ejemplo de operaciones avanzadas con listas:**

```python
# Filtrar niveles pares usando comprensión de listas
niveles_pares = [nivel for nivel in range(1, 11) if nivel % 2 == 0]

# Imprimir la lista de niveles pares
print(niveles_pares)  # Salida: [2, 4, 6, 8, 10]

# Combinar dos listas de personajes
heroes = ["Mario", "Luigi"]
villanos = ["Bowser", "Wario"]
todos = heroes + villanos

# Imprimir la lista combinada
print(todos)  # Salida: ['Mario', 'Luigi', 'Bowser', 'Wario']
```

**Ejemplo de operaciones avanzadas con diccionarios:**

```python
# Actualizar puntuaciones usando comprensión de diccionarios
puntuaciones_actualizadas = {jugador: puntuaciones[jugador] + 10 for jugador in puntuaciones}

# Imprimir el diccionario de puntuaciones actualizadas
print(puntuaciones_actualizadas)  # Salida: {'Mario': 10, 'Luigi': 10, 'Peach': 10}

# Combinar dos diccionarios de objetos
objetos1 = {"pocion": 5, "espada": 1}
objetos2 = {"escudo": 1, "pocion": 3}
objetos_combinados = {**objetos1, **objetos2}

# Imprimir el diccionario combinado
print(objetos_combinados)  # Salida: {'pocion': 3, 'espada': 1, 'escudo': 1}
```
