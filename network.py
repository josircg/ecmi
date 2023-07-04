import streamlit as st
import streamlit.components.v1 as components
import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network
import got
#Network(notebook=True)
st.title('Hello Pyvis')
# make Network show itself with repr_html

#def net_repr_html(self):
#  nodes, edges, height, width, options = self.get_network_data()
#  html = self.template.render(height=height, width=width, nodes=nodes, edges=edges, options=options)
#  return html

st.sidebar.title('Choose your favorite Graph')
option=st.sidebar.selectbox('select graph',
                            ('Simple', 'Karate', 'GOT'))
physics=st.sidebar.checkbox('add physics interactivity?')

if option == 'Simple':
    htmlfile = open("html/test.html", 'r', encoding='utf-8')
    source_code = htmlfile.read()
    components.html(source_code, height = 900,width=900)

if option == 'GOT':
    HtmlFile = open("gameofthrones.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read()
    components.html(source_code, height = 1200,width=1000)

if option == 'Karate':
    HtmlFile = open("html/karate.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read()
    components.html(source_code, height = 1200,width=1000)