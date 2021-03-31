from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def say_route(name):
    return "Hi"+ " " +str(name.capitalize())+"!"

@app.route('/repeat/<int:value>/<name>')
def repeat_names(value , name):
    return int(value) * (" " + str(name))

if __name__=="__main__":
    app.run(debug=True)
