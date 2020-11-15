# import dependencies and create the app
from flask import Flask, render_template, url_for, request, redirect, g
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Classes.db'
db = SQLAlchemy(app)
name = "Name"

class StudentClass(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(255), nullable=False, server_default="Generic Course")
    link = db.Column(db.String(255), server_default="https://www.google.com")
    day = db.Column(db.String(10))
    start = db.Column(db.Time, default=datetime.time(0, 0))
    end = db.Column(db.Time, default=datetime.time(0, 0))

@app.route('/delete/<int:id>')
def delete(id):
    to_delete = StudentClass.query.get_or_404(id)
    try:
        db.session.delete(to_delete)
        db.session.commit()
        return redirect('/configure')
    except:
        redirect('/error')

@app.route('/setName', methods=["POST"])
def setName():
    global name
    name = request.form['name']
    return redirect('/configure')

# get list the daily classes
def getClasses(today):
    if (today == "Sunday"):
        classes =  StudentClass.query.filter(StudentClass.day=="Sunday").order_by(StudentClass.start)
    elif (today == "Monday"):
        classes = StudentClass.query.filter(StudentClass.day=="Monday").order_by(StudentClass.start)
    elif (today == "Tuesday"):
        classes = StudentClass.query.filter(StudentClass.day=="Tuesday").order_by(StudentClass.start)
    elif (today == "Wednesday"):
        classes = StudentClass.query.filter(StudentClass.day=="Wednesday").order_by(StudentClass.start)
    elif (today == "Thursday"):
        classes = StudentClass.query.filter(StudentClass.day=="Thursday").order_by(StudentClass.start)
    elif (today == "Friday"):
        classes = StudentClass.query.filter(StudentClass.day=="Friday").order_by(StudentClass.start)
    elif (today == "Saturday"):
        classes = StudentClass.query.filter(StudentClass.day=="Saturday").order_by(StudentClass.start)
    return classes

# get list of upcoming classes
def getNext(classes):
    upcoming = []
    now = datetime.datetime.now().time()

    for course in classes:
        #if start time >= current time
        if (course.end >= now):
            upcoming.append(course)
    return upcoming

# get the current class
def getCurrent(upcoming):
    return upcoming.pop(0)
    
# get the previous classes
def getPrevious(classes):
    previous = []
    now = datetime.datetime.now().time()

    for course in classes:
        if (course.end < now):
            previous.append(course)
    return previous

# index page
@app.route('/')
def index():
    global name
    today = datetime.datetime.now().strftime('%A')
    cTime = datetime.datetime.now()
    sTime = cTime.strftime('%H:%M')

    # sort the classes
    classes = getClasses(today)
    upcoming = getNext(classes)
    current = getCurrent(upcoming)
    previous = getPrevious(classes)

    return render_template('/public/index.html', name=name, ctime=sTime, today=today, upcoming=upcoming, current=current, previous=previous)

# configure page for adding / remoiving classes
@app.route('/configure', methods=['POST', 'GET'])
def configure():
    if request.method == 'POST':
        title = request.form['title']
        if title == "": title = "Generic Course"
        link = request.form['link']
        if link == "": link = "https://www.google.com"
        day = request.form['day']
        try:
            s1, s2 = request.form['start'].split(':', 1)
            e1, e2 = request.form['end'].split(':', 1)
        except:
            s1 = 0
            s2 = 0
            e1 = 0
            e2 = 0        
        start = datetime.time(int(s1), int(s2))
        end = datetime.time(int(e1), int(e2))
        
        # create new entry into db
        new_class = StudentClass(title=title, link=link, day=day, start=start, end=end)
        # push to db
        try:
            db.session.add(new_class)
            db.session.commit()
            return redirect('/configure')
        except:
            return redirect('/error')

    else:
        classes = StudentClass.query.order_by(StudentClass.start).all()
        #classes = StudentClass.query.filter(StudentClass.day=="Sunday").order_by(StudentClass.start)
        return render_template("/public/configure.html", classes=classes)

@app.route('/error', methods=['POST', 'GET'])
def error():
    if request.method == 'POST':
        return redirect('/error')
    else:
        return '''
            <a href="/"><p>there was an error. click here to go to the home page</p></a>
        '''

if __name__ == "__main__":
    app.run(debug=True)