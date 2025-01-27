from flask import Flask, render_template, url_for, request, flash, redirect, session
import requests

app = Flask(__name__)
app.secret_key = 'my_secrete_key'


API_URL = 'http://127.0.0.1:3000'

@app.route('/', methods=['GET', 'POST'])
def landing_page():
    return render_template('landing_page.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template('dashboard.html')



if __name__ == '__main__':
    app.run(port=5000, debug=True)
