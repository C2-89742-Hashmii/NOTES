
from flask import Flask

app = Flask(__name__)



@app.route("/", methods=['GET'])

def index():
    return "WELCOME TO THE WORLD OF FLASK  "

app.run(port=5000 , host="0.0.0.0", debug=True)

 