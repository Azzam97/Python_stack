"""
    this program runs an app to give me a diffirent number of boxes based on the route used
"""

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def level_1():
    return render_template('index.html')

@app.route('/play/<int:num>')
def level_2(num):
    return render_template('index_number.html', num)

@app.route('/play/<int:num>/<color>')
def level_3(num , color):
    return render_template('index_number_color.html', num, colour=color)

if __name__=="__main__":
    app.run(debug=True)