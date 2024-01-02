import streamlit as st
import pandas as pd
from bs4 import BeautifulSoup
import requests
import json
from functions import scraping_bdm

st.set_page_config(
    page_title = 'ff',
    page_icon = '',
    layout = 'wide',
)

st.title('Home')

res = None

with st.form("First Form"):
    user_input = st.text_input("Tap your text")
    
    if st.form_submit_button('Send'):
        res = scraping_bdm(f'https://www.blogdumoderateur.com/?s={user_input}/')

col1, col2 = st.columns(2)

if res:
    df = pd.DataFrame(res).T
    csv = df.to_csv().encode('utf-8')

    with col1:
        st.write(f'Télécharger les {len(res)} article.s ?')

    with col2:
        st.download_button(
            "Press to Download",
            csv,
            "file.csv",
            "text/csv",
            key='download-csv'
        )
else :
    st.write('Aucuns résultats trouvés')