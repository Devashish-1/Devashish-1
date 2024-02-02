import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.decomposition import TruncatedSVD
from flask import Flask, render_template, request

def load_movie_data():
    new_data = pd.read_csv('C:\Users\devas\OneDrive\Desktop\html css main proj\movie reccomendation')
    return new_data

def preprocess_data(movie_data):
    return movie_data

def train_svd_model(train_data):
    user_item_matrix = train_data.pivot_table(index='userId', columns='movieId', values='rating').fillna(0)
    n_components = min(user_item_matrix.shape[0], user_item_matrix.shape[1])
    SVD = TruncatedSVD(n_components=n_components)
    matrix = SVD.fit_transform(user_item_matrix)

    return SVD, matrix

app = Flask(__name__)
movie_data = load_movie_data()
movie_data = preprocess_data(movie_data)
train_data, test_data = train_test_split(movie_data, test_size=0.2, random_state=42)
svd_model, svd_matrix = train_svd_model(train_data)

def recommend_movies(movie_title):
    return ['Movie A', 'Movie B', 'Movie C']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommendations', methods=['POST'])
def get_recommendations():
    movie_title = request.form['movie_title']
    recommendations = recommend_movies(movie_title)
    return render_template('recommendations.html', movie_title=movie_title, recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
