
from flask import Flask , render_template

app =Flask(__name__)


@app.route('/', methods=['GET'])

def index():
    return render_template('index.html')
    

@app.route('/test', methods=['GET'])

def test():
    return "TEST"

app.run(port=5500, host="0.0.0.0" , debug=True)
