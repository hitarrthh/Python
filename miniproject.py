import streamlit as st
import pandas as pd

data = pd.read_csv('movies.csv')

ans = st.set_page_config(layout="wide", page_title='MINI PROJECT')
st.title('MOVIE RECOMMENDATION')

ans = ['Action', 'Comedy', 'Drama', 'Crime', 'Adventure', 'Mystery', 'History', 'Biography',
       'Thriller', 'Romance', 'Family', 'Horror', 'Sci-Fi', 'Music', 'War', 'Western', 'Animation',
       'Film-Noir']
ans.sort()

selected_genre = st.selectbox(label='Choose Genre', options=[None] + ans)

selected_adult = st.selectbox(label='Adult Content', options=[None, 'Yes', 'No'])

if selected_genre is not None and selected_adult is not None:
    recommend = data[
        (data['genre'].str.contains(selected_genre, case=False, na=False)) & (data['adult'] == selected_adult)
    ]

    if recommend.empty:
        st.write("SORRY, NO MOVIES FOUND FOR YOUR CRITERIA")
    else:
        st.write("RECOMMENDED MOVIES FOR YOU ARE:")
        recommended_movies = recommend.sort_values(by='rating', ascending=False)['title'].reset_index(drop=True)
        st.write(recommended_movies)  

    filtered_genre_gross = recommend.groupby('genre')['gross'].sum().sort_values(ascending=False)
    st.write("Gross Earnings by Genre")
    st.bar_chart(filtered_genre_gross)
