from run import app
from flask import render_template
from flask import jsonify


@app.route('/')
def index():
    return render_template('index.html')
