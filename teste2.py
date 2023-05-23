import streamlit as st
import pandas as pd

st.title('Teste ECMI 2')

st.write("Tabela")

dataframe = pd.DataFrame({
    'Nome': ['Josir', 'Bruno', 'Bruna', 'Anna'],
    'Salário': [10, 20, 30, 40]
})
dataframe.style.highlight_max(axis=0)

st.write(dataframe)
