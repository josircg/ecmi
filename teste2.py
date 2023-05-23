import streamlit as st
import pandas as pd

st.title('Teste ECMI 2')

st.write("Tabela")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))
