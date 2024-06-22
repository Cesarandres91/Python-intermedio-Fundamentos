## 9. 📑 Documentación y Pruebas

En el análisis de datos, es importante documentar el código para que otros puedan entenderlo y probarlo para asegurarse de que funciona correctamente. Vamos a aprender sobre cómo usar docstrings para documentar, cómo hacer pruebas unitarias con `unittest`, cómo usar `pytest` y cómo medir la cobertura de las pruebas.

### 9.1 📜 Documentación con Docstrings

Los docstrings son cadenas de texto que se colocan al principio de una función, clase o módulo para explicar qué hace. Es como dejar notas en tu cuaderno de análisis para que otros sepan lo que hiciste.

**Ejemplo:**

```python
def sumar(a, b):
    """
    Suma dos números y devuelve el resultado.

    Parámetros:
    a (int): El primer número.
    b (int): El segundo número.

    Devuelve:
    int: La suma de a y b.
    """
    return a + b

# Usar la función
resultado = sumar(3, 4)
print(resultado)  # Salida: 7
```

### 9.2 ✅ Pruebas Unitarias con unittest

Las pruebas unitarias son pruebas automáticas que verifican si pequeñas partes de tu código (como funciones) funcionan correctamente. Es como hacer un experimento para asegurarte de que tu análisis de datos es correcto.

**Ejemplo:**

```python
import unittest

def restar(a, b):
    """Resta dos números y devuelve el resultado."""
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
```

### 9.3 🧪 Uso de pytest

`pytest` es una herramienta para hacer pruebas que es fácil de usar y muy poderosa. Es como usar una lupa mágica para verificar tu código de análisis de datos.

**Ejemplo:**

Primero, instala `pytest` usando pip:

```bash
pip install pytest
```

Crea un archivo de prueba llamado `test_funciones.py`:

```python
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def test_sumar():
    assert sumar(3, 4) == 7
    assert sumar(-1, 1) == 0

def test_restar():
    assert restar(10, 5) == 5
    assert restar(-1, -1) == 0
```

Luego, ejecuta `pytest` en la terminal:

```bash
pytest
```

### 9.4 📈 Cobertura de Pruebas

La cobertura de pruebas mide qué porcentaje de tu código está siendo probado. Es como asegurarte de que has revisado cada página de tu cuaderno de análisis de datos.

**Ejemplo:**

Primero, instala `coverage` usando pip:

```bash
pip install coverage
```

Usa `coverage` para ejecutar tus pruebas y generar un informe de cobertura:

```bash
# Ejecutar pruebas con cobertura
coverage run -m pytest

# Generar informe de cobertura
coverage report

# Opcional: Generar informe HTML
coverage html
```

Este desarrollo cubre cómo usar docstrings para documentar tu código, cómo hacer pruebas unitarias con `unittest`, cómo usar `pytest` y cómo medir la cobertura de las pruebas en el contexto del análisis de datos, explicándolo de manera sencilla y con ejemplos prácticos.
