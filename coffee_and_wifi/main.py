
from attr import field
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, URLField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

COFFEE_CHOICES = [('☕️'), ('☕️☕️'), ('☕️☕️☕️'),
                  ('☕️☕️☕️☕️'), ('☕️☕️☕️☕️☕️')]
WIFI_CHOICES = [('✘'), ('💪'), ('💪💪'),
                ('💪💪💪'), ('💪💪💪💪'), ('💪💪💪💪💪')]
OUTLET_CHOICES = [('🔌'), ('🔌🔌'), ('🔌🔌🔌'),
                  ('🔌🔌🔌🔌'), ('🔌🔌🔌🔌🔌')]


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = URLField('Location', validators=[DataRequired(), URL()])
    open_time = StringField('Opening time', validators=[DataRequired()])
    close_time = StringField('Closing time', validators=[DataRequired()])
    coffee = SelectField(
        'Coffee Rating', choices=COFFEE_CHOICES, validators=[DataRequired()])
    wifi = SelectField('Wifi', choices=WIFI_CHOICES, validators=[
                       DataRequired()], render_kw={'style': 'width: 16ch'})
    outlets = SelectField(
        'Power Outlets', choices=OUTLET_CHOICES, validators=[DataRequired()])
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafe-data.csv', 'a') as csv_file:
            csv_file.write(f"\n{form.cafe.data},"
                           f"{form.location.data},"
                           f"{form.open_time.data},"
                           f"{form.close_time.data},"
                           f"{form.coffee.data},"
                           f"{form.wifi.data},"
                           f"{form.outlets.data}")
            csv_file.close()
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
