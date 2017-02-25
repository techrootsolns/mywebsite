import json
from flask import Flask, render_template
from webapp import app

@app.route('/')
@app.route('/home')
def index():
    return render_template('main.html')

