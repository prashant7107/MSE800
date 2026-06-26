from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_flask():
    return """
    <!DOCTYPE html>
    <html style="background:green; color:red">
    <head>
        <title>Flask Website</title>
    </head>
    <body>
    <h1>Welcome!</h1>
    <p>Check out the documentation</p>
    <a href="https://flask.palletsprojects.com/en/stable/quickstart/">Flask Quickstart Guide</a>
    </body>
    </html>
    """

if __name__ == 'name':
    app.run(debug=True)