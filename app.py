from flask import Flask, render_template, request
from helper import stringToJSON
app = Flask(__name__)

data = ""
jsonString = ""
@app.route("/", methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        jsonString = request.form['jsonString']
        data = request.form['jsonString']
        data = stringToJSON(data)
        return render_template('index.html', jsonString = jsonString, classObject=data)
    else:
        return render_template('index.html')
  

if __name__ == "__main__":
    app.run(debug=True)