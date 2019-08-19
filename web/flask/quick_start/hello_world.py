from flask import Flask,url_for
app = Flask(__name__)

@app.route('/hello/<name>')
def hello(name):
    return 'Hello %s!'%(name)

@app.route("/")
def index():
    return 'index page'

@app.route("/about")
def about():
    return 'about'

if __name__ == '__main__':
    app.debug = True
    app.run()