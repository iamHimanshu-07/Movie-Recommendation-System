# Movie Recommendation System

Simple item-based collaborative filtering movie recommender (demo).

## Contents
- `movies.csv` - sample movie metadata
- `ratings.csv` - sample user ratings
- `movie_recommender.py` - Python script implementing item-based CF
- `project_report.pdf` - project report (abstract, methodology, results, conclusion)

## How to run
1. Install dependencies:
   ```
   pip install pandas scikit-learn scipy reportlab
   ```
2. Run:
   ```
   python movie_recommender.py
   ```

## Notes
- This is a small demo dataset. For real projects, use the MovieLens dataset.
- The recommender uses cosine similarity on item-user ratings matrix.
