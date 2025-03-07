# 🌟 PyData Panama - Retos de Datos con Python

Bienvenido a **pydatapanama-retos**, un repositorio colaborativo de **PyData Panama** donde la comunidad puede proponer y resolver retos de datos con Python. 🚀

Este repositorio está diseñado para fomentar el aprendizaje práctico a través de **desafíos reales** y un sistema de **ranking de contribuyentes**.

---

## 🎯 **Objetivo del repositorio**
El propósito de este repositorio es:

👉 Centralizar retos de análisis de datos en Python.  
👉 Permitir que cualquier miembro de la comunidad pueda **crear y resolver retos**.  
👉 Incentivar la participación con un **ranking de puntos automático**.  
👉 Fomentar el aprendizaje a través de desafíos reales.  
👉 Servir como un espacio para compartir soluciones y enfoques diversos.  

📌 **Todos los retos siguen un mismo formato**, lo que permite que sean fáciles de seguir y evaluar.

---

## 🏆 **Sistema de Ranking - Gana puntos por participar**
Para fomentar la participación, este repositorio incluye un **ranking automático** que asigna puntos a los participantes:

| Acción | Puntos |
|--------|--------|
| **Crear un nuevo reto** | +40 puntos |
| **Resolver un reto (subir una solución)** | +30 puntos |
| **Mejorar un reto existente (modificar README, pruebas, etc.)** | +10 puntos |

📌 **El ranking se actualiza automáticamente** cuando un Pull Request (PR) es fusionado a `main`.  
📌 Puedes consultar el **ranking actual** en el archivo [`RANKING.md`](RANKING.md).

---

## 📂 **Estructura del repositorio**
Cada reto estará dentro de la carpeta `retos/`:
```plaintext
📂 pydatapanama-retos/
 ├📂 retos/                  # Carpeta donde la comunidad sube los retos
 │  ├📂 reto-template-usuario/  # Ejemplo de un reto propuesto por un usuario
 │  │  ├📄 README.md      # Explicación del reto y reglas
 │  │  ├📂 data/         # Datos necesarios para el reto (si aplica)
 │  │  ├📂 src/          # Código base del reto (si aplica)
 │  │  ├📂 tests/        # Pruebas unitarias para validar soluciones
 │  │  └📂 submissions/  # Soluciones enviadas por los participantes
 ├📂 .github/workflows/    # Automatización de ranking con GitHub Actions
 ├📂 scripts/              # Código para actualizar el ranking
 ├📄 RANKING.md            # Ranking de los participantes
 ├📄 LICENSE               # Licencia open-source
 └📄 README.md             # Descripción general del repositorio
```

📌 **Cada carpeta de reto debe seguir un formato específico para que sea detectado correctamente.**

---

## 📁 **Reglas para nombrar los retos correctamente**
Para que GitHub Actions asigne correctamente los puntos, cada reto debe seguir este formato:

```
reto-{nombre-del-reto}-{usuario-github}
```

**Ejemplos válidos:**
✅ `retos/reto-contar-vocales-jasonssdev/`  
✅ `retos/reto-predict-stock-maria123/`  
✅ `retos/reto-clustering-datos-carlosdev/`  

📌 **Si no sigues este formato, tu contribución no será reconocida en el ranking.**

---

## 🤝 **Cómo participar y contribuir**
👉 Sigue estos pasos para **crear o resolver un reto**:

### 1️⃣ **Clona el repositorio**
```bash
git clone git@github.com:pydatapanama/pydatapanama-retos.git
cd pydatapanama-retos
```

### 2️⃣ **Crea un nuevo branch con tu usuario**
```bash
git checkout -b reto-{nombre-del-reto}-{tu_usuario}
```

### 3️⃣ **Crea o resuelve un reto**
- **Para crear un reto:**
  ```bash
  cp -r retos/reto-template-usuario retos/reto-{nombre-del-reto}-{tu_usuario}
  ```
  Luego edita el **README.md** con la descripción del reto.

- **Para resolver un reto existente:**
  - Ve a la carpeta del reto.
  - Agrega tu solución dentro de `submissions/` con tu nombre de usuario.
  ```bash
  cd retos/reto-contar-vocales-jasonssdev/submissions
  touch solucion-jasonssdev.ipynb
  ```

### 4️⃣ **Sube tu branch y haz un Pull Request**
```bash
git add .
git commit -m "📝 Añadiendo nuevo reto sobre {tema}"
git push origin reto-{nombre-del-reto}-{tu_usuario}
```

Luego, crea un **Pull Request** en GitHub para que tu reto o solución sea revisado e integrado.

---

## 🌟 **¡Gracias por contribuir!**
Si tienes dudas, pregunta en nuestra comunidad o abre un Issue en GitHub. 🎯

