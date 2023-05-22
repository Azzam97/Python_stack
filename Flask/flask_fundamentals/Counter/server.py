from flask import Flask, render_template, request, redirect,session


app = Flask(__name__)
app.secret_key = "it's a secret"

@app.route('/')
def visits():
    if 'visits' in session:
        session['visits'] = int(session.get('visits')) + 1
        session['users'] = int(session.get('users')) + 1
    else:
        session['visits'] = 1
        session['users'] = 1
    return render_template('index.html', count = session['visits'], users = session['users'])

@app.route('/destroy_session', methods=['POST'])
def destroy():
    session.clear()
    return redirect('/')

@app.route('/plus_two', methods=['POST'])
def plus_two():
    session['visits'] = session['visits'] + 2
    session['users'] = session['users'] + 1
    return render_template('index.html', count = session['visits'], users = session['users'])

@app.route('/reset', methods=['POST'])
def reset():
    session['visits'] = 0
    return redirect('/')

@app.route('/increment', methods=['POST'])
def increment():
    x = request.form['increment']
    session['visits'] = session['visits'] + int(x)
    session['users'] = session['users'] + 1
    return render_template('index.html', count = session['visits'], users = session['users'])

if __name__ == '__main__':
    app.run(debug=True)