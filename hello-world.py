from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World'

@app.route('/user/<user_name>')
def user_name(user_name): 
    return "Hello " + user_name + "!"

if __name__ == '__main__':
    app.run(host='0.0.0.0')