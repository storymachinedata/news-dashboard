# here we download pycountry pacakge to convert the country codes in two alphabet form which are
# basically the country code

import streamlit as st
import requests as re
import pycountry as py
# from api import apiKEY

myKey= 'ebaa63cf9dfa430d8f20bb9f7726ed03'
st.title('News App')
# now for dividing whole screen into two parts we can use st.columns
col1,col2=st.columns([2,1]) # 75,25

with col1:
    #user=st.text_input('Enter country name')
    user = st.selectbox('Choose your country',
            ('Argentina','Australia','Austria','Belgium','Brazil','Canada','China','Czechia','France','Germany','Greece','Hungary','India','Ireland','Israel','Italy','Japan','Mexico','Netherlands','Poland','Portugal','Russia','Sweden','Turkey','Ukraine','United Kingdom','United States'))
    btn= st.button('Enter')

with col2:
   st.image("https://www.storymachine.de/assets2/img/storymachine.png", width=200)


if btn:
    country=py.countries.get(name=user).alpha_2
    url=f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={myKey}"
    r = re.get(url)
    r=r.json()# here we have everything all the components of news
    articles = r['articles']

    #print(articles[0])

    for article in articles:
        st.header(article['title'])
        if article['author']:
            st.write('Author:',article['author'])
        #st.write('Source:',article['source']['name'])
        st.write('Url:',article['url'])
        st.write('Published At:',article['publishedAt'])


        try:
            st.image(article['urlToImage'])
        except Exception:
            pass






