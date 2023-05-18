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
    y = ver_num
    return render_template('index_row.html', row = y)

@app.route('/<int:hor_num>/<int:ver_num>')
def checkerboard3(hor_num,ver_num):
    x = hor_num
    y = ver_num
    return render_template('index_row_line.html', row = x , line = y)

@app.route('/<int:hor_num>/<int:ver_num>/<color1>/<color2>')
def checkerboard4(hor_num, ver_num, color1, color2):
    x = hor_num
    y = ver_num
    return render_template('index_new_colors.html', row = x, line = y, colour1 = color1, colour2 = color2)

if __name__=='__main__':
    app.run(debug=True)
