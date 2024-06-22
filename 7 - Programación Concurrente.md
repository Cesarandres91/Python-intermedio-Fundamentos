## 7. 🧵 Programación Concurrente

En un videojuego, a veces necesitamos hacer varias cosas al mismo tiempo, como mover varios personajes o cargar datos mientras el juego sigue funcionando. Vamos a aprender sobre hilos (threads), procesos, la librería `asyncio` y el uso de locks y semáforos.

### 7.1 🧶 Hilos (Threads)

Los hilos permiten que varias partes de tu programa se ejecuten al mismo tiempo. Es como si cada personaje en tu videojuego tuviera su propio cerebro para pensar y actuar independientemente.

**Ejemplo:**

```python
import threading

# Definir una función que representará una tarea en un hilo
def mover_personaje(nombre, pasos):
    for i in range(pasos):
        print(f"{nombre} se movió al paso {i + 1}")

# Crear hilos para mover a dos personajes
hilo_mario = threading.Thread(target=mover_personaje, args=("Mario", 5))
hilo_luigi = threading.Thread(target=mover_personaje, args=("Luigi", 5))

# Iniciar los hilos
hilo_mario.start()
hilo_luigi.start()

# Esperar a que los hilos terminen
hilo_mario.join()
hilo_luigi.join()
```

### 7.2 ⚙️ Procesos (Processes)

Los procesos son como hilos, pero cada proceso tiene su propio espacio de memoria. Es como si cada personaje tuviera su propio mundo en el que jugar.

**Ejemplo:**

```python
import multiprocessing

# Definir una función que representará una tarea en un proceso
def atacar_enemigo(nombre, veces):
    for i in range(veces):
        print(f"{nombre} atacó al enemigo {i + 1} veces")

# Crear procesos para que dos personajes ataquen enemigos
proceso_mario = multiprocessing.Process(target=atacar_enemigo, args=("Mario", 5))
proceso_luigi = multiprocessing.Process(target=atacar_enemigo, args=("Luigi", 5))

# Iniciar los procesos
proceso_mario.start()
proceso_luigi.start()

# Esperar a que los procesos terminen
proceso_mario.join()
proceso_luigi.join()
```

### 7.3 🔄 Librería asyncio

La librería `asyncio` permite escribir código concurrente usando corutinas. Es como si los personajes pudieran tomar turnos rápidamente para hacer sus tareas sin detener el juego.

**Ejemplo:**

```python
import asyncio

# Definir una corutina que representará una tarea
async def recolectar_objetos(nombre, objetos):
    for objeto in objetos:
        print(f"{nombre} recolectó {objeto}")
        await asyncio.sleep(1)  # Simular un retraso en la recolección

# Crear una función principal para ejecutar las corutinas
async def main():
    mario = recolectar_objetos("Mario", ["moneda", "estrella", "flor"])
    luigi = recolectar_objetos("Luigi", ["hongo", "moneda", "estrella"])
    
    await asyncio.gather(mario, luigi)

# Ejecutar la función principal
asyncio.run(main())
```

### 7.4 🔒 Uso de Locks y Semáforos

Los locks y semáforos son herramientas para controlar el acceso a recursos compartidos. Es como tener reglas para que los personajes no se peleen por los mismos juguetes.

**Ejemplo con Locks:**

```python
import threading

# Crear un lock
lock = threading.Lock()

# Definir una función que use el lock
def usar_recurso(nombre):
    lock.acquire()
    try:
        print(f"{nombre} está usando el recurso")
    finally:
        lock.release()

# Crear hilos para que dos personajes usen el recurso
hilo_mario = threading.Thread(target=usar_recurso, args=("Mario",))
hilo_luigi = threading.Thread(target=usar_recurso, args=("Luigi",))

# Iniciar los hilos
hilo_mario.start()
hilo_luigi.start()

# Esperar a que los hilos terminen
hilo_mario.join()
hilo_luigi.join()
```

**Ejemplo con Semáforos:**

```python
import threading

# Crear un semáforo con un contador de 2
semaforo = threading.Semaphore(2)

# Definir una función que use el semáforo
def acceder_recurso(nombre):
    semaforo.acquire()
    try:
        print(f"{nombre} está accediendo al recurso")
    finally:
        semaforo.release()

# Crear hilos para que tres personajes accedan al recurso
hilo_mario = threading.Thread(target=acceder_recurso, args=("Mario",))
hilo_luigi = threading.Thread(target=acceder_recurso, args=("Luigi",))
hilo_peach = threading.Thread(target=acceder_recurso, args=("Peach",))

# Iniciar los hilos
hilo_mario.start()
hilo_luigi.start()
hilo_peach.start()

# Esperar a que los hilos terminen
hilo_mario.join()
hilo_luigi.join()
hilo_peach.join()
```

Este desarrollo cubre cómo usar hilos, procesos, la librería `asyncio`, y locks y semáforos en el contexto de un videojuego, explicándolo de manera sencilla y con ejemplos prácticos.
