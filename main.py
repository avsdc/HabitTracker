from flask import Flask, render_template, redirect, url_for, jsonify, request
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, URL

import csv

from bs4 import BeautifulSoup

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt 

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

var = 0
j = 0
m = 0
habit_list = []
daylist = []


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

class HabitForm(FlaskForm):
        walk = SelectField('Walking', choices=["✘", "🚶‍", "🚶‍🚶‍", "🚶‍🚶‍🚶‍", "🚶‍🚶‍🚶‍🚶‍", "🚶‍🚶‍🚶‍🚶‍🚶‍", "🚶‍🚶‍🚶‍🚶‍🚶‍🚶‍"], validators=[DataRequired()])
        run = SelectField('Running', choices=["✘", "🏃‍", "🏃‍‍🏃️‍️️", "🏃🏃‍♀️🏃‍♀️", "🏃🏃‍🏃‍♀️️🏃‍♀️", "🏃‍♀️🏃‍♀️🏃‍♀️🏃‍♀️🏃‍♀️", "🏃‍♀️🏃‍🏃‍🏃‍🏃‍🏃‍♀️️️️️️"], validators=[DataRequired()])
        dance = SelectField('DanceWorkout', choices=["✘", "💃", "💃💃", "💃💃💃", "💃💃💃💃", "💃💃💃💃💃", "💃💃💃💃💃💃"], validators=[DataRequired()])
        read = SelectField('Reading', choices=["✘", "👩‍🏫", "👩‍🏫👩‍🏫", "👩‍🏫👩‍🏫👩‍🏫", "👩‍🏫👩‍🏫👩‍🏫👩‍🏫", "👩‍🏫👩‍🏫👩‍🏫👩‍🏫👩‍🏫", "👩‍🏫👩‍🏫👩‍🏫👩‍🏫👩‍🏫👩‍🏫"], validators=[DataRequired()])
        meditate = SelectField('Meditating', choices=["✘", "🧘‍♀️", "🧘‍♀️🧘‍♀️", "🧘‍♀️🧘‍♀️🧘‍♀️", "🧘‍♀️🧘‍♀️🧘‍♀️🧘‍♀️", "🧘‍♀️🧘‍🧘‍🧘‍🧘‍♀️️️️", "🧘‍♀️🧘‍♀️🧘‍♀️🧘‍♀️🧘‍♀️🧘‍♀️"], validators=[DataRequired()])
        cook = SelectField('Cooking', choices=["✘", "👩‍🍳", "👩‍🍳👩‍🍳", "👩‍🍳👩‍🍳👩‍🍳", "👩‍🍳👩‍🍳👩‍🍳👩‍🍳", "👩‍🍳👩‍🍳👩‍🍳👩‍🍳👩‍🍳", "👩‍🍳👩‍🍳👩‍🍳👩‍🍳👩‍🍳👩‍🍳"], validators=[DataRequired()])
        submit = SubmitField('Submit')

# all Flask routes below

# Display the home page
@app.route("/")
def home():
    return render_template("index.html")

