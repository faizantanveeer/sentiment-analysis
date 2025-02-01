from flask import Flask, request, jsonify, render_template
from joblib import load
import numpy as np
from scipy.sparse import csr_matrix # Import for sparse matrix handling

app = Flask(__name__)

model = load('model.pkl') 
vect = load('vect.pkl')


print('vocab: ', len(vect.vocabulary_))

print('model: ', model.coef_.shape)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    name = request.form.get('name')
    email = request.form.get('email')
    review = request.form.get('review')

    review_vectorized = vect.transform([review])  # Transform the input

    if isinstance(review_vectorized, csr_matrix): # Check if it is a sparse matrix
        prediction = model.predict(review_vectorized)
    else: # It's not sparse
        prediction = model.predict(review_vectorized.toarray()) # then convert to array

    prediction_list = prediction.tolist()

    if prediction_list[0] == 0:
        sentiment = 'Negative'
    else:
        sentiment = 'Positive'
    return render_template('index.html', prediction_text=sentiment, review_text=review, name=name, email=email)


if __name__ == '__main__':
    app.run(debug=True)