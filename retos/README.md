# 📂 Directorio de Retos - PyData Panama

Bienvenido al directorio `retos/`, donde la comunidad de **PyData Panama** puede proponer y resolver desafíos de análisis de datos en Python. 🚀

Cada reto es un ejercicio diseñado para mejorar habilidades en manipulación de datos, visualización, machine learning y más. Sigue esta guía para contribuir correctamente.

---

## 📀 ¿Cómo estructurar un nuevo reto?
Cada reto debe seguir la estructura estándar para garantizar que pueda ser entendido, resuelto y evaluado fácilmente.

### 📂 **Estructura de un reto**
Cada reto debe estar dentro de una carpeta con el siguiente formato:
```plaintext
📂 retos/
 ├── 📂 reto-{nombre-del-reto}-{usuario}/  # Carpeta con el reto
 │   ├── 🐜 README.md     # Explicación del reto y reglas
 │   ├── 📂 data/         # Datos necesarios para el reto (si aplica)
 │   ├── 📂 notebooks/    # Notebooks del reto (si aplica)
 │   ├── 📂 src/          # Código base del reto (si aplica)
 │   ├── 📂 tests/        # Pruebas unitarias para validar soluciones (si aplica)
 │   └── 📂 submissions/  # Soluciones enviadas por los participantes
```
📢 **Ejemplo real:**
```plaintext
📂 retos/reto-contar-vocales-jasonssdev/
 ├─ README.md
 ├─ data/
 ├─ notebooks/
 ├─ src/
 ├─ tests/
 └─ submissions/
```

---

## 🏆 **Reglas para crear un reto**
Para que tu reto sea aceptado y cuente en el **ranking**, debe cumplir con estas reglas:

### ✅ **Formato del nombre de la carpeta**
Cada reto debe nombrarse siguiendo esta estructura:
```plaintext
reto-{nombre-del-reto}-{usuario-github}
```
**Ejemplos válidos:**
- `retos/reto-analizar-ventas-maria123/`
- `retos/reto-predict-stock-carlosdev/`
- `retos/reto-clustering-clientes-jasonssdev/`

### ✅ **Contenido mínimo del reto**
Cada reto debe contener al menos:
1️⃣ **README.md** → Explica el problema, los datos y los criterios de evaluación.  
2️⃣ **submissions/** → Carpeta para que los participantes suban sus soluciones en formato `.ipynb`.  

Opcionalmente, puedes agregar:
- **data/** → Si el reto usa datasets, deben guardarse aquí.
- **notebooks/** → Si el reto usa notebooks, deben guardarse aquí.
- **src/** → Código base o archivos auxiliares.
- **tests/** → Pruebas automatizadas para validar soluciones.

---

## 🚀 **Cómo agregar un nuevo reto**

### 1️⃣ **Haz un Fork del repositorio**
Entra al repositorio en GitHub y presiona el botón [Fork](https://github.com/pydatapanama/pydatapanama-retos/fork) en la esquina superior derecha.

### 2️⃣ **Clona tu Fork en tu máquina local**
```bash
git clone https://github.com/tu-usuario/pydatapanama-retos.git
cd pydatapanama-retos
```

### 3️⃣ **Crea un nuevo branch con tu usuario**
```bash
git checkout -b reto-{nombre-del-reto}-{tu_usuario}
```

### 4️⃣ **Copia la plantilla de reto**
```bash
cp -r retos/reto-template-usuario retos/reto-{nombre-del-reto}-{tu_usuario}
```
📢 **Ejemplo real:**
```bash
cp -r retos/reto-template-usuario retos/reto-analizar-ventas-maria123
```

### 5️⃣ **Edita el README.md del reto**
- Explica claramente el problema.
- Indica los criterios de evaluación.
- Agrega ejemplos si es necesario.

### 6️⃣ **Sube tu reto y haz un Pull Request**
```bash
git add .
git commit -m "🚀 Agregando nuevo reto sobre {tema}"
git push origin reto-{nombre-del-reto}-{tu_usuario}
```

Luego, ve a **GitHub** y crea un **Pull Request** para que tu reto sea revisado e integrado.

---

## 🎯 **Cómo resolver un reto**

### 1️⃣ **Haz un Fork del repositorio**
Si aún no lo has hecho, haz un Fork del repositorio en GitHub: [Fork](https://github.com/pydatapanama/pydatapanama-retos/fork).

### 2️⃣ **Clona tu Fork en tu máquina local**
```bash
git clone https://github.com/tu-usuario/pydatapanama-retos.git
cd pydatapanama-retos
```

### 3️⃣ **Crea un nuevo branch con tu usuario**
```bash
git checkout -b solucion-{nombre-del-reto}-{tu_usuario}
```

### 4️⃣ **Agrega tu solución en `submissions/`**
- Asegúrate de que tu solución sea un **Jupyter Notebook (`.ipynb`)**.
- Guarda el archivo con tu usuario en el nombre.

📢 **Ejemplo:**
```bash
cd retos/reto-analizar-ventas-maria123/submissions
touch solucion-maria123.ipynb
```

### 5️⃣ **Sube tu solución y haz un Pull Request**
```bash
git add .
git commit -m "📚 Agregando solución al reto {nombre-del-reto}"
git push origin solucion-{nombre-del-reto}-{tu_usuario}
```

Luego, ve a **GitHub** y crea un **Pull Request** para que tu solución sea revisada e integrada.

---

## 🌟 **¡Gracias por contribuir!**
Si tienes dudas, pregunta en nuestra comunidad o abre un Issue en GitHub. 🚀