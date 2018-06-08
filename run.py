import os
from datetime import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)