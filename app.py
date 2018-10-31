import os
from flask import Flask, render_template, g, request
import requests
import random

app = Flask(__name__)

@app.route('/')
def index(name=None):
    return render_template('index.html')

@app.route('/categories')
def categories():
    categories = requests.get('http://jservice.io/api/categories/', data={'count': 6})
    categories_json = categories.json()
    return render_template('categories.html', **locals())

@app.route('/category/<category_id>')
def get_question_from_category(category_id=None):
    question_list = requests.get('http://jservice.io/api/category', data={'id': category_id}).json()['clues']
    question_obj = random.choice(question_list)
    question, answer = question_obj['question'], question_obj['answer']
    return render_template('question.html', **locals())

@app.route('/question')
def get_random_question():
    question_obj = requests.get('http://jservice.io/api/random').json()[0]
    question, answer = question_obj['question'], question_obj['answer']
    return render_template('question.html', **locals())

@app.route('/answer', methods=['GET'])
def check_answer():
    input_answer = request.args['input_answer']
    real_answer = request.args['real_answer']
    correct_answer_string = 'Correct' if input_answer.lower() == real_answer.lower() else 'Incorrect'
    return render_template('answer.html', **locals())

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    # app.run(host='0.0.0.0', port=port, debug=True)
    app.run(debug=True)
