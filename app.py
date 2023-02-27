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
        print(data)
        return render_template('index.html', jsonString = jsonString, classObjects=data)
    else:
        return render_template('index.html')
    
  

if __name__ == "__main__":
    app.run(debug=True)
    