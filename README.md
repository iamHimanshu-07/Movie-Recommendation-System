# 🎬 Movie Recommendation System

A Movie Recommendation System built using **Item-Based Collaborative Filtering** and **Cosine Similarity** on the MovieLens dataset.

This project analyzes user rating patterns and recommends movies that users are likely to enjoy based on similarities between movies.

---

# 📖 Overview

Recommendation systems power many modern platforms such as Netflix, Amazon, Spotify, and YouTube.

This project demonstrates how collaborative filtering works by:

* Processing movie ratings from thousands of users
* Building an Item-User Matrix
* Computing movie similarities using Cosine Similarity
* Generating personalized movie recommendations

The project uses the MovieLens dataset containing:

* 9,742 Movies
* 100,836 Ratings
* 610 Users

---

# 🚀 Features

✅ Item-Based Collaborative Filtering

✅ Cosine Similarity Recommendation Engine

✅ MovieLens Dataset Integration

✅ Sparse Matrix Processing

✅ Personalized Top-N Recommendations

✅ Modular Python Implementation

---

# 🛠️ Technologies Used

| Technology   | Purpose                       |
| ------------ | ----------------------------- |
| Python       | Programming Language          |
| Pandas       | Data Processing               |
| NumPy        | Numerical Operations          |
| SciPy        | Sparse Matrix Handling        |
| Scikit-Learn | Cosine Similarity Calculation |

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/movie-recommendation-system.git

cd movie-recommendation-system
```

## Create Virtual Environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate.bat
```

Linux/Mac:

```bash
source venv/bin/activate.bat
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

Execute:

```bash
python movie_recommender.py
```

The program will:

1. Load movie data
2. Load ratings data
3. Build an Item-User Matrix
4. Calculate Movie Similarities
5. Generate Recommendations
   
Run:
<img width="1347" height="671" alt="image" src="https://github.com/user-attachments/assets/e0a47b17-e879-4b6d-b526-a83a03568ce0" />

---

# 🧠 Recommendation Pipeline

```text
Ratings Data
      │
      ▼
Item-User Matrix
      │
      ▼
Cosine Similarity
      │
      ▼
Similarity Matrix
      │
      ▼
Recommendation Engine
      │
      ▼
Top-N Recommended Movies
```
---

# 🎯 Sample Recommendation Flow

User Ratings:

```text
The Dark Knight      ★★★★★
Inception            ★★★★★
Interstellar         ★★★★☆
```

System Recommendation:

```text
Batman Begins
The Prestige
Memento
Fight Club
The Matrix
```

---

# 🌟 Applications

Recommendation systems are widely used in:

* Netflix
* Amazon
* Spotify
* YouTube
* Disney+
* E-Commerce Platforms
* Online Learning Platforms

---

# 👨‍💻 Author

Himanshu Singh Yadav

Machine Learning Enthusiast | Python Developer | Data Science Learner
