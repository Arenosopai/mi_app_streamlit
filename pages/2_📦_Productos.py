import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ── Configuración de página ──────────────────────────────────────────────────
st.set_page_config(page_title="Productos", page_icon="📦")

# ── Título principal ─────────────────────────────────────────────────────────
st.title("📦 Catálogo de Productos")

# ── Imagen desde Unsplash ────────────────────────────────────────────────────
st.image(
    "https://images.unsplash.com/photo-1607082348824-0a96f2a4b9da?w=900&auto=format&fit=crop",
    caption="Nuestro inventario de productos",
    use_column_width=True,
)

st.divider()

# ── DataFrame de productos ───────────────────────────────────────────────────
productos = pd.DataFrame({
    "Nombre":    ["Laptop Pro",   "Teclado Mecánico", "Monitor 4K",  "Mouse Inalámbrico", "Auriculares BT", "Silla Ergonómica", "Webcam HD"],
    "Categoría": ["Computadores", "Accesorios",       "Computadores", "Accesorios",        "Audio",          "Mobiliario",       "Accesorios"],
    "Precio ($)": [3_200_000,     180_000,             950_000,        85_000,              320_000,          780_000,            150_000],
    "Stock":     [12,             45,                  8,              60,                  25,               10,                 30],
})

# ── Métrica total de productos ───────────────────────────────────────────────
st.metric(label="Total de productos en catálogo", value=len(productos))

st.divider()

# ── Filtro por categoría ─────────────────────────────────────────────────────
categorias_disponibles = sorted(productos["Categoría"].unique())
seleccion = st.multiselect(
    "🔍 Filtrar por categoría:",
    options=categorias_disponibles,
    default=categorias_disponibles,
)

df_filtrado = productos[productos["Categoría"].isin(seleccion)]

# ── Tabla filtrada ───────────────────────────────────────────────────────────
st.subheader("📋 Productos")
st.dataframe(df_filtrado.reset_index(drop=True), use_container_width=True)

# ── Gráfico de barras: Precio por producto ───────────────────────────────────
st.subheader("💰 Precio por producto")

if df_filtrado.empty:
    st.warning("Selecciona al menos una categoría para ver el gráfico.")
else:
    fig, ax = plt.subplots(figsize=(9, 4))
    colores = plt.cm.tab10.colors[: len(df_filtrado)]
    bars = ax.barh(df_filtrado["Nombre"], df_filtrado["Precio ($)"], color=colores)

    ax.set_xlabel("Precio (COP $)")
    ax.set_title("Precio por producto")
    ax.bar_label(bars, fmt="$ {:,.0f}", padding=4, fontsize=8)
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"${x:,.0f}"))
    ax.invert_yaxis()
    plt.tight_layout()
    st.pyplot(fig)