from flask import Flask, render_template,request
from flask_babel import Babel, _

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'zh'
babel = Babel(app)


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['zh', 'en'])


@app.route('/')
def hello():
    day = _("Saturday")

    return render_template('index.html', day=day)


if __name__ == '__main__':
    app.run(debug=True)


"""
代码汇总：

1、新建babel.cfg:
[python: **.py]
[jinja2: **/templates/**.html]
extensions=jinja2.ext.autoescape,jinja2.ext.with_
2、生成编译模板
pybabel extract -F babel.cfg -o messages.pot .
3、翻译
pybabel init -i messages.pot -d translations -l zh_Hans-CN
4、手动输入中文
messages.mo
5、编译翻译结果
pybabel compile -d translations
6、更新翻译
pybabel update -i messages.pot -d translations
"""