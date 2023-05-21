"""
    this program runs an app to give me a diffirent number of boxes based on the route
"""

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def level_1():
    return render_template('index.html', number = 3, colour = 'aqua')

@app.route('/play/<int:num>')
def level_2(num):
    x = num
    return render_template('index.html', number = x, colour = 'aqua')

@app.route('/play/<int:num>/<color>')
def level_3(num , color):
    x = num
    return render_template('index.html', number = x, colour = color)

if __name__=="__main__":
    app.run(debug=True)