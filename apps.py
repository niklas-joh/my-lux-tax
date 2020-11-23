from flask import flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydata.db'
# Store secret keys in config file to hide from view on Github
# 
# See https://github.com/MirelaI/flask_config_example for tutorial
# !!! Remember to add config.json to .gitignore !!!
app.config.from_json('config.json')

# Get secret keys from config.json
app.secret_key = app.config['APP_SECRET_KEY']
db = SQLAlchemy(app)