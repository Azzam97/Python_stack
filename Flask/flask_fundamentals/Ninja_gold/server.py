from flask import Flask, render_template,redirect, request, session
import random

app = Flask(__name__)
app.secret_key = "ninja"

@app.route('/')
def game_start():
    session['gold'] = 0
    return render_template('index.html', gold = session['gold'])

@app.route('/process_money', methods=['POST'])
def process():
    method = request.form['building']
    if method == 'farm':
        amount = random.randint(10,20)
        text = f"earned {amount} golds from the farm"
    elif method == 'cave':
        amount = random.randint(5,10)
        text = f"earned {amount} golds from the cave"
    elif method == 'house':
        amount = random.randint(2,5)
        text = f"earned {amount} golds from the house"
    elif method == 'casino':
        amount = random.randint(-50,50)
        if amount >= 0:
            text = f"earned {amount} golds from the casino"
        else:
            text = f"entered a casino and lost {amount} golds...ouch"
    session['gold'] = amount + session['gold']
    return render_template('index.html', gold = session['gold'], text = text)

if __name__ == '__main__':
    app.run(debug=True)