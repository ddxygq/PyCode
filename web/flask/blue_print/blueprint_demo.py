from flask import Flask,url_for,render_template,redirect
from app_blueprint.simple_page import simple_page


app = Flask(__name__)
app.register_blueprint(simple_page)


@app.route('/test')
def test():
    return redirect(url_for('simple_page.show'))


if __name__ == '__main__':
    app.run()