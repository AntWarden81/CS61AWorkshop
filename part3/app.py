import os
from flask import Flask, render_template, g
import requests

app = Flask(__name__, instance_relative_config=True)

@app.route('/')
def index(name=None):
    print("in index")
    g.name = name
    return render_template('index.html')

@app.route('/categories')
def categories():
    categories = requests.get('http://jservice.io/api/categories/', data={'count': 10})
    categories_json = categories.json()
    ids = [category['id'] for category in categories_json]
    titles = [category['title'] for category in categories_json]
    print(ids, titles, categories_json)
    return render_template('categories.html')

@app.route('/category/<category_id>')
def get_question_from_category(category_id=None):
    return render_template('question.html')

@app.route('/question')
def get_random_question():
    question_obj = requests.get('http://jservice.io/api/random').json()[0]
    question, answer = question_obj['question'], question_obj['answer']
    print(question_obj)
    print(question, answer)
    return render_template('question.html')

@app.route('/answer')
def check_answer():
    print('check answer')
    return render_template('answer.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    # aapp.run(host='0.0.0.0', port=port)
    app.run()
