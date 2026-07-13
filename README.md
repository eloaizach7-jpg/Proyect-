#  Análisis de Anuncios de Venta de Coches
# 🚗 Dashboard de Análisis de Anuncios de Venta de Coches

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

Una aplicación web interactiva y profesional para analizar datos de anuncios de venta de coches con visualizaciones dinámicas, filtros avanzados y estadísticas detalladas.

---

## ✨ Características Principales

### 📊 Visualizaciones Avanzadas
- 📈 **10 gráficos interactivos** diferentes
- 🎨 Paletas de colores profesionales
- 🔍 Zoom, pan y descarga de gráficos en PNG
- 📱 Interfaz responsive (desktop y móvil)

### 🔧 Filtros Dinámicos
- ⏰ Rango de año del modelo
- 🏷️ Condición, tipo de vehículo, combustible
- ⚡ Transmisión y fabricante
- 🎯 Aplicación en tiempo real

### 📈 Métricas y Estadísticas
- 💰 Precio promedio, mediana, mín y máx
- 🛣️ Odómetro promedio
- 📊 8+ métricas principales
- 🔬 Estadísticas avanzadas (desviación estándar, skewness, IQR)

### 📥 Exportación de Datos
- 📋 Tabla de datos filtrados con formato
- 📥 Descarga en CSV
- 🔄 Reordenamiento y selección de columnas
- 💾 Preserva todos los filtros aplicados

### 🔮 Opciones Avanzadas
- 🎚️ Selector de modo histograma (overlay/stack)
- 📊 Matriz de correlación interactiva
- 🧮 Análisis estadístico profundo
- 🎯 Análisis por subcategorías

---

## 🚀 Inicio Rápido

### Requisitos Previos
- **Python** 3.8 o superior
- **pip** (gestor de paquetes de Python)
- Archivo `vehicles_us.csv` en la carpeta del proyecto

### Instalación

#### 1️⃣ Clona o descarga el repositorio
```bash
git clone https://github.com/tu-usuario/dashboard-coches.git
cd dashboard-coches
```

#### 2️⃣ Crea un entorno virtual (recomendado)
```bash
# En Windows
python -m venv venv
venv\Scripts\activate

# En macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

#### 3️⃣ Instala las dependencias
```bash
pip install -r requirements.txt
```

#### 4️⃣ Ejecuta la aplicación
```bash
streamlit run app_optimizado.py
```

La aplicación se abrirá automáticamente en `http://localhost:8501`

---

## 📖 Cómo Usar

### Interface Principal

#### 1. **Barra de Filtros Lateral**
```
⚙️ Filtros de datos
├── Rango de año del modelo (slider)
├── Condición (multiselect)
├── Tipo de vehículo (multiselect)
├── Combustible (multiselect)
├── Transmisión (multiselect)
├── Fabricante (multiselect)
├── Modo de histograma (overlay/stack)
└── 🔧 Opciones avanzadas (checkbox)
```

**Tip:** Los filtros se aplican en tiempo real. Todos están seleccionados por defecto para ver todos los datos.

#### 2. **Métricas Principales**
Muestra 8 métricas resumen:
- Total de anuncios filtrados
- Precio promedio y mediana
- Odómetro promedio
- Modelos únicos
- Precio mín/máx
- Días promedio listado

#### 3. **Selector de Gráficos**
Elige entre 10 visualizaciones diferentes:

| Gráfico | Descripción | Mejor Para |
|---------|------------|-----------|
| 📈 Condición vs Año | Histograma agrupado | Ver tendencias por año |
| 💰 Histograma de Precio | Distribución de precios | Identificar rangos comunes |
| 🛣️ Histograma Odómetro | Distribución kilometraje | Analizar desgaste |
| 📍 Dispersión Odómetro-Precio | Relación entre variables | Correlaciones |
| 📅 Precio por Año | Línea de tendencia | Evolución temporal |
| 🏭 Precio por Fabricante | Top 15 fabricantes | Comparar marcas |
| 🚗 Conteo por Tipo | Barras horizontales | Ver disponibilidad |
| ⚡ Transmisión vs Precio | Box plot | Comparar distribuciones |
| 🛢️ Combustible vs Precio | Box plot | Análisis por fuel type |
| 📊 Matriz Correlación | Heatmap interactivo | Relaciones numéricas |

