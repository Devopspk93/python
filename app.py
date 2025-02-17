from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, this website is coming soon!W!ty!!W'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

