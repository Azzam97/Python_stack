from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'this is a secret'
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
    print("got post info")
    session['username'] = request.form['name']
    session['email'] = request.form['email']
    return redirect('/show')

@app.route('/show')
def show_user():
    print("Showing the User Info From the Form")
    print(request.form)
    return render_template("show.html")

if __name__ == "__main__":
    app.run(debug=True)