import os

from flask import Flask, render_template, g

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
    def hello(name=None):
        g.name = name
        return render_template('index.html')

    @app.route('/kitty')
    @app.route('/kitty/<name>')
    @app.route('/<name>/kitty')
    def kitty(name=None):
        g.name = name
        return render_template('kitty.html')

    @app.route('/puppy')
    @app.route('/puppy/<name>')
    @app.route('/<name>/puppy')
    def puppy(name=None):
        g.name = name
        return render_template('puppy.html')

    @app.route('/get/character')
    # https://swapi.co/api/people/?search=r2
    def getChar():
        return render_template('query.html')

    @app.route('/get/character/<name>')
    def showChar
        return render_template('display.html')

    return app

