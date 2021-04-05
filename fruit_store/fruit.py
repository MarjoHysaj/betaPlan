from flask import Flask, render_template, request, redirect ,url_for
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])
def checkout():
    fruit_count = int(request.form['strawberry']) + int(request.form['apple']) + int(request.form['blackberry'])
    fruits = {
        'sb': request.form['strawberry'],
        'ap': request.form['apple'],
        'rs': request.form['raspberry'],
        'bb': request.form['blackberry'],
        'fn': request.form['first_name'],
        'ln': request.form['last_name'],
        'sid': request.form['student_id'],
        'fc': request.form['fruit_count']
    }
    print("Charging {} {} for {} fruits".format(request.form['first_name'],request.form['last_name'],request.form['fruit_count']))
    return render_template("checkout.html" , dojo_fruit=fruits)
    
@app.route('/fruits')
def fruits():
    return render_template("fruits.html")
    
if __name__=="__main__":
    app.run(debug=True)