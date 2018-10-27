# Set up flask
from flask import Flask
app = Flask(__name__)

# The route of this request. The hello() function is called when you call this path.
@app.route('/')
def hello():
    return 'Hello world'
