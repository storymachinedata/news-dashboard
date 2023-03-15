# here we download pycountry pacakge to convert the country codes in two alphabet form which are
# basically the country code

from unicodedata import category
import streamlit as st
import requests as re
import pycountry as py
# from api import apiKEY

myKey= 'ebaa63cf9dfa430d8f20bb9f7726ed03'

st.set_page_config(layout="centered")


st.markdown(
        f"""
<style>
    .reportview-container .main .block-container{{
        max-width: {400}px;
        
    }}
 
</style>
""",
        unsafe_allow_html=True,
    )






st.image("https://www.storymachine.de/assets2/img/storymachine.png", width=200)
st.title('News Dashboard')
# now for dividing whole screen into two parts we can use st.columns
col1,col2=st.columns([2,1]) # 75,25


with col1:
    #user=st.text_input('Enter country name')
    user = st.selectbox('Choose your country',
            ('Argentina','Australia','Austria','Belgium','Brazil','Canada','China','Czechia','France','Germany','Greece','Hungary','India','Ireland','Israel','Italy','Japan','Mexico','Netherlands','Poland','Portugal','Russia','Sweden','Turkey','Ukraine','United Kingdom','United States'))
    user2 = st.selectbox('Choose the category',
            ('business','entertainment','general','health','science','sports','technology'))
    btn= st.button('Enter')

   


if btn:
    country=py.countries.get(name=user).alpha_2
    
    url=f"https://newsapi.org/v2/top-headlines?country={country}&category={user2}&apiKey={myKey}"
    r = re.get(url)
    r=r.json()# here we have everything all the components of news
    articles = r['articles']


    for article in articles:
        st.header(article['title'])
        if article['author']:
            st.write('Author:',article['author'])
        #st.write('Source:',article['source']['name'])
        st.write('Url:',article['url'],unsafe_allow_html=True)
        #st.write('Published At:',article['publishedAt'])


        try:
            st.image(article['urlToImage'])
        except Exception:
            pass



