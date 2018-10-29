import os

from flask import Flask, render_template, g

import requests

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
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


    return app
