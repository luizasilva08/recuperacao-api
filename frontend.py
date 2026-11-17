
import streamlit as st
from consumidor_api import obter_dados_meteorologicos

st.set_page_config(
    page_title="Monitoramento Meteorológico",
    page_icon="🌦️",
    layout="wide"
)

st.title("🌦️ Monitoramento Meteorológico")
st.caption("Estação meteorológica — Jaraguá do Sul/SC")

st.divider()

if st.button("🔄 Atualizar dados"):
    st.rerun()

try:
    with st.spinner("Consultando a API meteorológica..."):
        dados = obter_dados_meteorologicos()

    st.success("Dados meteorológicos carregados.")

    st.subheader("Condições atuais")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Temperatura",
        f"{dados["current"]["temperature_2m"]:.1f} °C"
    )

    col2.metric(
        "Umidade relativa",
        f"{dados["current"]["relative_humidity_2m"]:.0f} %"
    )

    col3.metric(
        "Sensação térmica",
        f"{dados["current"]["apparent_temperature"]:.1f} °C"
    )

    col4, col5 = st.columns(2)

    col4.metric(
        "Precipitação",
        f"{dados["current"]["precipitation"]:.1f} mm"
    )

    col5.metric(
        "Velocidade do vento",
        f"{dados["current"]["wind_speed_10m"]:.1f} km/h"
    )

    st.divider()

    st.caption(f"Horário dos dados: {dados["current"]["time"]}")

except Exception as erro:
    st.error(f"Não foi possível consultar os dados: {erro}")