#### 4. **Tabla de Datos**
Expande la sección para:
- ✅ Seleccionar columnas a mostrar
- 📊 Reordenar por cualquier columna
- 📥 Descargar como CSV
- 🔍 Buscar valores específicos

---

## 🏗️ Estructura del Proyecto

```
dashboard-coches/
│
├── 📄 app_optimizado.py          # Aplicación principal
├── 📄 vehicles_us.csv             # Dataset (no incluido)
├── 📄 requirements.txt            # Dependencias
│
├── 📁 docs/
│   ├── MEJORAS_REALIZADAS.md     # Cambios implementados
│   ├── ROADMAP_FUTURO.md         # Mejoras planeadas
│   └── README.md                  # Este archivo
│
└── 📁 .gitignore                  # Archivos ignorados por Git
```

### Archivos Principales

**`app_optimizado.py`** (600+ líneas)
- Carga y limpieza de datos
- Configuración de página
- Barra lateral de filtros
- Métricas dinámicas
- 10 visualizaciones interactivas
- Tabla de datos exportable
- Estadísticas avanzadas

---

## 📊 Visualizaciones Detalladas

### 1. Condición vs Año del Modelo
- **Tipo:** Histograma agrupado
- **Eje X:** Año del modelo
- **Eje Y:** Cantidad de vehículos
- **Color:** Condición del vehículo
- **Uso:** Identificar cuándo se venden más vehículos de cada condición

### 2. Histograma de Precio
- **Tipo:** Histograma con color por condición
- **Modos:** Overlay (transparente) o Stack (apilado)
- **Bins:** 50 intervalos de precio
- **Uso:** Ver distribución de precios, identificar outliers

### 3. Dispersión: Odómetro vs Precio
- **Tipo:** Scatter plot
- **Tamaño de punto:** Días listados
- **Color:** Condición del vehículo
- **Información hover:** Modelo, año, tipo, transmisión
- **Estadística:** Correlación mostrada
- **Uso:** Analizar impacto del kilometraje en precio

### 4. Precio Promedio por Año
- **Tipo:** Línea con banda de confianza
- **Línea azul:** Precio promedio
- **Línea naranja:** Mediana
- **Banda gris:** ±1 desviación estándar
- **Uso:** Ver tendencia de precios en el tiempo

### 5. Box Plots (Transmisión y Combustible)
- **Tipo:** Caja y bigotes
- **Muestra:** Distribución por categoría
- **Elementos:** Q1, mediana, Q3, outliers
- **Uso:** Comparar distribuciones entre categorías

### 6. Matriz de Correlación
- **Tipo:** Heatmap interactivo
- **Rango:** -1 a +1
- **Colores:** Rojo (negativo) a Azul (positivo)
- **Variables:** Precio, Odómetro, Año, Días Listado
- **Uso:** Identificar relaciones entre variables

---

## 🔧 Opciones Avanzadas

Active el checkbox "🔧 Opciones avanzadas" en la barra lateral para acceder a:

### Filtro Personalizado de Precios
```
Rango de precios a visualizar:
[Mín: $1,000] ----[-----]---- [Máx: $50,000]
```
Permite hacer zoom en rangos específicos de precios

### Estadísticas Avanzadas
- **Precio:**
  - Desviación Estándar
  - Rango Intercuartil (Q1-Q3)
  - Skewness (asimetría)
  
- **Odómetro:**
  - Desviación Estándar
  - Rango Intercuartil
  - Skewness

---

## 📥 Exportar Datos

