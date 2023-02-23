from flask import Flask, render_template, request
from helper import stringToJSON
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form['data']
        data = stringToJSON(data)
        return render_template('base.html', data=data)
    return render_template('base.html')