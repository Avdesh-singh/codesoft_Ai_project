import pandas as pd

# Load MovieLens dataset (replace with your local path)
movies = pd.read_csv('movies.csv')
ratings = pd.read_csv('ratings.csv')

# Merge the datasets on movieId
movie_data = pd.merge(ratings, movies, on='movieId')

# Pivot the data to create a user-item matrix
user_movie_matrix = movie_data.pivot_table(index='userId', columns='title', values='rating')
user_movie_matrix.fillna(0, inplace=True)

from sklearn.metrics.pairwise import cosine_similarity

# Compute the cosine similarity between users
user_similarity = cosine_similarity(user_movie_matrix)

# Convert the similarity matrix to a DataFrame
user_similarity_df = pd.DataFrame(user_similarity, index=user_movie_matrix.index, columns=user_movie_matrix.index)





def recommend_movies(user_id, num_recommendations=5):
    similar_users = user_similarity_df[user_id].sort_values(ascending=False).index[1:]
    user_ratings = user_movie_matrix.loc[similar_users].mean(axis=0)
    user_watched_movies = user_movie_matrix.loc[user_id][user_movie_matrix.loc[user_id] > 0].index
    recommendations = user_ratings.drop(user_watched_movies).sort_values(ascending=False).head(num_recommendations)
    return recommendations




import streamlit as st

# Streamlit App
st.title("Simple Movie Recommendation System")

user_id = st.number_input("Enter User ID", min_value=1, max_value=user_movie_matrix.index.max())

if st.button('Recommend Movies'):
    recommendations = recommend_movies(user_id)
    st.write("Here are the recommended movies for you:")
    for i, movie in enumerate(recommendations.index, 1):
        st.write(f"{i}. {movie}")

