import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date

# ── 1. CONFIGURACIÓN DE PÁGINA ───────────────────────────────────────────────
st.set_page_config(page_title="Reportes", page_icon="📊")

# ── 2. TÍTULO PRINCIPAL ──────────────────────────────────────────────────────
st.title("📊 Dashboards y Reportes")
st.divider()

# ── 3. KPIs — TARJETAS DE MÉTRICAS ──────────────────────────────────────────
col1, col2, col3 = st.columns(3)

col1.metric(
    label="💰 Ventas Totales",
    value="$ 48.500.000",
    delta="↑ 12% vs mes anterior",
)
col2.metric(
    label="👥 Clientes Activos",
    value="1.340",
    delta="↑ 58 nuevos",
)
col3.metric(
    label="📦 Productos Vendidos",
    value="3.872",
    delta="↓ 3% vs mes anterior",
    delta_color="inverse",
)

st.divider()

# ── 4. DATOS DE VENTAS POR MES ───────────────────────────────────────────────
ventas_df = pd.DataFrame({
    "Mes": ["Ene", "Feb", "Mar", "Abr", "May", "Jun",
            "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"],
    "Ventas ($)": [
        3_200_000, 2_800_000, 4_100_000, 3_750_000,
        5_000_000, 4_600_000, 5_300_000, 4_900_000,
        5_800_000, 6_200_000, 5_500_000, 7_100_000,
    ],
})

# ── 5. SELECTOR DE RANGO DE FECHAS ───────────────────────────────────────────
st.subheader("📅 Selecciona el rango del reporte")

rango = st.date_input(
    "Rango de fechas:",
    value=(date(2024, 1, 1), date(2024, 12, 31)),
    min_value=date(2024, 1, 1),
    max_value=date(2024, 12, 31),
)

st.divider()

# ── 6. GRÁFICO DE LÍNEAS: VENTAS POR MES ────────────────────────────────────
st.subheader("📈 Ventas por mes (2024)")

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(
    ventas_df["Mes"],
    ventas_df["Ventas ($)"],
    marker="o",
    linewidth=2.5,
    color="#4C72B0",
    markerfacecolor="#E05C5C",
    markersize=8,
)
ax.fill_between(ventas_df["Mes"], ventas_df["Ventas ($)"], alpha=0.1, color="#4C72B0")
ax.set_xlabel("Mes")
ax.set_ylabel("Ventas (COP $)")
ax.set_title("Ventas mensuales 2024")
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"${x/1_000_000:.1f}M"))
ax.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()

st.pyplot(fig)

st.divider()

# ── 7. BOTÓN DE DESCARGA DE REPORTE ─────────────────────────────────────────
st.subheader("⬇️ Descargar reporte")

csv = ventas_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Descargar reporte en CSV",
    data=csv,
    file_name="reporte_ventas_2024.csv",
    mime="text/csv",
)