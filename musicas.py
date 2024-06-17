import pandas as pd
import numpy as np
import streamlit as st
import random
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import string
import time

df = pd.read_csv('letras_musicas.csv')

st.set_page_config(page_icon='🎵')

with st.sidebar:
    st.subheader('Adivinhe: Um Jogo para Testar seus Conhecimentos Musicais')
    st.write('Esse projeto tem como objetivo oferecer um momento de diversão para qualquer pessoa com interesse em testar seus conhecimentos musicais!')
    st.write('Ao todo, são 70 músicas de 16 artistas (nacionais e internacionais)!')
    st.caption('Projeto desenvolvido por Clarissa Treptow, sob supervisão do Prof. Josir C. Gomes')
    st.caption('FGV ECMI')

def cores_diferentes():
    color_palettes = [
        'viridis', 'winter', 'summer', 'prism', 'Accent', 'Blues', 'Oranges',
        'GnBu', 'Purples', 'coolwarm', 'cool', 'gist_ncar_r', 'hsv', 'rainbow',
        'spring', 'magma'
    ]
    return random.choice(color_palettes)

def gerar_nuvem_e_opcoes(df):
    musica = df.sample(1).iloc[0]
    letra = musica['letra']
    artista_correto = musica['artista']
    
    wordcloud = WordCloud(width=800, height=400, background_color='white', colormap=cores_diferentes()).generate(letra)

    artistas_unicos = df[df['artista'] != artista_correto]['artista'].unique()    
    outros_artistas = np.random.choice(artistas_unicos, 4, replace=False).tolist()
    
    opcoes = outros_artistas + [artista_correto]
    random.shuffle(opcoes)
    
    return wordcloud, artista_correto, opcoes

if 'wordcloud' not in st.session_state:
    st.session_state.wordcloud, st.session_state.artista_correto, st.session_state.opcoes = gerar_nuvem_e_opcoes(df)

if 'rodada' not in st.session_state:
    st.session_state.rodada = 1

if 'pontuacao' not in st.session_state:
    st.session_state.pontuacao = 0

if st.session_state.rodada <= 10:
    st.title(f"Rodada {st.session_state.rodada} de 10: Adivinhe o Artista!")
    st.subheader("Por meio desta nuvem de palavras, tente adivinhar quem é o artista desta música:")
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(st.session_state.wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)

    escolha = st.radio("Quem é o artista desta música?", st.session_state.opcoes)

    if st.button("Verificar"):
        if escolha == st.session_state.artista_correto:
            st.success("Parabéns! Você acertou!")
            st.session_state.pontuacao += 5
        else:
            st.error(f"Que pena! A resposta correta é {st.session_state.artista_correto}.")
            st.session_state.pontuacao -= 5
        
        st.session_state.rodada += 1
        
        if st.session_state.rodada <= 10:
            st.session_state.wordcloud, st.session_state.artista_correto, st.session_state.opcoes = gerar_nuvem_e_opcoes(df)
            st.experimental_rerun()
        else:
            st.balloons()
            st.write(f"Jogo terminado! Sua pontuação final é: {st.session_state.pontuacao} pontos")

else:
    st.write(f"Jogo terminado! Sua pontuação final é: {st.session_state.pontuacao}")
    st.button("Reiniciar", on_click=lambda: [st.session_state.update({'rodada': 1, 'pontuacao': 0})])
