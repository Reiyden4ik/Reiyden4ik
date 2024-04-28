from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/test')
def test():
    return 'PIONEER!'
print('hi')