# import streamlit as st
# from config.configuration import AppConfiguration
# from components.recommender import Recommender
# import pickle

# config = AppConfiguration()

# st.header("Books Recommender")

# book_names = pickle.load(open("templates/book_names.pkl",'rb'))

# selected = st.selectbox("Select Book",book_names)

# if st.button("Recommend"):
#     rec = Recommender().recommend(selected, config)
#     for i in rec[1:]:
#         st.write(i)

import streamlit as st
from config.configuration import AppConfiguration
from components.recommender import Recommender
import pickle

config = AppConfiguration()

st.header("Books Recommender")

book_names = pickle.load(open("templates/book_names.pkl",'rb'))

selected = st.selectbox("Select Book",book_names)

if st.button("Recommend"):

    rec_books, images = Recommender().recommend(selected, config)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(rec_books[1])
        st.image(images[1])

    with col2:
        st.text(rec_books[2])
        st.image(images[2])

    with col3:
        st.text(rec_books[3])
        st.image(images[3])

    with col4:
        st.text(rec_books[4])
        st.image(images[4])

    with col5:
        st.text(rec_books[5])
        st.image(images[5])
