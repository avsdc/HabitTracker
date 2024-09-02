**Description**

Habit Tracker is a project in Python, Html and CSV. It tracks six habits - walking, running, dance-workout, reading, meditation, 
and cooking for each month of the year.
In main.py the routes are created, two for each month i.e. a route for reading from csv into the read html file, and a route for 
writing to csv file from the write html file for each month. For e.g. for the month of January, data from day-habits-jan.csv is 
read into the january-read.html under endpoint /january_read, and function january_read, and january-read.html is rendered. 
Each html file for reading from csv file for each month, such as january_read.html consists of two tables, the first one table1 
displays the days of the month, and the second table i.e. table2 displays the six habits. The number of minutes for each habit 
each day is determined by the number of emojis. For e.g. two emojis for walking imply that a person walked for 20 * 2 i.e. 40 minutes. 
An X entered in any field implies that no action occurred on the given day for the specified habit.The january_write function 
under january_write endpoint allows data to be added to the day-habits-jan.csv, by using the january-add.html.
From the home page there is a link to the first page of the year i.e. january-read.html. From january-read.html, there is a forward 
link to the february-read.html, and a back link to the home page. Thereafter, each page for reading for the remining months has a 
forward link to the next month, and a back link to the previous month, and in addition, a link to the home page. December has a back 
link to november, and a link to the home page.


**Requirements:**

Using pip install, instll the following:


Flask 2.3.2
WTForms==3.0.1
Flask_WTF==1.2.1
Werkzeug==3.0.0
flask_sqlalchemy==3.1.1
SQLAlchemy==2.0.25



