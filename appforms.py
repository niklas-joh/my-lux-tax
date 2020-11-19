from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

# Load secret key from file
app.config.from_json('config.json')

# Get secret keys from config.json
app.secret_key = app.config['APP_SECRET_KEY']
app.config['SESSION_TYPE'] = 'filesystem'

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return 'Form Successfully Submitted!'
    return render_template('formlogin.html', title='Sign In', form=form)

if __name__ == '__main__':
    app.run(debug=True)