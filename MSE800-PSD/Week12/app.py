from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_flask():
    return "<p> Hello Flask </p>"


@app.route('/bye')
def bye():
    return "<p> Bye </p>"

if __name__ == 'name':
    app.run(debug=True)


@app.route('/username/<name>')
def learn(name):
    return f"{name} is using Flask"\

@app.route('/var/<name>/<int:number>')
def two_var(name, number):
    return f"{name} is using Flask with number {number}"

if __name__ == 'name':
    app.run(debug=True)