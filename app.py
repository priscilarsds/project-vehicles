import pandas as pd
import plotly.express as px
import streamlit as st

# Título ajustado para a realidade do dataset
st.header('Análise de Anúncios de Carros Usados: Quilometragem e Preço')

# Carregamento do dataset
car_data = pd.read_csv('Cars dataset.csv')

# Botão para criar o Histograma
hist_button = st.button('Criar histograma')

if hist_button:
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig = px.histogram(car_data, x="km_driven", title="Distribuição de Quilometragem Rodada")
    st.plotly_chart(fig, use_container_width=True)

# Botão para criar o Gráfico de Dispersão
scatter_button = st.button('Criar gráfico de dispersão')

if scatter_button:
    st.write('Criando um gráfico de dispersão: Preço de Venda vs Quilometragem')
    fig_scatter = px.scatter(
        car_data, 
        x="km_driven", 
        y="selling_price", 
        title="Preço de Venda por Quilometragem"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)