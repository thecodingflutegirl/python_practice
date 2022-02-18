from distutils.log import Log
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)
app.secret_key = 'shhh-something-secret'


class Login(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Length(min=8, max=30), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=8, max=30)])
    submit = SubmitField('Login')


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    form = Login()
    if form.validate_on_submit():
        if form.email.data == 'admin@email.com' and form.password.data == '12345678':
            return render_template('success.html')
        else:
            return render_template('denied.html')

    return render_template('login.html', title='login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
