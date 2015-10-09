import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    return 'You have successfully logged in'

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
