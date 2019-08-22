from flask import Flask,g,render_template

app = Flask(__name__)


@app.context_processor
def inject_user():
    """上下文处理器使得模板可以使用一个名为 user ，值为 g.user 的变量"""
    return dict(user = g.user)


@app.route('/')
def index():
    g.user = 'keguang'
    return render_template('index.html')


@app.context_processor
def utility_processor():
    """上下文处理器也可以使某个函数在模板中可用"""
    def format_price(amount, currency=u'$'):
        return u'{0:.2f}{1}'.format(amount, currency)

    return dict(format_price=format_price)


if __name__ == '__main__':
    app.run(debug=True)