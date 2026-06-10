"""

Simple item-based collaborative filtering recommender using cosine similarity.

"""

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import csr_matrix
import numpy as np

def load_data(path="."):
    movies = pd.read_csv(f"{path}/movies.csv")
    ratings = pd.read_csv(f"{path}/ratings.csv")
    return movies, ratings

def build_item_user_matrix(ratings):
    # pivot to item-user matrix (rows: movieId, cols: userId)
    mat = ratings.pivot_table(index='movieId', columns='userId', values='rating').fillna(0)
    return mat

def compute_item_similarity(item_user_mat):
    # cosine similarity between items
    mat = item_user_mat.values
    sim = cosine_similarity(mat)
    sim_df = pd.DataFrame(sim, index=item_user_mat.index, columns=item_user_mat.index)
    return sim_df

def recommend_for_user(user_id, movies, ratings, sim_df, top_n=5):
    # get user ratings
    user_ratings = ratings[ratings.userId == user_id]
    if user_ratings.empty:
        return []

    # score candidate items by weighted sum of similarities * rating
    scores = {}
    for _, row in user_ratings.iterrows():
        mid = row['movieId']
        rating = row['rating']
        if mid not in sim_df.index:
            continue
        sim_series = sim_df[mid]
        for item, sim in sim_series.items():
            if item in user_ratings['movieId'].values:
                continue
            scores.setdefault(item, 0)
            scores[item] += sim * rating

    # normalize and sort
    if not scores:
        return []
    scored = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    recommended = [int(item) for item, _ in scored[:top_n]]
    return movies[movies.movieId.isin(recommended)][['movieId','title','genres']]

def main(path="."):
    movies, ratings = load_data(path)
    # ensure ids are integers
    ratings['movieId'] = ratings['movieId'].astype(int)
    ratings['userId'] = ratings['userId'].astype(int)
    movies['movieId'] = movies['movieId'].astype(int)

    item_user_mat = build_item_user_matrix(ratings)
    sim_df = compute_item_similarity(item_user_mat)

    example_users = sorted(ratings['userId'].unique())
    print("Example users in data:", example_users)
    for uid in example_users:
        recs = recommend_for_user(uid, movies, ratings, sim_df, top_n=5)
        print(f"Recommendations for user {uid}:")
        if recs.empty:
            print("  No recommendations (user rated all items or no data).")
        else:
            print(recs.to_string(index=False))
        print("-"*40)

if __name__ == "__main__":
    main(path=".")
