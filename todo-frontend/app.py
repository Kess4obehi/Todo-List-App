from flask import Flask, render_template, url_for, request, flash, redirect, session
import requests

app = Flask(__name__)
app.secret_key = 'my_secrete_key'


API_URL = 'http://127.0.0.1:3000'

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(port=5000, debug=True)
