from flask import Flask

app = Flask(__name__)

@app.route('/app')
def hello():
    return 'Hello, world!'

if __name__ == '__main__':
    app.run()