from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def form():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def survey():
    name = request.form['your-name']
    location = request.form['location']
    language = request.form['language']
    gender = request.form['gender']
    list = request.form.getlist('hobby')
    comment = request.form['comment']
    return render_template(
                          'result.html',
                          name = name,
                          location = location,
                          language = language,
                          comment = comment,
                          gender = gender,
                          list = list
                        )

if __name__=='__main__':
    app.run(debug=True)