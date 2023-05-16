import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import numpy as np

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data
  
def test_file():
    # Create a text element and let the reader know the data is loading.
    data_load_state = st.text('Loading data...')
    # Load 10,000 rows of data into the dataframe.
    data = load_data(10000)
    # Notify the reader that the data was successfully loaded.
    data_load_state.text("Done!")

st.title('Teste ECMI')
st.set_option('deprecation.showPyplotGlobalUse', False)
st.sidebar.header("Select Link")
links = ["https://seaportai.com/blog-predictive-maintenance/",
         "https://seaportai.com/healthcare-analytics/",
         "https://seaportai.com/blog-rpameetsai/",
         "https://seaportai.com/covid-19/"]

URL = st.sidebar.selectbox('Link', links)
st.sidebar.header("Select No. of words you want to display")
words = st.sidebar.selectbox("No. of words", range(10, 1000, 10))
if URL is not None:
    r = requests.get(URL)
    #using the web scraping library that is Beautiful Soup
    soup = BeautifulSoup(r.content, 'html.parser')
    #extracting the data that is in 'div' content of HTML page
    table = soup.find('div', attrs = {'id':'main-content'})
    text = table.text
    #cleaning the data with regular expression library
    cleaned_text = re.sub('\t', "", text)
    cleaned_texts = re.split('\n', cleaned_text)
    cleaned_textss = "".join(cleaned_texts)
    st.write("Word Cloud Plot")
    #using stopwords to remove extra words
    stopwords = set(STOPWORDS)
    wordcloud = WordCloud(background_color = "white", max_words =
              words,stopwords = stopwords).generate(cleaned_textss)
    plt.imshow(wordcloud, interpolation = 'bilinear')
    plt.axis("off")
    plt.show()
    st.pyplot()
