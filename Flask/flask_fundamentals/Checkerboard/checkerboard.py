"""
    this program runs an app to give me a checkerboard based on the diffirent variables
"""

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def checkerboard1():
    return render_template('index.html')

@app.route('/<int:ver_num>')
def checkerboard2(ver_num):
    return render_template('index_vertical.html', ver_num)

@app.route('/<int:hor_num>/<int:ver_num>')
def checkerboard3(hor_num,ver_num):
    return render_template('index_horizental_vertical.html',hor_num , ver_num)

if __name__=='__main__':
    app.run(debug=True)