### Descargar como CSV
1. Expande "📋 Ver tabla de datos filtrados"
2. Personaliza columnas si lo deseas
3. Selecciona orden (ascendente/descendente)
4. Haz clic en "📥 Descargar CSV"

El archivo CSV incluirá:
- ✅ Solo datos filtrados
- ✅ Columnas seleccionadas
- ✅ Orden elegido
- ✅ Nombre: `datos_filtrados.csv`

---

## 🔄 Flujo de Datos

```
📁 vehicles_us.csv
        ↓
    Carga con Pandas
        ↓
    Limpieza de datos
    ├── Convertir tipos
    ├── Llenar NaN
    ├── Validar precios
    └── Extraer fabricante
        ↓
    Aplicar filtros
    ├── Año modelo
    ├── Condición
    ├── Tipo vehículo
    ├── Combustible
    ├── Transmisión
    └── Fabricante
        ↓
    Calcular métricas
        ↓
    Generar visualizaciones
        ↓
    Mostrar en Streamlit
```

---

## ⚙️ Configuración

### Variables de Entorno (Opcional)
```bash
# .env
DATA_PATH=./data/vehicles_us.csv
DEBUG=False
MAX_ROWS=100000
```

### Configuración de Streamlit
El archivo `app_optimizado.py` incluye:
```python
st.set_page_config(
    page_title='Análisis de Anuncios de Coches',
    layout='wide',
    initial_sidebar_state='expanded'
)
```

---

## 🐛 Troubleshooting

### ❌ Error: "vehicles_us.csv not found"
```
Solución: Asegúrate de que el archivo CSV está en la misma carpeta
que app_optimizado.py
```

### ❌ Error: "ModuleNotFoundError"
```bash
# Reinstala las dependencias
pip install --upgrade -r requirements.txt
```

### ❌ La app es lenta
```bash
# Streamlit recompila con cada cambio
# Para modo de reloj: Ctrl+Shift+R en la app
# O ejecuta con:
streamlit run app_optimizado.py --client.showErrorDetails=false
```

### ❌ Los gráficos no se muestran
```bash
# Intenta limpiar caché
streamlit cache clear
streamlit run app_optimizado.py
```

### ❌ Error de memoria
```python
# Si el dataset es muy grande, filtra en carga:
car_data = pd.read_csv('vehicles_us.csv', nrows=50000)
```

---

## 📊 Ejemplo de Uso

### Caso 1: Buscar Coches Baratos en Buen Estado

1. **Filtros a aplicar:**
   - Condición: Selecciona solo "like new" y "excellent"
   - Año: Mantén rango completo
   
2. **Gráfico a usar:**
   - "Precio promedio por Año"
   
3. **Resultado:**
   - Verás qué años tienen mejor precio en buena condición

### Caso 2: Analizar Impacto del Km en Precio

1. **Gráfico a usar:**
   - "Dispersión: Odómetro vs Precio"
   
2. **Observa:**
   - La correlación mostrada en la app
   - Cómo se agrupan por condición
   
3. **Exporta:**
   - Descarga los datos para análisis más profundo

### Caso 3: Comparar Fabricantes

1. **Gráfico a usar:**
   - "Precio promedio por Fabricante"
   
2. **Filtra:**
   - Por tipo de vehículo si lo deseas
   - Verás ranking de marcas por precio

---

## 🚀 Mejoras Realizadas (vs Original)

| Característica | Antes | Después |
|---|---|---|
| **Gráficos** | 6 | 10 |
| **Validación datos** | ❌ | ✅ |
| **Caché** | ❌ | ✅ |
| **Métricas** | 6 | 8+ |
| **Exportar CSV** | ❌ | ✅ |
| **Opciones avanzadas** | ❌ | ✅ |
| **Diseño UI** | Básico | Profesional |
| **Errores tratados** | ❌ | ✅ |

📖 Ver archivo **MEJORAS_REALIZADAS.md** para detalles completos.

---

