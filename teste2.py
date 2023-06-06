import streamlit as st
import pandas as pd
import numpy as np

st.title('Teste ECMI 2')

st.write("Tabela")

lista_salario = [10, 20, 30, 40] 
lista_nomes = ['Josir', 'Bruno', 'Bruna', 'Anna']

texto = st.text_input("Digite um nome")
salario = float(st.text_input("Digite o salário", "0"))
if texto:
    lista_nomes.append(texto)
    lista_salario.append(salario)

    dataframe = pd.DataFrame({
        'Nome': lista_nomes,
        'Salário': lista_salario
    })

    dataframe.style.highlight_max(axis=0)

    st.write(dataframe)

    chart_data = pd.DataFrame(
         np.random.randn(20, 3),
         columns=['a', 'b', 'c'])

    st.bar_chart(chart_data)
