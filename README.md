# 🚗 Dashboard de Análisis de Coches v2.1

[![Streamlit](https://img.shields.io/badge/streamlit-app-FF4B4B.svg)](https://analisis-de-anuncios-de-venta-de-coches.onrender.com)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Análisis interactivo de anuncios de venta de coches con 10 visualizaciones, filtros inteligentes y soporte de múltiples unidades.

**🌐 [Prueba la app en línea](https://analisis-de-anuncios-de-venta-de-coches.onrender.com)**

---

## ✨ Novedades v2.1

### 🌍 Conversión de Unidades
- Cambia entre **Millas** y **Kilómetros** con un click
- Todos los gráficos y métricas se actualizan automáticamente

### 📑 Filtros Organizados
- **Pestaña Básicos**: Año, condición, tipo de vehículo
- **Pestaña Avanzados**: Combustible, transmisión, fabricante

### 📊 Visualizaciones en Pestañas
- **Pestaña Visualizaciones**: Todos los gráficos interactivos
- **Pestaña Datos**: Tabla de datos con descarga CSV

---

## 🎯 Características

### 10 Gráficos Interactivos
- 📈 Condición vs Año del Modelo
- 💰 Histograma de Precio
- 🛣️ Histograma de Odómetro
- 📍 Scatter Odómetro vs Precio
- 📅 Tendencia de Precio
- 🏭 Precio por Fabricante
- 🚗 Conteo por Tipo
- ⚡ Transmisión vs Precio
- 🛢️ Combustible vs Precio
- 📊 Matriz de Correlación

### 8+ Métricas
- Total de anuncios
- Precio promedio y mediana
- Odómetro promedio (con conversión)
- Modelos únicos
- Días en lista
- Precio mín/máx
- Estadísticas avanzadas

---

## 🚀 Instalación Local

### Requisitos
- Python 3.8+
- pip

### Pasos

```bash
# 1. Clonar repositorio
git clone https://github.com/tu-usuario/dashboard-coches.git
cd dashboard-coches

# 2. Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar aplicación
streamlit run app_optimizado.py
```

La app se abrirá en `http://localhost:8501`

---

## 📖 Guía Rápida

### Cambiar Unidad de Distancia
En la parte superior encontrarás:
```
🌍 Unidad de distancia: [Millas ▼]
```
Selecciona **Kilómetros** y todos los valores se convierten automáticamente.

### Usar Filtros
**Barra Lateral:**
- 🔍 **Básicos**: Año, condición, tipo (uso frecuente)
- ⚡ **Avanzados**: Combustible, transmisión, fabricante

### Ver Gráficos
**Área Principal:**
- 📊 **Visualizaciones**: Selecciona y explora 10 gráficos
- 📋 **Datos**: Tabla formateada con descarga CSV

---

## 💡 Casos de Uso

### 1. Encontrar Buen Precio en Buen Estado
```
1. Filtros Básicos → Selecciona "like new" y "excellent"
2. Visualizaciones → "Precio Promedio por Año"
3. Datos → Descarga CSV
```

### 2. Analizar Impacto del Kilometraje
```
1. Unidad → Tu preferencia
2. Visualizaciones → "Scatter Odómetro vs Precio"
3. Ve la correlación y distribución
```

### 3. Comparar Fabricantes
```
1. Filtros Avanzados → Selecciona marcas
2. Visualizaciones → "Precio por Fabricante"
3. Datos → Exporta resultados
```

---

## 🔧 Stack Tecnológico

| Componente | Tecnología |
|---|---|
| Framework | Streamlit |
| Visualización | Plotly |
| Datos | Pandas |
| Computación | NumPy |
| Lenguaje | Python 3.8+ |

---

## 📊 Comparación de Versiones

| Característica | v1.0 | v2.0 | v2.1 |
|---|:---:|:---:|:---:|
| Gráficos | 6 | 10 | 10 |
| Filtros organizados | ❌ | ❌ | ✅ |
| Conversión unidades | ❌ | ❌ | ✅ |
| Pestañas | ❌ | ❌ | ✅ |
| Exportar CSV | ❌ | ✅ | ✅ |

---

## 🐛 Solución de Problemas

**Error: "vehicles_us.csv not found"**
```bash
# Asegúrate que el archivo está en la misma carpeta
ls -la vehicles_us.csv
```

**La app es lenta**
```bash
# Limpia caché
streamlit cache clear
streamlit run app_optimizado.py
```

**Los gráficos no se actualizan**
```bash
# Verifica filtros y recarga
# Presiona R en la app
```

---

## 📁 Estructura del Proyecto

```
dashboard-coches/
├── app_optimizado.py       # Aplicación principal
├── vehicles_us.csv         # Dataset
├── requirements.txt        # Dependencias
├── README.md              # Este archivo
├── CAMBIOS_v2.1.md        # Cambios técnicos
└── docs/                  # Documentación adicional
```

---

## 📋 Requisitos (requirements.txt)

```
streamlit>=1.28.0
pandas>=2.0.0
plotly>=5.17.0
numpy>=1.24.0
```

Instálalo con:
```bash
pip install -r requirements.txt
```

---

## ✨ Mejoras Técnicas v2.1

- ✅ Conversión dinámmica de unidades
- ✅ Filtros en pestañas para mejor organización
- ✅ Visualizaciones separadas en pestaña dedicada
- ✅ Datos originales preservados (sin modificaciones)
- ✅ Labels dinámicas que se adaptan a unidades
- ✅ Mejor rendimiento y navegación


---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el repositorio
2. Crea una rama (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Eres libre de usar, modificar y distribuir.

---

## 📞 Contacto

- 📧 Email: [tu-email@ejemplo.com]
- 🐛 Issues: Reporta bugs en GitHub
- 💡 Sugerencias: Abre una discussion

---

## 🙏 Agradecimientos

- Streamlit por el framework
- Plotly por visualizaciones
- Pandas por procesamiento de datos
- La comunidad Python

---

<div align="center">

### 🌐 [Prueba la App en Línea](https://analisis-de-anuncios-de-venta-de-coches.onrender.com)

</div>
