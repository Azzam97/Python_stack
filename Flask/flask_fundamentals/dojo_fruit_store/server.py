from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    f_name = request.form['first_name']
    l_name = request.form['last_name']
    full_name = f_name, l_name
    count = 0
    buyer_id = request.form['student_id']
    fruit1 = request.form['strawberry']
    fruit2 = request.form['raspberry']
    fruit3 = request.form['apple']
    fruit4 = request.form['blackberry']
    count = int(fruit1) + int(fruit2) + int(fruit3) + int(fruit4)
    print(f'Charging {full_name} for {count} fruits')
    print(request.form)
    return render_template(
                            "checkout.html",
                            strawberry = fruit1,
                            raspberry = fruit2,
                            apple = fruit3,
                            blackberry = fruit4,
                            first_name = f_name,
                            last_name = l_name,
                            id = buyer_id
                        )

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    