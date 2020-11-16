from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/user/<user_name>')
def user_name(user_name): 
    return "Hello " + user_name + "!"

if __name__ == '__main__':
    app.run(host='0.0.0.0')