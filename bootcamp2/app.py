from flask import Flask, request, jsonify, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_form', methods=['POST'])
def process_form():
    name = request.form['name']
    birthdate = request.form['birthdate']
    birth_date_obj = datetime.strptime(birthdate, '%Y-%m-%d')
    age = (datetime.now() - birth_date_obj).days // 365
    response = {
        'name': name,
        'birthdate': birthdate,
        'age': age
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
