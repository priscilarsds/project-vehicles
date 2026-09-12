import pandas as pd
import plotly.express as px
import streamlit as st

# Cabeçalho do aplicativo
st.header('Dashboard de Veículos de Luxo: Carros Esportivos', divider='rainbow')
st.write(
    'Este aplicativo web interativo foi desenvolvido para explorar dados de'
    ' veículos, com foco em modelos esportivos e de luxo.'
)

# Lendo o conjunto de dados
car_data = pd.read_csv('Cars dataset.csv')

# Filtrando apenas para a marca Maserati
maserati_data = car_data[
    car_data['brand'].str.contains('Maserati', case=False, na=False)
]

# Proteção: se o dataset escolhido não contiver Maserati, usamos o dataset completo para o app não ficar vazio
if maserati_data.empty:
  st.warning(
      'Nota: O arquivo CSV atual não possui registros da Maserati. Exibindo o'
      ' dataset geral para demonstração dos gráficos:'
  )
  df_plot = car_data
else:
  df_plot = maserati_data

# --- Seção do Histograma (Quilometragem) ---
st.subheader('Distribuição de Quilometragem (km_driven)')
hist_button = st.button('Criar histograma')

if hist_button:
  st.write('Criando um histograma para a quilometragem dos veículos...')
  fig_hist = px.histogram(df_plot, x='km_driven')
  st.plotly_chart(fig_hist, use_container_width=True)

# --- Seção do Gráfico de Dispersão (Preço x Quilometragem) ---
st.subheader('Relação entre Preço de Venda e Quilometragem')
scatter_button = st.button('Criar gráfico de dispersão')

if scatter_button:
  st.write('Criando um gráfico de dispersão (Preço x Quilometragem)...')
  fig_scatter = px.scatter(
      df_plot, x='km_driven', y='selling_price', color='fuel'
  )
  st.plotly_chart(fig_scatter, use_container_width=True)