from flask import Flask

app = Flask(__name__)

@app.route('/')
def get_table():
    return "Hello world!"


@app.route('/health')
def is_health():
    return '{"status": "OK"}'


@app.errorhandler(404)
def page_not_found(e):
    return '404', 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)