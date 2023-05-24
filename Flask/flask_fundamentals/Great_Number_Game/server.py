from flask import Flask, render_template, session, redirect, request
import random

app = Flask(__name__)
app.secret_key = "not telling you"


@app.route('/')
def make_random():
    session['number'] = random.randint(1, 100)
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def compare_results():
    number = int(request.form['guess'])
    if number > session['number']:
        text = "Too High"
        color = "red"
    elif number < session['number']:
        text = "Too Low"
        color = "red"
    else:
        text = f"{str(number)} was the correct answer"
        color = "green"
    return render_template('index.html', text=text, color=color)


if __name__ == ('__main__'):
    app.run(debug=True)
