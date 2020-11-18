from flask import Flask, render_template, session
app = Flask(__name__)

# Store secret keys in config file to hide from view on Github
# 
# See https://github.com/MirelaI/flask_config_example for tutorial
# !!! Remember to add config.json to .gitignore !!!
app.config.from_json('config.json')

# Get secret keys from config.json
app.secret_key = app.config['APP_SECRET_KEY']
app.config['SESSION_TYPE'] = 'filesystem'

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/user/<user_name>')
def user_name(user_name): 
    return "Hello " + user_name + "!"

@app.route('/about')
def about():
   return render_template('about.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')