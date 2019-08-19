from flask import Flask, request,make_response,render_template,g

app = Flask(__name__)


@app.route('/')
def index():
    """
    访问根目录
    """
    username = request.cookies.get('Hm_lvt_c8c69d3a72a8d2f94296b68d15bb0560')
    return username


@app.route('/set_cookie')
def set_cookie():
    user_lang = request.cookies.get('user_lang')
    return render_template('cookie_demo.html', name=user_lang)


@app.after_request
def call_after_request_callbacks(response):
    for callback in getattr(g, 'after_request_callbacks', ()):
        result = callback(response)
        '''
        'NoneType' object is not callable 解决办法
        https://stackoverflow.com/questions/11939858/flask-nonetype-object-is-not-callable
        '''
        # response = callback(response)
        # https://stackoverflow.com/questions/11939858/flask-nonetype-object-is-not-callable
        if result is not None:
            response = result
    return response


def after_this_request(f):
    if not hasattr(g, 'after_request_callbacks'):
        g.after_request_callbacks = []
    g.after_request_callbacks.append(f)
    return f


@app.before_request
def detect_user_language():
    print('goto detect_user_language')
    language = request.cookies.get('user_lang')
    if language is None:
        print('goto language is None')
        language = 'zh-cn'
        @after_this_request
        def remember_language(response):
            print('goto remember_language')
            response.set_cookie('user_lang', language)
    g.language = language

@app.route('/cookie')
def cookie():
    resp = make_response(render_template('hello.html'))
    resp.set_cookie('username', 'keguang')
    return resp

if __name__ == '__main__':
    app.run(debug=True)