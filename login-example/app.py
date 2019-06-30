from database import *
from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
    

@app.route('/login', methods=['POST'])
def login():
    user = get_user(request.form['username'])
    if user != None and user.password == request.form["password"]:
        return render_template('logged.html',name = user.username)
    else:
        return home()


@app.route('/signup', methods=['POST'])
def signup():
    #check that username isn't taken
    user = get_user(request.form['username'])
    if user == None:
        create_user(request.form['username'],request.form['password'])
    return home()


@app.route('/logout')
def logout():
    return home()


if __name__ == '__main__':
    app.run(debug=True)
