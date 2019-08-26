from flask import Flask
import config

app = Flask(__name__)

# 通过Class加载配置，推荐
app.config.from_object(config.Config2)


@app.route('/')
def default_config():
    # flask内置配置
    app.config['DEBUG'] = True
    # 用户自己的配置，属性名必须大写
    app.config['NAME'] = 'keguang'
    for key, value in app.config.items():
        print(key, '=>', value)

    return 'default_config()'


@app.route('/config')
def load_config_file():
    for key, value in app.config.items():
        print(key, '=>', value)

    return 'load_config_file()'


if __name__ == '__main__':
    app.run()
