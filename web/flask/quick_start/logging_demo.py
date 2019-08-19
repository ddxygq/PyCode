from flask import Flask

app = Flask(__name__)


@app.route('/logger')
def log():
    app.logger.debug('debug log')
    app.logger.warning('warning log')
    app.logger.error('error log')

    return '''
    <h1>logger</h1>
    '''

if __name__ == '__main__':
    app.run(debug=True)