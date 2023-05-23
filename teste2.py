import streamlit as st
import pandas as pd

st.title('Teste ECMI 2')

st.write("Tabela")
st.write(pd.DataFrame({
    'Nome': ['Josir', 'Bruno', 'Bruna', 'Anna'],
    'Salário': [10, 20, 30, 40]
}))
