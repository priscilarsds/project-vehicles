import streamlit as st

# Título do aplicativo
st.title("Meu Primeiro Aplicativo Web de Veículos")

# Texto descritivo
st.write("Olá! Este é um aplicativo web interativo criado em Python e hospedado na nuvem.")

# Um botão interativo simples
if st.button("Clique em mim"):
    st.success("Parabéns! O Streamlit está funcionando perfeitamente.")