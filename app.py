from pathlib import Path
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# ==================== CONFIGURACIÓN ====================
st.set_page_config(
    page_title='Análisis de Anuncios de Coches',
    layout='wide',
    initial_sidebar_state='expanded'
)

# Estilos personalizados
st.markdown("""
    <style>
    .main {
        padding-top: 1rem;
    }
    .metric-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
    }
    h1 {
        color: #1f77b4;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    h3 {
        color: #2c3e50;
        border-bottom: 3px solid #3498db;
        padding-bottom: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# ==================== CARGA Y LIMPIEZA DE DATOS ====================
@st.cache_data
def load_and_clean_data():
    base_dir = Path(__file__).resolve().parent
    data_path = base_dir / 'vehicles_us.csv'
    car_data = pd.read_csv(data_path)
    
    # Limpieza de datos
    car_data['model_year'] = pd.to_numeric(car_data['model_year'], errors='coerce').astype('Int64')
    car_data['price'] = pd.to_numeric(car_data['price'], errors='coerce')
    car_data['odometer'] = pd.to_numeric(car_data['odometer'], errors='coerce')
    car_data['days_listed'] = pd.to_numeric(car_data['days_listed'], errors='coerce').astype('Int64')
    
    # Llenar valores faltantes
    car_data['condition'] = car_data['condition'].fillna('unknown')
    car_data['fuel'] = car_data['fuel'].fillna('unknown')
    car_data['transmission'] = car_data['transmission'].fillna('unknown')
    car_data['type'] = car_data['type'].fillna('unknown')
    car_data['model'] = car_data['model'].fillna('unknown')
    
    # Extraer fabricante del modelo
    car_data['manufacturer'] = (
        car_data['model']
        .astype(str)
        .str.strip()
        .str.split(r'\s+', expand=True)[0]
        .str.lower()
        .replace({'': 'unknown'})
    )
    
    # Eliminar registros con precios inválidos
    car_data = car_data[(car_data['price'] > 0) & (car_data['price'] < 1000000)]
    
    return car_data

car_data = load_and_clean_data()

# ==================== HEADER ====================
col_header1, col_header2 = st.columns([3, 1])
with col_header1:
    st.title('🚗 Análisis de Anuncios de Venta de Coches')
    st.markdown('*Explora datos interactivos con filtros dinámicos y visualizaciones avanzadas*')

with col_header2:
    st.metric('📊 Total de registros', f'{len(car_data):,}')

st.markdown('---')
st.selectbox(
    '🌍 Unidad de distancia',
    ['Millas', 'Kilómetros'],
    index=0,
    key='distance_unit_top',
    help='Cambia la unidad usada en odómetro, métricas y gráficos.'
)

distance_unit = st.session_state.distance_unit_top

# ==================== BARRA LATERAL DE FILTROS ====================
st.sidebar.header('⚙️ Filtros de datos')

# Crear pestañas en la barra lateral
filter_tabs = st.sidebar.tabs(['🔍 Básicos', '⚡ Avanzados'])

with filter_tabs[0]:  # Filtros Básicos
    st.markdown('### Filtros Principales')
    
    # Filtro de año
    model_year_min = int(car_data['model_year'].min(skipna=True))
    model_year_max = int(car_data['model_year'].max(skipna=True))
    year_range = st.slider(
        'Rango de año del modelo',
        min_value=model_year_min,
        max_value=model_year_max,
        value=(model_year_min, model_year_max),
        key='year_slider'
    )
    
    # Condición
    selected_conditions = st.multiselect(
        'Condición',
        sorted(car_data['condition'].unique()),
        default=sorted(car_data['condition'].unique()),
        key='condition_filter_basic'
    )
    
    # Tipo de vehículo
    selected_types = st.multiselect(
        'Tipo de vehículo',
        sorted(car_data['type'].unique()),
        default=sorted(car_data['type'].unique()),
        key='type_filter_basic'
    )

with filter_tabs[1]:  # Filtros Avanzados
    st.markdown('### Filtros Avanzados')
    
    # Combustible
    selected_fuels = st.multiselect(
        'Combustible',
        sorted(car_data['fuel'].unique()),
        default=sorted(car_data['fuel'].unique()),
        key='fuel_filter_adv'
    )
    
    # Transmisión
    selected_transmissions = st.multiselect(
        'Transmisión',
        sorted(car_data['transmission'].unique()),
        default=sorted(car_data['transmission'].unique()),
        key='transmission_filter_adv'
    )
    
    # Fabricante
    selected_manufacturers = st.multiselect(
        'Fabricante',
        sorted(car_data['manufacturer'].unique()),
        default=sorted(car_data['manufacturer'].unique())[:10],
        key='manufacturer_filter_adv'
    )
    
    # Opciones de visualización
    st.markdown('---')
    st.markdown('#### Visualización')
    
    histogram_mode = st.selectbox(
        'Modo de histograma',
        ['overlay', 'stack'],
        help='overlay: barras transparentes | stack: barras apiladas',
        key='histogram_mode_adv'
    )
    
    show_advanced = st.checkbox('🔧 Mostrar estadísticas avanzadas', value=False, key='show_advanced_stats')

# ==================== APLICAR FILTROS ====================
filtered_data = car_data[
    (car_data['model_year'] >= year_range[0]) &
    (car_data['model_year'] <= year_range[1]) &
    (car_data['condition'].isin(selected_conditions)) &
    (car_data['type'].isin(selected_types)) &
    (car_data['fuel'].isin(selected_fuels)) &
    (car_data['transmission'].isin(selected_transmissions)) &
    (car_data['manufacturer'].isin(selected_manufacturers))
]

# Validación de datos filtrados
if len(filtered_data) == 0:
    st.warning('⚠️ No hay datos que coincidan con los filtros seleccionados. Por favor, ajusta los filtros.')
    st.stop()

# ==================== MÉTRICAS ====================
st.markdown('### 📈 Métricas Principales')

conversion_factor = 1.60934 if distance_unit == 'Kilómetros' else 1.0
unit_label = 'km' if distance_unit == 'Kilómetros' else 'mi'
odometer_axis_label = f'Odómetro ({unit_label})'

display_data = filtered_data.copy()
display_data['odometer'] = (display_data['odometer'] * conversion_factor).round(0).astype('Int64')

total_listings = len(filtered_data)
avg_price = filtered_data['price'].mean()
median_price = filtered_data['price'].median()
avg_odometer = display_data['odometer'].mean()
unique_models = filtered_data['model'].nunique()
min_price = filtered_data['price'].min()
max_price = filtered_data['price'].max()
avg_days = filtered_data['days_listed'].mean()

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        '📋 Anuncios',
        f'{total_listings:,}',
        delta=f'{(total_listings/len(car_data)*100):.1f}% del total'
    )

with col2:
    st.metric(
        '💵 Precio Promedio',
        f'${avg_price:,.0f}' if not pd.isna(avg_price) else 'N/A',
        delta=f'Mediana: ${median_price:,.0f}' if not pd.isna(median_price) else 'N/A'
    )

with col3:
    st.metric(
        '⏱️ Odómetro Promedio',
        f'{avg_odometer:,.0f} {unit_label}' if not pd.isna(avg_odometer) else 'N/A'
    )

with col4:
    st.metric(
        '🔧 Modelos Únicos',
        f'{unique_models:,}'
    )

with col5:
    st.metric(
        '📅 Días Listado Prom.',
        f'{avg_days:.0f}' if not pd.isna(avg_days) else 'N/A'
    )

# Rango de precios
col6, col7 = st.columns(2)
with col6:
    st.metric('💲 Precio Mínimo', f'${min_price:,.0f}' if not pd.isna(min_price) else 'N/A')
with col7:
    st.metric('💲 Precio Máximo', f'${max_price:,.0f}' if not pd.isna(max_price) else 'N/A')

# ==================== VISUALIZACIÓN EN PESTAÑAS ====================
visual_tab, data_tab = st.tabs(['📊 Visualizaciones', '📋 Datos'])

with visual_tab:
    st.markdown('---')
    st.markdown('### 📊 Selecciona una visualización')
    chart_type = st.selectbox(
        'Selecciona un gráfico',
        [
            '📈 Condición vs Año del Modelo',
            '💰 Histograma de Precio',
            '🛣️ Histograma de Odómetro',
            '📍 Dispersión: Odómetro vs Precio',
            '📅 Precio Promedio por Año',
            '🏭 Precio Promedio por Fabricante',
            '🚗 Conteo por Tipo de Vehículo',
            '⚡ Transmisión vs Precio',
            '🛢️ Combustible vs Precio',
            '📊 Matriz de Correlación (Avanzado)'
        ]
    )

    st.markdown('---')
    
    if chart_type == '📈 Condición vs Año del Modelo':
        st.subheader('Comparación de Condición por Año del Modelo')
        st.info('Visualiza cómo la condición de los vehículos se distribuye a través de los años (agrupado en intervalos de 5 años).')
        
        df_plot = filtered_data.dropna(subset=['model_year']).copy()
        
        if len(df_plot) > 0:
            # Crear intervalos de 5 años
            min_year = int(df_plot['model_year'].min())
            max_year = int(df_plot['model_year'].max())
            
            # Crear etiquetas de intervalos de 5 años
            bins = list(range(min_year, max_year + 6, 5))
            df_plot['year_interval'] = pd.cut(df_plot['model_year'], bins=bins, right=False, 
                                               labels=[f'{int(bins[i])}-{int(bins[i+1]-1)}' for i in range(len(bins)-1)])
            
            # Contar por intervalo y condición
            df_interval = df_plot.groupby(['year_interval', 'condition'], observed=True).size().reset_index(name='count')
            
            fig = px.bar(
                df_interval,
                x='year_interval',
                y='count',
                color='condition',
                barmode='group',
                category_orders={'condition': sorted(df_plot['condition'].unique())},
                labels={'year_interval': 'Rango de Años', 'count': 'Cantidad', 'condition': 'Condición'},
                title='Condición vs Rango de Año del Modelo',
                color_discrete_sequence=px.colors.qualitative.Set2,
            )
            fig.update_layout(
                hovermode='x unified',
                height=500,
                xaxis_title='Rango de Años',
                yaxis_title='Cantidad'
            )
            st.plotly_chart(fig, width='stretch')

    elif chart_type == '💰 Histograma de Precio':
        st.subheader('Distribución de Precios')
        st.info('Observe cómo varían los precios según la condición del vehículo.')
        
        if show_advanced:
            price_min, price_max = st.slider(
                'Rango de precios a visualizar',
                int(filtered_data['price'].min()),
                int(filtered_data['price'].max()),
                (int(filtered_data['price'].min()), int(filtered_data['price'].max()))
            )
            df_price = filtered_data[(filtered_data['price'] >= price_min) & (filtered_data['price'] <= price_max)]
        else:
            df_price = filtered_data
        
        fig = px.histogram(
            df_price,
            x='price',
            color='condition',
            barmode=histogram_mode,
            opacity=0.75,
            nbins=50,
            title='Distribución de Precio por Condición',
            labels={'price': 'Precio (USD)', 'count': 'Cantidad'},
            category_orders={'condition': sorted(df_price['condition'].unique())},
            color_discrete_sequence=px.colors.qualitative.Plotly
        )
        fig.update_layout(
            legend_title_text='Condición',
            hovermode='x unified',
            height=500
        )
        st.plotly_chart(fig, width='stretch')

    elif chart_type == '🛣️ Histograma de Odómetro':
        st.subheader('Distribución del Odómetro')
        st.info('Análisis del desgaste de los vehículos según su condición.')
        
        fig = px.histogram(
            display_data,
            x='odometer',
            color='condition',
            barmode=histogram_mode,
            opacity=0.75,
            nbins=50,
            title='Distribución del Odómetro por Condición',
            labels={'odometer': odometer_axis_label, 'count': 'Cantidad'},
            category_orders={'condition': sorted(filtered_data['condition'].unique())},
            color_discrete_sequence=px.colors.qualitative.Plotly
        )
        fig.update_layout(
            legend_title_text='Condición',
            hovermode='x unified',
            height=500
        )
        fig.update_xaxes(title_text=odometer_axis_label, tickformat='~s', tickangle=-30)
        st.plotly_chart(fig, width='stretch')

    elif chart_type == '📍 Dispersión: Odómetro vs Precio':
        st.subheader('Relación entre Odómetro y Precio')
        st.info('Explorar cómo el kilometraje afecta el valor del vehículo.')
        
        correlation = display_data[['odometer', 'price']].corr().iloc[0, 1]
        st.markdown(f'**Correlación Odómetro-Precio:** {correlation:.3f}')
        
        fig = px.scatter(
            display_data,
            x='odometer',
            y='price',
            color='condition',
            size='days_listed' if 'days_listed' in filtered_data.columns else None,
            hover_data=['model', 'model_year', 'type', 'transmission'],
            title='Odómetro vs Precio (tamaño = días listados)',
            labels={'odometer': odometer_axis_label, 'price': 'Precio (USD)'},
            color_discrete_sequence=px.colors.qualitative.Vivid
        )
        fig.update_traces(marker=dict(size=8, opacity=0.6, line=dict(width=0.5)))
        fig.update_layout(height=600, hovermode='closest')
        fig.update_xaxes(title_text=odometer_axis_label, tickformat='~s', tickangle=-30)
        st.plotly_chart(fig, width='stretch')

    elif chart_type == '📅 Precio Promedio por Año':
        st.subheader('Tendencia del Precio a lo Largo de los Años')
        st.info('Observe cómo varían los precios según el año del modelo.')
        
        df_avg = filtered_data.groupby('model_year', dropna=True).agg({
            'price': ['mean', 'median', 'std'],
            'model': 'count'
        }).reset_index()
        df_avg.columns = ['model_year', 'price_mean', 'price_median', 'price_std', 'count']
        df_avg = df_avg.sort_values('model_year')
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=df_avg['model_year'],
            y=df_avg['price_mean'],
            name='Promedio',
            mode='lines+markers',
            line=dict(color='#1f77b4', width=3),
            marker=dict(size=8)
        ))
        fig.add_trace(go.Scatter(
            x=df_avg['model_year'],
            y=df_avg['price_median'],
            name='Mediana',
            mode='lines+markers',
            line=dict(color='#ff7f0e', width=2, dash='dash'),
            marker=dict(size=6)
        ))
        fig.add_trace(go.Scatter(
            x=df_avg['model_year'],
            y=df_avg['price_mean'] + df_avg['price_std'],
            fill=None,
            mode='lines',
            name='',
            line_color='rgba(0,0,0,0)',
            showlegend=False
        ))
        fig.add_trace(go.Scatter(
            x=df_avg['model_year'],
            y=df_avg['price_mean'] - df_avg['price_std'],
            fill='tonexty',
            mode='lines',
            name='±1 Desv. Est.',
            line_color='rgba(0,0,0,0)',
            fillcolor='rgba(31, 119, 180, 0.2)'
        ))
        fig.update_layout(
            title='Precio Promedio por Año del Modelo',
            xaxis_title='Año del Modelo',
            yaxis_title='Precio (USD)',
            hovermode='x unified',
            height=500
        )
        st.plotly_chart(fig, width='stretch')

    elif chart_type == '🏭 Precio Promedio por Fabricante':
        st.subheader('Comparación de Precio Promedio por Fabricante')
        st.info('Ranking de los fabricantes por precio promedio.')
        
        df_manu = (
            filtered_data.groupby('manufacturer', dropna=True).agg({
                'price': 'mean',
                'model': 'count'
            }).reset_index()
            .rename(columns={'price': 'avg_price', 'model': 'count'})
            .sort_values('avg_price', ascending=False)
        )
        
        top_n = min(15, len(df_manu))
        df_manu = df_manu.head(top_n)
        
        fig = px.bar(
            df_manu,
            x='manufacturer',
            y='avg_price',
            color='avg_price',
            color_continuous_scale='Viridis',
            title=f'Precio Promedio por Fabricante (Top {top_n})',
            labels={'manufacturer': 'Fabricante', 'avg_price': 'Precio Promedio (USD)'},
            hover_data={'count': True, 'avg_price': ':.0f'}
        )
        fig.update_layout(xaxis_tickangle=-45, height=500)
        st.plotly_chart(fig, width='stretch')

    elif chart_type == '🚗 Conteo por Tipo de Vehículo':
        st.subheader('Distribución de Vehículos por Tipo')
        st.info('Cantidad de anuncios disponibles para cada tipo de vehículo.')
        
        type_count = filtered_data['type'].value_counts().reset_index()
        type_count.columns = ['type', 'count']
        type_count = type_count.sort_values('count', ascending=False)
        
        fig = px.bar(
            type_count,
            x='type',
            y='count',
            color='count',
            color_continuous_scale='Blues',
            title='Distribución por Tipo de Vehículo',
            labels={'type': 'Tipo de Vehículo', 'count': 'Cantidad'},
            text='count'
        )
        fig.update_traces(textposition='outside')
        fig.update_layout(height=500, showlegend=False)
        st.plotly_chart(fig, width='stretch')

    elif chart_type == '⚡ Transmisión vs Precio':
        st.subheader('Análisis de Precio por Tipo de Transmisión')
        
        fig = px.box(
            filtered_data,
            x='transmission',
            y='price',
            color='transmission',
            title='Distribución de Precio por Transmisión',
            labels={'transmission': 'Transmisión', 'price': 'Precio (USD)'},
            color_discrete_sequence=px.colors.qualitative.Set2
        )
        fig.update_layout(height=500, showlegend=False)
        st.plotly_chart(fig, width='stretch')

    elif chart_type == '🛢️ Combustible vs Precio':
        st.subheader('Análisis de Precio por Tipo de Combustible')
        
        fig = px.box(
            filtered_data,
            x='fuel',
            y='price',
            color='fuel',
            title='Distribución de Precio por Combustible',
            labels={'fuel': 'Combustible', 'price': 'Precio (USD)'},
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        fig.update_layout(height=500, showlegend=False)
        st.plotly_chart(fig, width='stretch')

    elif chart_type == '📊 Matriz de Correlación (Avanzado)':
        st.subheader('Matriz de Correlación de Variables Numéricas')
        st.info('Identifica relaciones entre variables numéricas del dataset.')
        
        numeric_cols = display_data[['price', 'odometer', 'model_year', 'days_listed']].select_dtypes(include=['number']).dropna()
        
        if len(numeric_cols) > 0:
            corr_matrix = numeric_cols.corr()
            
            fig = px.imshow(
                corr_matrix,
                labels=dict(color='Correlación'),
                x=['Precio', 'Odómetro', 'Año', 'Días Listado'],
                y=['Precio', 'Odómetro', 'Año', 'Días Listado'],
                color_continuous_scale='RdBu',
                zmin=-1, zmax=1,
                text_auto=True,
                title='Matriz de Correlación'
            )
            fig.update_layout(height=500)
            st.plotly_chart(fig, width='stretch')

with data_tab:
    st.markdown('---')
    st.subheader('Datos Detallados')
    
    # Opciones de visualización
    cols_to_show = st.multiselect(
        'Selecciona las columnas a mostrar',
        display_data.columns.tolist(),
        default=['model', 'model_year', 'price', 'odometer', 'condition', 'type', 'transmission', 'fuel']
    )
    
    # Opción de orden
    order_col = st.selectbox('Ordenar por:', cols_to_show)
    order_asc = st.checkbox('Ascendente', value=True)
    
    df_display = display_data[cols_to_show].sort_values(order_col, ascending=order_asc).reset_index(drop=True)
    
    st.dataframe(
        df_display,
        height=400,
        use_container_width=True,
        column_config={
            'price': st.column_config.NumberColumn('Precio (USD)', format='$%,.0f'),
            'odometer': st.column_config.NumberColumn(f'Odómetro ({unit_label})', format='%,.0f'),
            'model_year': st.column_config.NumberColumn('Año', format='%d'),
            'days_listed': st.column_config.NumberColumn('Días', format='%d')
        }
    )
    
    # Descargar datos
    csv = df_display.to_csv(index=False)
    st.download_button(
        label='📥 Descargar CSV',
        data=csv,
        file_name='datos_filtrados.csv',
        mime='text/csv'
    )

# ==================== ESTADÍSTICAS AVANZADAS ====================
if show_advanced:
    st.markdown('---')
    st.markdown('### 🔬 Estadísticas Avanzadas')
    
    col_stats1, col_stats2 = st.columns(2)
    
    with col_stats1:
        st.markdown('#### Precio')
        st.write(f'**Desviación Estándar:** ${filtered_data["price"].std():,.2f}')
        st.write(f'**Rango Intercuartil (Q1-Q3):** ${filtered_data["price"].quantile(0.25):,.0f} - ${filtered_data["price"].quantile(0.75):,.0f}')
        st.write(f'**Skewness:** {filtered_data["price"].skew():.3f}')
    
    with col_stats2:
        st.markdown('#### Odómetro')
        st.write(f'**Desviación Estándar:** {display_data["odometer"].std():,.0f} {unit_label}')
        st.write(f'**Rango Intercuartil (Q1-Q3):** {display_data["odometer"].quantile(0.25):,.0f} - {display_data["odometer"].quantile(0.75):,.0f} {unit_label}')
        st.write(f'**Skewness:** {display_data["odometer"].skew():.3f}')

st.markdown('---')
st.markdown('<p style="text-align: center; color: gray; font-size: 0.9em;">📊 Dashboard de Análisis de Anuncios de Coches | Desarrollado con Streamlit & Plotly</p>', unsafe_allow_html=True)