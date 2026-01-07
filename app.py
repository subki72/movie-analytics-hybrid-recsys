import streamlit as st
import pandas as pd
import joblib
import ast
from deep_translator import GoogleTranslator

# ==============================================================================
# 1. LOAD DATA
# ==============================================================================
@st.cache_resource
def load_data():
    movies_small = joblib.load('Models/movie_data.pkl')
    cosine_sim = joblib.load('Models/cosine_sim.pkl')
    indices = joblib.load('Models/indices.pkl')
    return movies_small, cosine_sim, indices

movies_small, cosine_sim, indices = load_data()

# ==============================================================================
# 2. HELPER FUNCTION
# ==============================================================================
def clean_genre_format(raw_data):
    try:
        if isinstance(raw_data, str):
            data_list = ast.literal_eval(raw_data)
        else:
            data_list = raw_data
        genre_names = [item['name'] for item in data_list]
        return ", ".join(genre_names)
    except:
        return "Unknown"

# ==============================================================================
# 3. WEB UserInterface
# ==============================================================================
st.title("Movie Recommendation Engine")
st.write("Bingung mau nonton apa? Pilih film favorit lo di bawah:")

movie_list = indices.index.tolist()
selected_movie = st.selectbox("Pilih Film Favorit:", movie_list)

if st.button("Cari Rekomendasi"):
    try:
        idx = indices[selected_movie]
        
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:6] 
        
        movie_indices = [i[0] for i in sim_scores]
        recommendations = movies_small.iloc[movie_indices]
        
        st.success(f"Karena lu suka **{selected_movie}**, ini rekomendasi buat lu:")
        
        # Translator
        translator = GoogleTranslator(source='auto', target='id')
        
        # Progress bar
        progress_text = "Sedang menerjemahkan sinopsis... Sabar ya!"
        my_bar = st.progress(0, text=progress_text)
        total_items = len(recommendations)

        for i, (index, row) in enumerate(recommendations.iterrows()):
            my_bar.progress((i + 1) / total_items, text=progress_text)
            
            nice_genre = clean_genre_format(row['genres'])
            
            # Translate Sinopsis
            try:
                overview_indo = translator.translate(row['overview'])
            except:
                overview_indo = row['overview']
            
            with st.expander(f"{row['original_title']}"):
                st.caption(f"Genre: {nice_genre}")
                st.write("**Sinopsis:**")
                st.write(overview_indo)
                st.markdown("---")
                st.write(f"Rating Asli: {row['vote_average']}")
        
        my_bar.empty()
            
    except Exception as e:
        st.error(f"Waduh, ada error: {e}")
