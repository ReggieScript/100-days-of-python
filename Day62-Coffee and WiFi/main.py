from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField(label = "Location", validators=[DataRequired(),URL()])
    openTime = StringField(label="Opening time",validators=[DataRequired()])
    closingTime = StringField(label = "Closing Time", validators=[DataRequired()])
    coffeeRating = SelectField(label="Coffee Rating", validators=[DataRequired()], choices=["✘","☕️", "☕️☕️", "☕️☕️☕️", "☕️☕️☕️☕️", "☕️☕️☕️☕️☕️"])
    wifiRating = SelectField(label="Wifi Rating", validators=[DataRequired()], choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"])
    powerRating = SelectField(label="Power Rating", validators=[DataRequired()], choices=["✘","🔌","🔌🔌","🔌🔌🔌","🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"])
    submit = SubmitField(label="Add Cafe")


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods= ["GET","POST"])
def add_cafe():
    form = CafeForm(request.form)
    new_cafe = []
    form.validate_on_submit()
    if form.validate_on_submit():
        print("True")
        for field in form:
            new_cafe.append(field.data)
            print(new_cafe)
        with open('Day62-Coffee and WiFi\cafe-data.csv','a', newline='/n', encoding="UTF8") as csv_file:
            csv_data = csv.writer(csv_file)
            csv_data.writerow(new_cafe)
        return app.redirect("/add")
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('Day62-Coffee and WiFi\cafe-data.csv', encoding="UTF8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
