from flask import Flask , render_template ,request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/survey' , methods=['POST'])
def survey():
    return render_template("survey.html" , survey_info=request.form)

if __name__ == "__main__":
    app.run(debug=True)