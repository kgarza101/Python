from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

# Setup app to use sqlalchemy database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sampledb.db"
db = SQLAlchemy(app)

# Step up a simple table for the database
class Visitor(db.Model):
    username = db.Column(db.String(100), primary_key=True)
    numVisits = db.Column(db.Integer, default=1)
    
    def __repr__(self): #prints data from database
        return f"{self.username} - {self.numVisits}"
# Create tables in database
with app.app_context():
    db.create_all()
    
# function to read in details for page 
def readDetails(filename):
    with open(filename, 'r') as f:
        return [line for line in f]
            
# make a homepage
@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/hello/<name>')
def hello(name):
    listOfNames = [name, "Yoyo", "Yennifer"]
    return render_template('name.html', name=name, nameList=listOfNames)

@app.route('/')
def aboutMe(name1):
    aboutlist = [name1, "Kayla"]
    return render_template('name.html', name1=name1, aboutlist=aboutlist)

@app.route('/form', methods=['GET', 'POST'])
def formDemo():
    name = None
    if request.method == 'POST':
        name = request.form['name']
        # check if user is in the database
        visitor = Visitor.query.get(name)
        if visitor == None:
            # add Visitor to the database
            visitor = Visitor(username=name)
            db.session.add(visitor)
        else:
            visitor.numVisits += 1
            
        db.session.commit()
    return render_template('form.html', name=name)

# Add in a page to view all vistors
@app.route('/visitors')
def visitors():
    people = Visitor.query.all()
    return render_template('visitors.html', people=people)

# add the option to run this file directly 
if __name__ == "__main__":
    app.run(debug=True)
    