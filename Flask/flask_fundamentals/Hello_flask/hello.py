from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return " Dojo"

@app.route('/<name>')
def faliure(name):
    return "Hi "+ name

@app.route('/repeate/<num>/<name>')
def repeate(name, num):
    repetition = int (num)       #convert the number from string into an int to be used in the return statement
    return name * repetition

if __name__=="__main__":
    app.run(debug=True)
