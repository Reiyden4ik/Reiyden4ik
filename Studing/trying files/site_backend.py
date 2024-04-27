from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Серега, ты лучший ♥"

@app.route('/api', methods=['GET'])
def get_data():
    data = {
        'fuck this all'
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

#http://localhost:5000
#http://localhost:5000/api