#Display habits for January
@app.route('/january_read')
def january_read():

        data = []
        with open('day-habits/day-habits-jan.csv', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                data.append(row)
        return render_template('january-read.html', data=data, i=var)


# Add habits for January
@app.route('/january_write', methods=['GET', 'POST'])
def january_write():
    form = HabitForm()

    if form.validate_on_submit():
        with open("day-habits/day-habits-jan.csv", mode="a", encoding='utf-8') as csv_file:
            csv_file.write(f"\n{form.walk.data},"
                           f"{form.run.data},"
                           f"{form.dance.data},"
                           f"{form.read.data},"
                           f"{form.meditate.data},"
                           f"{form.cook.data}")
            return redirect(url_for('january_read'))
    return render_template('january-add.html', form=form)



# Display February
@app.route('/february_read')
def february_read():
    data = []
    with open('day-habits/day-habits-feb.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            data.append(row)
        return render_template('february-read.html', data=data, i=var)


# Add habits for February
@app.route('/february_write', methods=['GET', 'POST'])
def february_write():
    form = HabitForm()

    if form.validate_on_submit():
        with open("day-habits/day-habits-feb.csv", mode="a", encoding='utf-8') as csv_file:
            csv_file.write(f"\n{form.walk.data},"
                           f"{form.run.data},"
                           f"{form.dance.data},"
                           f"{form.read.data},"
                           f"{form.meditate.data},"
                           f"{form.cook.data}")
            return redirect(url_for('february_read'))
    return render_template('february-add.html', form=form)


# Display March
@app.route('/march_read')
def march_read():
    data = []
    with open('day-habits/day-habits-march.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            data.append(row)
        return render_template('march-read.html', data=data, i=var)



#Add habits for March
@app.route('/march_write', methods=['GET', 'POST'])
def march_write():
    form = HabitForm()

    if form.validate_on_submit():
        with open("day-habits/day-habits-march.csv", mode="a", encoding='utf-8') as csv_file:
            csv_file.write(f"\n{form.walk.data},"
                           f"{form.run.data},"
                           f"{form.dance.data},"
                           f"{form.read.data},"
                           f"{form.meditate.data},"
                           f"{form.cook.data}")
            return redirect(url_for('march_read'))
    return render_template('march-add.html', form=form)


# Display habits for April
@app.route('/april_read')
def april_read():
    data = []
    with open('day-habits/day-habits-april.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            data.append(row)
        return render_template('april-read.html', data=data, i=var)


#Add habits for April
@app.route('/april_write', methods=['GET', 'POST'])
def april_write():
    form = HabitForm()

    if form.validate_on_submit():
        with open("day-habits/day-habits-april.csv", mode="a", encoding='utf-8') as csv_file:
            csv_file.write(f"\n{form.walk.data},"
                           f"{form.run.data},"
                           f"{form.dance.data},"
                           f"{form.read.data},"
                           f"{form.meditate.data},"
                           f"{form.cook.data}")
            return redirect(url_for('april_read'))
    return render_template('april-add.html', form=form)


# Display habits for May
@app.route('/may_read')
def may_read():
    data = []
    with open('day-habits/day-habits-may.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            data.append(row)
        return render_template('may-read.html', data=data, i=var)


# Add habits for May
@app.route('/may_write', methods=['GET', 'POST'])
def may_write():
    form = HabitForm()

    if form.validate_on_submit():
        with open("day-habits/day-habits-may.csv", mode="a", encoding='utf-8') as csv_file:
            csv_file.write(f"\n{form.walk.data},"
                           f"{form.run.data},"
                           f"{form.dance.data},"
                           f"{form.read.data},"
                           f"{form.meditate.data},"
                           f"{form.cook.data}")
            return redirect(url_for('may_read'))
    return render_template('may-add.html', form=form)


# Display habits for June
@app.route('/june_read')
def june_read():
    data = []
    with open('day-habits/day-habits-june.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            data.append(row)
        return render_template('june-read.html', data=data, i=var)


# Add habits for June
@app.route('/june_write', methods=['GET', 'POST'])
def june_write():
    form = HabitForm()

    if form.validate_on_submit():
        with open("day-habits/day-habits-june.csv", mode="a", encoding='utf-8') as csv_file:
            csv_file.write(f"\n{form.walk.data},"
                           f"{form.run.data},"
                           f"{form.dance.data},"
                           f"{form.read.data},"
                           f"{form.meditate.data},"
                           f"{form.cook.data}")
            return redirect(url_for('june_read'))
    return render_template('june-add.html', form=form)


# Display habits for July
@app.route('/july_read')
def july_read():
    data = []
    with open('day-habits/day-habits-july.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            data.append(row)
        return render_template('july-read.html', data=data, i=var)

# Add habits for July
@app.route('/july_write', methods=['GET', 'POST'])
def july_write():
    form = HabitForm()

    if form.validate_on_submit():
        with open("day-habits/day-habits-july.csv", mode="a", encoding='utf-8') as csv_file:
            csv_file.write(f"\n{form.walk.data},"
                           f"{form.run.data},"
                           f"{form.dance.data},"
                           f"{form.read.data},"
                           f"{form.meditate.data},"
                           f"{form.cook.data}")
            return redirect(url_for('july_read'))
    return render_template('july-add.html', form=form)


# Display habits for August
@app.route('/august_read')
def august_read():
    data = []
    with open('day-habits/day-habits-aug.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            data.append(row)
        return render_template('august-read.html', data=data, i=var)

# Add habits for August
@app.route('/august_write', methods=['GET', 'POST'])
def august_write():
    form = HabitForm()

    if form.validate_on_submit():
        with open("day-habits/day-habits-aug.csv", mode="a", encoding='utf-8') as csv_file:
            csv_file.write(f"\n{form.walk.data},"
                           f"{form.run.data},"
                           f"{form.dance.data},"
                           f"{form.read.data},"
                           f"{form.meditate.data},"
                           f"{form.cook.data}")
            return redirect(url_for('august_read'))
    return render_template('august-add.html', form=form)


# Display habits for September
@app.route('/september_read')
def september_read():
    data = []
    with open('day-habits/day-habits-sept.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            data.append(row)
        return render_template('september-read.html', data=data, i=var)


# Add habits for September
@app.route('/september_write', methods=['GET', 'POST'])
def september_write():
    form = HabitForm()

    if form.validate_on_submit():
        with open("day-habits/day-habits-sept.csv", mode="a", encoding='utf-8') as csv_file:
            csv_file.write(f"\n{form.walk.data},"
                           f"{form.run.data},"
                           f"{form.dance.data},"
                           f"{form.read.data},"
                           f"{form.meditate.data},"
                           f"{form.cook.data}")
            return redirect(url_for('september_read'))
    return render_template('september-add.html', form=form)


# Display habits for October
@app.route('/october_read')
def october_read():
    data = []
    with open('day-habits/day-habits-oct.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            data.append(row)
        return render_template('october-read.html', data=data, i=var)


# Add habits for October
@app.route('/october_write', methods=['GET', 'POST'])
def october_write():
    form = HabitForm()

    if form.validate_on_submit():
        with open("day-habits/day-habits-oct.csv", mode="a", encoding='utf-8') as csv_file:
            csv_file.write(f"\n{form.walk.data},"
                           f"{form.run.data},"
                           f"{form.dance.data},"
                           f"{form.read.data},"
                           f"{form.meditate.data},"
                           f"{form.cook.data}")
            return redirect(url_for('october_read'))
    return render_template('october-add.html', form=form)


# Display habits for November
@app.route('/november_read')
def november_read():
    data = []
    with open('day-habits/day-habits-nov.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            data.append(row)
        return render_template('november-read.html', data=data, i=var)


# Add habits for November
@app.route('/november_write', methods=['GET', 'POST'])
def november_write():
    form = HabitForm()

    if form.validate_on_submit():
        with open("day-habits/day-habits-nov.csv", mode="a", encoding='utf-8') as csv_file:
            csv_file.write(f"\n{form.walk.data},"
                           f"{form.run.data},"
                           f"{form.dance.data},"
                           f"{form.read.data},"
                           f"{form.meditate.data},"
                           f"{form.cook.data}")
            return redirect(url_for('november_read'))
    return render_template('november-add.html', form=form)



# Display habits for December
@app.route('/december_read')
def december_read():
    data = []
    with open('day-habits/day-habits-dec.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            data.append(row)
        return render_template('december-read.html', data=data, i=var)


# Add habits for December
@app.route('/december_write', methods=['GET', 'POST'])
def december_write():
    form = HabitForm()

    if form.validate_on_submit():
        with open("day-habits/day-habits-dec.csv", mode="a", encoding='utf-8') as csv_file:
            csv_file.write(f"\n{form.walk.data},"
                           f"{form.run.data},"
                           f"{form.dance.data},"
                           f"{form.read.data},"
                           f"{form.meditate.data},"
                           f"{form.cook.data}")
            return redirect(url_for('december_read'))
    return render_template('december-add.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
