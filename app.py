from flask import Flask
app = Flask(__name__)

##flask app routing

@app.route("/", methods=['GET', 'POST'])

def welcome():
    return "<h1>Hello, World!</h1>"

@app.route("/index", methods=['GET', 'POST'])

def index():
    return "<h1>Welcome to the Index Page!</h1>"
#variable rules

@app.route("/anant/<score>",methods=['GET', 'POST'])

def anant(score:int):
    return f"<h3>Welcome ANANT! Your score is {score}</h3>"
@app.route("/form",methods=['GET', 'POST'])


if __name__=='__main__':
    app.run(debug=True)