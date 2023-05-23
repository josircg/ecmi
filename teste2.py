import streamlit as st
import pandas as pd
import numpy as np

st.title('Teste ECMI 2')

st.write("Tabela")

dataframe = pd.DataFrame({
    'Nome': ['Josir', 'Bruno', 'Bruna', 'Anna'],
    'Salário': [10, 20, 30, 40]
})
dataframe.style.highlight_max(axis=0)

st.write(dataframe)

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)