## 🔮 Roadmap (Próximas Mejoras)

### Corto Plazo (Fácil) 📊
- [ ] Comparador de modelos (lado a lado)
- [ ] Badges de "Ganga" (precio muy bajo)
- [ ] Historial de búsquedas

### Mediano Plazo (Moderado) 🤖
- [ ] Predictor de precios con ML
- [ ] Dashboard de alertas
- [ ] Box plot segmentado
- [ ] Análisis de regresión

### Largo Plazo (Complejo) 🚀
- [ ] Mapas interactivos (Folium)
- [ ] API de datos en vivo
- [ ] Sistema multi-usuario (Firebase)
- [ ] Análisis de sentimiento

📖 Ver archivo **ROADMAP_FUTURO.md** para ideas de código.

---

## 📚 Stack Tecnológico

| Componente | Tecnología | Versión |
|---|---|---|
| **Framework Frontend** | Streamlit | 1.28.0+ |
| **Análisis de datos** | Pandas | 2.0.0+ |
| **Visualización** | Plotly | 5.17.0+ |
| **Lenguaje** | Python | 3.8+ |
| **Computación** | NumPy | 1.24.0+ |

---

## 🔐 Seguridad

- ✅ Sin almacenamiento de datos sensibles
- ✅ Datos procesados localmente
- ✅ Sin conexión a bases de datos externas
- ✅ Archivo CSV no modificado
- ⚠️ Asegúrate de no compartir datos personales en el CSV

---

## 📄 Licencia

Este proyecto está bajo la licencia **MIT**. Eres libre de:
- ✅ Usar en proyectos personales o comerciales
- ✅ Modificar el código
- ✅ Distribuir
- ✅ Usar privadamente

Simplemente incluye una copia de la licencia.

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Para contribuir:

1. **Fork** el repositorio
2. **Crea una rama** para tu feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. **Push** a la rama (`git push origin feature/AmazingFeature`)
5. **Abre un Pull Request**

### Áreas donde se busca ayuda:
- 🐛 Reporte de bugs
- 🎨 Mejoras de UI/UX
- 📊 Nuevas visualizaciones
- 📖 Documentación
- 🧪 Tests

---

## 📧 Contacto y Soporte

### ¿Preguntas o sugerencias?
- 📧 **Email:** [tu-email@ejemplo.com]
- 🐛 **Issues:** [Abre un issue en GitHub]
- 💬 **Discussions:** [Participa en discusiones]

### Reportar un Bug
Crea un issue con:
- Descripción clara del problema
- Pasos para reproducir
- Versión de Python y Streamlit
- Captura de pantalla si aplica

---

## 📊 Estadísticas del Proyecto

- 📝 **Líneas de código:** 600+
- 📊 **Visualizaciones:** 10
- 🔧 **Filtros:** 6
- ⚡ **Optimizaciones:** 12+
- 📚 **Documentación:** Completa

---

## 🙏 Agradecimientos

- 🎨 Plotly por excelentes gráficos
- 🐍 Streamlit por framework innovador
- 🐼 Pandas por procesamiento de datos
- 👥 La comunidad de código abierto

---

## 📖 Recursos Adicionales

- [Documentación Streamlit](https://docs.streamlit.io/)
- [Documentación Plotly](https://plotly.com/python/)
- [Documentación Pandas](https://pandas.pydata.org/docs/)
- [Python Official Docs](https://docs.python.org/3/)

---

## ⭐ Si te gustó este proyecto

Por favor, dale una estrella ⭐ en GitHub y comparte con otros.

---

**Versión:** 2.0 Optimizada  
**Última actualización:** Diciembre 2024  
**Mantenedor:** [Tu Nombre]  
**Estado:** ✅ Activo y listo para producción

---

<div align="center">

### 🚀 Hecho con ❤️ usando Python, Streamlit y Plotly

[⬆ Volver arriba](#-dashboard-de-análisis-de-anuncios-de-venta-de-coches)

</div>
