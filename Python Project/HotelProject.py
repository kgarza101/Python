from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def base():
    return render_template('base.html')

if __name__ == "__main__":
    app.run(debug=True)
    
@app.route('/login')
def login():
    return render_template("login.html") 
    
@app.route('/logout')
def logout():
    return render_template("logout.html") 

@app.route('/hotelhome')
def hotelhome():
    return render_template("hotelhome.html") 
 
