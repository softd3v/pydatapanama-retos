# 🏆 {Nombre del Reto}

📌 **Descripción:**
{Explica el reto de manera clara y concisa. ¿Cuál es el problema a resolver? ¿Por qué es relevante?}

📊 **Objetivo:**
{Describe qué se espera lograr con este reto. Puede ser calcular métricas, hacer una visualización, aplicar machine learning, etc.}

👤 **Autor del reto:**
{Especifica el nombre de usuario de GitHub de quien creó el reto.}

---

## 📂 **Estructura del reto**
Este reto sigue la estructura estándar:
```plaintext
📂 reto-{nombre-del-reto}-{usuario}/
 ├── README.md        # Explicación del reto
 ├── 📂 data/         # Datos del reto (si aplica)
 ├── 📂 src/          # Código base del reto (si aplica)
 ├── 📂 tests/        # Pruebas unitarias (opcional)
 ├── 📂 submissions/  # Soluciones de los participantes
```
📢 **Importante:**
- **Si tu reto usa datasets**, agrégalo en la carpeta `data/`.
- **Si requiere código base**, colócalo en `src/`.
- **Las soluciones deben subirse en `submissions/` en formato `.ipynb`.**

---

## 📌 **Datos del reto** (Si aplica)
📂 **Dataset:** `{nombre-del-archivo.csv}`
🔹 **Descripción:** {Breve explicación del dataset}
🔹 **Fuente:** {Indica la fuente del dataset si aplica}
🔹 **Diccionario de datos:**
| Columna | Descripción |
|---------|------------|
| `{columna_1}` | {Explicación} |
| `{columna_2}` | {Explicación} |
| `{columna_3}` | {Explicación} |

---

## 🚀 **Cómo participar**
1️⃣ **Clona el repositorio**
```bash
git clone git@github.com:pydatapanama/pydatapanama-retos.git
cd pydatapanama-retos
```

2️⃣ **Crea un nuevo branch con tu usuario**
```bash
git checkout -b reto-{nombre-del-reto}-{tu_usuario}
```

3️⃣ **Dirígete a la carpeta del reto y crea tu solución**
```bash
cd retos/reto-{nombre-del-reto}-{usuario}/submissions
```
```bash
touch {tu_usuario}.ipynb
```

4️⃣ **Desarrolla tu solución y súbela a GitHub**
```bash
git add .
git commit -m "🚀 Agregando solución al reto {nombre-del-reto}"
git push origin reto-{nombre-del-reto}-{tu_usuario}
```

5️⃣ **Crea un Pull Request en GitHub**
Para que tu solución sea revisada e integrada al repositorio.

---

## 🔹 **Criterios de evaluación**
Para evaluar las soluciones, se considerarán los siguientes aspectos:
✅ **Claridad y organización del código**
✅ **Uso adecuado de librerías de Python**
✅ **Calidad de la visualización (si aplica)**
✅ **Correctitud de los cálculos y análisis**

---

## 📚 **Recursos recomendados**
📌 [Documentación de Pandas](https://pandas.pydata.org/docs/)  
📌 [Documentación de Matplotlib](https://matplotlib.org/stable/contents.html)  
📌 [Documentación de Seaborn](https://seaborn.pydata.org/)  

---

🚀 **¡Esperamos tu participación!** Si tienes dudas, pregunta en nuestra comunidad o abre un Issue en GitHub. 😃