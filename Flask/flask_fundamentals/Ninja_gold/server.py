from flask import Flask, render_template, redirect, request, session
import random
from datetime import datetime


app = Flask(__name__)
app.secret_key = "ninja"

text = []


@app.route('/')
def game_start():
    if 'gold'  not in session:
        session['gold'] = 0
        session['amount'] = 0
        session['text'] = []
    gold = session['gold']
    text = session['text']
    amount = session['amount'] 
    return render_template('index.html', gold = gold, text = text, amount = amount)

@app.route('/clear', methods = ['POST'])
def clear():
    session.clear()
    return redirect('/')

@app.route('/process_money', methods=['POST'])
def process():
    now = datetime.now()
    timestamp = now.strftime("%Y/%m/%d %I:%M:%S %p")
    method = request.form['building']
    if method == 'farm':
        amount = random.randint(10, 20)
        session['gold'] += amount
        session['amount'] = amount
        text = (0, f"earned {amount} golds from the farm ! {timestamp}")
    elif method == 'cave':
        amount = random.randint(5, 10)
        session['gold'] += amount
        session['amount'] = amount
        text = (0, f"earned {amount} golds from the cave ! {timestamp}")
    elif method == 'house':
        amount = random.randint(2, 5)
        session['gold'] += amount
        session['amount'] = amount
        text = (0, f"earned {amount} golds from the house ! {timestamp}")
    elif method == 'casino':
        amount = random.randint(-50, 50)
        session['gold'] += amount
        if amount >= 0:
            session['amount'] = amount
            text = (
                0, f"earned {amount} golds from the casino ! {timestamp}")
        else:
            session['amount'] = amount
            text = (
                0, f"entered a casino and lost {amount} golds...ouch ! {timestamp}")
    session['text'].insert(0,text)
    return redirect('/',)


if __name__ == '__main__':
    app.run(debug=True)
