from flask import Flask, render_template
app = Flask(__name__)

@app.route('/checkerboard/<repeat>')
def index(repeat):
    return render_template("index.html" , num_repeat=int(repeat))

if __name__=="__main__":
    app.run(debug=True)
