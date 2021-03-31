from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play/<int:repeat>/<color>')
def play(repeat , color):
    return render_template("index.html" , num_repeat=int(repeat) ,change_color=color)

if __name__=="__main__":
    app.run(debug=True)
