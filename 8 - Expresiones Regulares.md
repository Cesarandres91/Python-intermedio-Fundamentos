## 8. 🔍 Expresiones Regulares

Las expresiones regulares son una herramienta poderosa para buscar y manipular texto. Imagina que estás buscando patrones específicos en grandes conjuntos de datos, como buscar palabras en un libro gigante.

### 8.1 📘 Introducción a Expresiones Regulares

Una expresión regular es como una fórmula mágica que describe un patrón en el texto. Puedes usarla para encontrar, reemplazar o dividir cadenas de texto.

**Ejemplo:**

Imagina que quieres encontrar todas las palabras que empiezan con "a" en una lista de palabras.

```python
import re

# Lista de palabras
palabras = ["apple", "banana", "avocado", "cherry", "apricot"]

# Expresión regular para encontrar palabras que empiezan con 'a'
patron = r'^a'

# Filtrar palabras que coinciden con el patrón
palabras_con_a = [palabra for palabra in palabras if re.match(patron, palabra)]
print(palabras_con_a)  # Salida: ['apple', 'avocado', 'apricot']
```

### 8.2 🔧 Uso del Módulo re

El módulo `re` en Python proporciona herramientas para trabajar con expresiones regulares. Puedes usar funciones como `re.match()`, `re.search()`, `re.findall()` y `re.sub()` para trabajar con texto.

**Ejemplo:**

Buscar todas las direcciones de correo electrónico en un texto:

```python
import re

# Texto con direcciones de correo electrónico
texto = "Contacta con nosotros en support@example.com o sales@example.org"

# Expresión regular para encontrar direcciones de correo electrónico
patron = r'b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+.[A-Z|a-z]{2,}b'

# Encontrar todas las direcciones de correo electrónico en el texto
correos = re.findall(patron, texto)
print(correos)  # Salida: ['support@example.com', 'sales@example.org']
```

### 8.3 🧩 Patrones Comunes

Existen muchos patrones comunes que puedes usar en expresiones regulares. Aquí tienes algunos ejemplos útiles:

- `d` : cualquier dígito
- `w` : cualquier letra, número o guion bajo
- `s` : cualquier espacio en blanco
- `.`  : cualquier carácter excepto el salto de línea
- `^`  : el inicio de una cadena
- `$`  : el final de una cadena

**Ejemplo:**

Buscar todas las palabras que terminan en "ing" en un texto:

```python
import re

# Texto con palabras
texto = "I am reading, writing, and enjoying coding."

# Expresión regular para encontrar palabras que terminan en 'ing'
patron = r'bw+ingb'

# Encontrar todas las palabras que terminan en 'ing'
palabras_ing = re.findall(patron, texto)
print(palabras_ing)  # Salida: ['reading', 'writing', 'enjoying']
```

### 8.4 ✂️ Reemplazo y División de Cadenas

Puedes usar expresiones regulares para reemplazar partes de una cadena o dividir una cadena en partes.

**Ejemplo de reemplazo:**

Reemplazar todas las cifras en un texto con un símbolo `#`:

```python
import re

# Texto con cifras
texto = "Mi número de teléfono es 123-456-7890"

# Expresión regular para encontrar cifras
patron = r'd'

# Reemplazar todas las cifras con '#'
texto_modificado = re.sub(patron, '#', texto)
print(texto_modificado)  # Salida: "Mi número de teléfono es ###-###-####"
```

**Ejemplo de división:**

Dividir un texto en palabras usando espacios como delimitadores:

```python
import re

# Texto con palabras
texto = "Dividimos este texto en palabras usando espacios."

# Expresión regular para encontrar espacios
patron = r's+'

# Dividir el texto en palabras
palabras = re.split(patron, texto)
print(palabras)  # Salida: ['Dividimos', 'este', 'texto', 'en', 'palabras', 'usando', 'espacios.']
```
