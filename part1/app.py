import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/route1')
def route1():
    return 'This is route1'

@app.route('/route2/<param>')
def route2(param=None):
    param = int(param)
    if param > 5:
        return '%s is greater than 5' % param
    else:
        return '%s is less than 5' % param

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True)
