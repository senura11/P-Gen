from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_password():
    length = int(request.form.get('length'))
    uppercase = 'on' if request.form.get('uppercase') else ''
    lowercase = 'on' if request.form.get('lowercase') else ''
    numbers = 'on' if request.form.get('numbers') else ''
    symbols = 'on' if request.form.get('symbols') else ''

    charset = ''
    if uppercase:
        charset += string.ascii_uppercase
    if lowercase:
        charset += string.ascii_lowercase
    if numbers:
        charset += string.digits
    if symbols:
        charset += string.punctuation

    password = ''.join(random.choice(charset) for _ in range(length))
    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run()
