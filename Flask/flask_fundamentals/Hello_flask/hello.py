"""
    this program runs an app to give me a welcome page based on my diffirent routes
"""


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

@app.route('/repeate/<int:num>/<name>')
def repeate(name, num):
    return name * num

if __name__=="__main__":
    app.run(debug=True)
